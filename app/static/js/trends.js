data = [4, 8, 15, 16, 23, 42];

const div = d3.select('body').append("div");

d3.selectAll("div").data(data).join("div").text(d => d);
