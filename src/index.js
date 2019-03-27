Plotly.d3.csv("https://raw.githubusercontent.com/JFBarryLi/DataViz/master/currency.csv", function(err, rows){

  function unpack(rows, key) {
  return rows.map(function(row) { return row[key]; });
}


var trace1 = {
  type: "scatter",
  mode: "lines",
  name: 'CAD',
  x: unpack(rows, 'Date'),
  y: unpack(rows, 'CAD'),
  line: {color: '#17BECF'}
}

var trace2 = {
  type: "scatter",
  mode: "lines",
  name: 'CNY',
  x: unpack(rows, 'Date'),
  y: unpack(rows, 'CNY'),
  line: {color: '#7F7F7F'}
}

var data = [trace1,trace2];

var layout = {
  title: 'USD vs CAD, USD vs CNY',
};

plotlyDiv = document.getElementById('plotly-example');
Plotly.newPlot('plotly-example', data, layout);
})