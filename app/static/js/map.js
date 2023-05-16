var getData = function() {
  fetch('/coordinates_data')
    .then(response => response.text()) // Parse the response body as text
    .then(data => {
      //add code to store data to a variable
      console.log(data); // Log the string data to the console
    })};



async function generatemap(){
  var key = '';
  await fetch('/mapboxapikey')
    .then(response => response.text())
    .then(data => {
      // add code to store data to a variable
       key = data; // return the data
    });
  
    mapboxgl.accessToken = key;

  const map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/streets-v11',
    center: [-73.98, 40.73],
    zoom: 10
  });

  var setPoint = function(planeid,longitude, latitude, summary){
    new mapboxgl.Marker()
        .setLngLat([longitude, latitude])
        .addTo(map);
  
        const popup = new mapboxgl.Popup({ offset: 25 }).setText(summary);
  
        // create DOM element for the marker
        const el = document.createElement('div');
        el.id = 'marker';
  
        // create the marker
        new mapboxgl.Marker(el)
        .setLngLat([longitude, latitude])
        .setPopup(popup) 
        .addTo(map);
  };


  return {
    map: map,
    setPoint: setPoint
  };
  
}

generatemap().then(result => {
  result.setPoint('plane1', -74.0, 40.7, 'Marker 1 Summary');
  result.setPoint('plane2', -73.9, 40.8, 'Marker 2 Summary');
});