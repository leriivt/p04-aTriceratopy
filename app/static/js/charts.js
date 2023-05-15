// set the dimensions and margins of the graph
var margin = {top: 10, right: 30, bottom: 30, left: 60},
    width = 460 - margin.left - margin.right,
    height = 400 - margin.top - margin.bottom;

// append the svg object to the body of the page
var svg = d3.select("#my_dataviz")
  .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform",
          "translate(" + margin.left + "," + margin.top + ")");

var rankings_data;

//Read the data
var getData = function() {
  fetch('/data')
    .then(response => response.text()) // Parse the response body as text
    .then(data => {
      //add code to store data to a variable
      rankings_data = data;
      console.log(data); // Log the string data to the console
    });
  }


  