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
  xaxis: {
    autorange: true,
    range: ['1981-06-10', '2016-11-30'],
    rangeselector: {buttons: [
        {
          count: 1,
          label: '1y',
          step: 'year',
          stepmode: 'backward'
        },
        {
          count: 5,
          label: '5y',
          step: 'year',
          stepmode: 'backward'
        },
        {
          count: 10,
          label: '10y',
          step: 'year',
          stepmode: 'backward'
        },
        {
          count: 20,
          label: '20y',
          step: 'year',
          stepmode: 'backward'
        },
        {
          count: 30,
          label: '30y',
          step: 'year',
          stepmode: 'backward'
        },
        {step: 'all'}
      ]},
    rangeslider: {range: ['1981-06-10', '2016-11-30']},
    type: 'date'
  },
  yaxis: {
    autorange: true,
    range: [0, 10],
    type: 'linear'
  }
};

plotlyDiv = document.getElementById('plotly-example');
Plotly.newPlot('plotly-example', data, layout);
})