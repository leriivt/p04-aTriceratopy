var getData = function() {
  fetch('/data')
    .then(response => response.text()) // Parse the response body as text
    .then(data => {
      //add code to store data to a variable
      console.log(data); // Log the string data to the console
    });

}


mapboxgl.accessToken = 'pk.eyJ1Ijoiam9ubmVlZSIsImEiOiJjbGhnajRrY2IwNTl1M2ZuejVoaHF6Z3N4In0.v1HJ4aKSzUZz0cmzdnYbrQ';

const map = new mapboxgl.Map({
  container: 'map',
  style: 'mapbox://styles/mapbox/streets-v11',
  center: [-73.98, 40.73],
  zoom: 10
});

map.on('load', () => {
  // Add a circle to the map at New York coordinates
  map.addLayer({
    'id': 'circle',
    'type': 'circle',
    'source': {
      'type': 'geojson',
      'data': {
        'type': 'Feature',
        'properties': {},
        'geometry': {
          'type': 'Point',
          'coordinates': [-73.98, 40.73] // New York coordinates
        }
      }
    },
    'paint': {
      'circle-radius': 10,
      'circle-color': 'red'
    }
  });
