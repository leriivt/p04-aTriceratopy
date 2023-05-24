google.charts.load('current', { 'packages': ['corechart'] });
google.charts.load('current', { packages: ['table'] });

google.charts.setOnLoadCallback(drawFunction);
//google.charts.setOnLoadCallback(drawTable);

async function getData() {
  try {
    return await fetch('/crashes_data')
      .then(response => response.text()) // Parse the response body as text
      .then(data => {
        crash = JSON.parse(data); // arr object
        //console.log(crash);
        return {
          crash: crash
        };
      });
  } catch {
    console.log("Data not present");
  }
}

getData().then(result => {
  var crashes_array = [['Decade', 'Crashes']];
  var fatalities_array = [['Decade', 'Fatalities']]
  for (var i = 1; i < 13; i++) {
    var decade = 1900 + ((i - 1) * 10);
    crashes_array.push([decade, 0]);
    fatalities_array.push([decade, 0])
  }

  var year, decade = 0;
  for (j = 0; j < result.crash.length; j++) {
    year = Number(result.crash[j][1].slice(-4));
    decade = year - (year % 10);
    var fatalities = 0
    if (result.crash[j][9] != "NULL") {
      fatalities = result.crash[j][9];
    }
    for (k = 0; k < crashes_array.length; k++) {
      if (crashes_array[k][0] == decade) {
        crashes_array[k][1] += 1;
        fatalities_array[k][1] += fatalities;
        break;
      }
    }
  }
  //console.log(fatalities_array)
  drawFunction(crashes_array, "Crashes by Decade", "Number of Crashes", "Decade", "crash_chart");
  drawFunction(fatalities_array, "Fatalities by Decade", "Number of Deaths", "Decade", "fatal_chart")

});


function drawFunction(arr, name, yaxis, xaxis, element) {

  var chart_data = google.visualization.arrayToDataTable(arr);

  var options = {
    title: name,
    curveType: 'function',
    legend: { position: 'bottom' },
    axisTitlesPosition: 'out',
    vAxis: { title: yaxis },
    hAxis: {
      title: xaxis,
      format: '####'
    }
  };

  var chart = new google.visualization.LineChart(document.getElementById(element));

  chart.draw(chart_data, options);
}