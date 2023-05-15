var getData = function() {
  fetch('/data')
    .then(response => response.text()) // Parse the response body as text
    .then(data => {
      //add code to store data to a variable
      console.log(data); // Log the string data to the console
    })};




const map = new mapboxgl.Map({
  container: 'map',
  style: 'mapbox://styles/mapbox/streets-v11',
  center: [-73.98, 40.73],
  zoom: 10
});

// map.on('load', () => {
//   // Add a circle to the map at New York coordinates
//   map.addLayer({
//     'id': 'circle',
//     'type': 'circle',
//     'source': {
//       'type': 'geojson',
//       'data': {
//         'type': 'Feature',
//         'properties': {},
//         'geometry': {
//           'type': 'Point',
//           'coordinates': [-73.98, 40.73] // New York coordinates
//         }
//       }
//     },
//     'paint': {
//       'circle-radius': 10,
//       'circle-color': 'red'
//     }
//   });
// });
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
      .setPopup(popup) // sets a popup on this marker
      .addTo(map);
}
