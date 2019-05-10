// Enter a speed between 0 and 180
// var level = 125;
if (pred_red === 'Poor Wine') {
  level = 45;
}
else if (pred_red === 'Average Wine'){
    level = 90;
  }
  
else level = 135;


// Trig to calc meter point
var degrees = 180 - level,
     radius = .5;
var radians = degrees * Math.PI / 180;
var x = radius * Math.cos(radians);
var y = radius * Math.sin(radians);

// Path: may have to change to create a better triangle
var mainPath = 'M -.0 -0.025 L .0 0.025 L ',
     pathX = String(x),
     space = ' ',
     pathY = String(y),
     pathEnd = ' Z';
var path = mainPath.concat(pathX,space,pathY,pathEnd);

var data = [{ type: 'scatter',
   x: [0], y:[0],
    marker: {size: 28, color:'850000'},
    showlegend: false,
    name: 'rotation',
    text: level,
    hoverinfo: 'text'},
  {values: [50/3, 50/3, 50/3, 50],
  rotation: 90,
  text: ['GREAT', 'AVERAGE', 'BAD', ''],
  textinfo: 'text',
  textposition:'inside',      
  marker: {colors:['RGBA(0, 128, 0, .9)', 'rgba(255, 195, 0, .8)',
                         'rgba(199, 0, 57, .9)', 
                         'rgba(255, 255, 255, 0)']},
  labels: ['2', '1', '0', ''],
  hoverinfo: 'label',
  hole: .5,
  type: 'pie',
  showlegend: false
}];

var layout = {
  shapes:[{
      type: 'path',
      path: path,
      fillcolor: '850000',
      line: {
        color: '850000'
      }
    }],
  title: '<br><b>Wine Gauge</b>',
  height: 1000,
  width: 1000,
  xaxis: {zeroline:false, showticklabels:false,
             showgrid: false, range: [-1, 1]},
  yaxis: {zeroline:false, showticklabels:false,
             showgrid: false, range: [-1, 1]}
};

Plotly.newPlot('RedDiv', data, layout, {showSendToCloud:true});