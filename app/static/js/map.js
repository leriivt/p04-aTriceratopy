async function generatemap() {
  var key = '';
  await fetch('/mapboxapikey')
    .then(response => response.text())
    .then(data => {
      // add code to store data to a variable
      key = data; // return the data
    });

  var listCoords = [];
  try {
    await fetch('/coordinates_data')
      .then(response => response.text()) // Parse the response body as text
      .then(data => {
        listCoords = JSON.parse(data); //list is arr object
      });
  } catch {
    console.log("Data not present");
  }

  var crash = []
  try {
    await fetch('/crashes_data')
      .then(response => response.text()) // Parse the response body as text
      .then(data => {
        crash = JSON.parse(data); //list is arr object
      });
  } catch {
    console.log("Data not present");
  }

  mapboxgl.accessToken = key;

  const map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/streets-v11',
    center: [-73.98, 40.73],
    zoom: 1
  });

  var setPoint = function (planeid, latitude, longitude, summary) {
    try{
      new mapboxgl.Marker()
      .setLngLat([latitude, longitude])
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
    }catch{
      console.log("invalid lat/long", "lat:" + latitude, "long:" + longitude);
    }

  };


  return {
    map: map,
    listCoords: listCoords,
    crash: crash,
    setPoint: setPoint
  };

}

//Updating range slider
function updateValue(value) {
  const timeperiod = document.getElementById('peroid');
  timeperiod.textContent = `${value}s`;
}

//Set Up range slider at leftmost
const rang = document.getElementById('timeperiod');
rang.value = rang.min;
updateValue(rang.value)

//plotting points
generatemap().then(result => {

    // console.log(Number(result.crash[i][1].slice(-4)));
    i = 0; 
  while(Number(result.crash[i][1].slice(-4)) < Number(rang.value)+100){
    result.setPoint(String(result.listCoords[i][0]), result.listCoords[i][2], result.listCoords[i][1], i);
    i++;
  }

});