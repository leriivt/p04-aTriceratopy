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

    const popup = new mapboxgl.Popup({ offset: 25 }).setHTML(summary);

    // create DOM element for the marker
    const el = document.createElement('div');
    el.id = 'marker';

    // create the marker
    new mapboxgl.Marker(el)
      .setLngLat([latitude, longitude])
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
//Set Up range slider at leftmost
const rang = document.getElementById('timeperiod');
rang.value = rang.min;
updateValue(rang.value) 

//Updating range slider
function updateValue(value) {
  const timeperiod = document.getElementById('peroid');
  timeperiod.textContent = `${value}s`;

  const rang = document.getElementById('timeperiod');
  console.log(Number(rang.value) + 10)
  if( 1915 < (Number(rang.value)+10) ) {
    console.log(true);
  }
  if( 1915 >= Number(rang.value)) {
    console.log(true);
  }
  generatemap().then(result => {
    for(i = 0; i < result.crash.length; i++){
      if(Number(result.crash[i][1].slice(-4)) < (Number(rang.value)+10) && Number(result.crash[i][1].slice(-4)) >= Number(rang.value)){
        summary = result.crash[i][1] + "<br>" + result.crash[i][2] + "<br>" + result.crash[i][11];
        result.setPoint(String(result.listCoords[i][0]), result.listCoords[i][2], result.listCoords[i][1], summary);
      }
    }
  });
}



