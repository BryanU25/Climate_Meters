// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Pie Chart Example
var ctx1 = document.getElementById("myPieChart1");
var myPieChart1 = new Chart(ctx1, {
  type: 'pie',
  data: {    
    datasets: [{      
      backgroundColor: ['#55ED55', '#FFFF55', '#FFA955', '#FF5555', '#A955AF'],
    }],
  },
});

var ctx2 = document.getElementById("myPieChart2");
var myPieChart2 = new Chart(ctx2, {
  type: 'pie',
  data: {
    datasets: [{     
      backgroundColor: ['#55ED55', '#FFFF55', '#FFA955', '#FF5555', '#A955AF'],
    }],
  },
});

var ctx3 = document.getElementById("myPieChart3");
var myPieChart3 = new Chart(ctx3, {
  type: 'pie',
  data: {
    datasets: [{
      backgroundColor: ['#55ED55', '#FFFF55', '#FFA955', '#FF5555', '#A955AF'],
    }],
  },
});

var ctx4 = document.getElementById('myPieChart4');
var myPieChart4 = new Chart(ctx4, {
  type: 'pie',  
  data: {
    datasets: [{            
      backgroundColor: ['#55ED55', '#FFFF55', '#FFA955', '#FF5555', '#A955AF'],
    }],
  },
});

var ctx = document.getElementById("myPieChart5");
var myPieChart5 = new Chart(ctx, {
  type: 'pie',
  data: {
    datasets: [{
      backgroundColor: ['#55ED55', '#FFFF55', '#FFA955', '#FF5555', '#A955AF'],
    }],
  },
});

var ctx = document.getElementById("myPieChart6");
var myPieChart6 = new Chart(ctx, {
  type: 'pie',
  data: {
    // labels: ["Blue", "Red", "Yellow", "Green"],
    datasets: [{
      backgroundColor: ['#55ED55', '#FFFF55', '#FFA955', '#FF5555', '#A955AF'],
    }],
  },
});

// Evento cuando cambia la selección
function actualizarGraficos(opcionSeleccionada) { 
  const nuevodato1= [150, 12, 30, 34, 2];
  const nuevodato2= [30, 40, 30, 0, 19];
  const nuevodato3= [16, 23, 12, 98, 0];
  const nuevodato4= [43, 26, 86, 2, 43];
  const nuevodato5= [35, 232, 13, 10, 14];
  const nuevodato6= [12, 76, 45, 43, 43];
  
    if (opcionSeleccionada == "Sensor1") {
      myPieChart1.data.datasets[0].data = nuevodato1;     
      myPieChart2.data.datasets[0].data = nuevodato2;
      myPieChart3.data.datasets[0].data = nuevodato3;      
      myPieChart4.data.datasets[0].data = nuevodato4;
      myPieChart5.data.datasets[0].data = nuevodato5;      
      myPieChart6.data.datasets[0].data = nuevodato6;
    } else if (opcionSeleccionada === "Sensor2") {
      myPieChart1.data.datasets[0].data = nuevodato2;      
      myPieChart2.data.datasets[0].data = nuevodato3;
      myPieChart3.data.datasets[0].data = nuevodato4;      
      myPieChart4.data.datasets[0].data = nuevodato5;
      myPieChart5.data.datasets[0].data = nuevodato6;      
      myPieChart6.data.datasets[0].data = nuevodato1;
    } else if (opcionSeleccionada === "Sensor3") {
      myPieChart1.data.datasets[0].data = nuevodato3;      
      myPieChart2.data.datasets[0].data = nuevodato4;
      myPieChart3.data.datasets[0].data = nuevodato5;      
      myPieChart4.data.datasets[0].data = nuevodato6;
      myPieChart5.data.datasets[0].data = nuevodato1;      
      myPieChart6.data.datasets[0].data = nuevodato2;
    } else if (opcionSeleccionada === "Sensor4") {
      myPieChart1.data.datasets[0].data = nuevodato4;      
      myPieChart2.data.datasets[0].data = nuevodato5;
      myPieChart3.data.datasets[0].data = nuevodato6;      
      myPieChart4.data.datasets[0].data = nuevodato1;
      myPieChart5.data.datasets[0].data = nuevodato2;      
      myPieChart6.data.datasets[0].data = nuevodato3;     
    }
    myPieChart1.update();
    myPieChart2.update();  
    myPieChart3.update();
    myPieChart4.update();
    myPieChart5.update();
    myPieChart6.update();
};

const seleccionarOpcion = document.getElementById('Sensores');
seleccionarOpcion.addEventListener('change', function () {
    const opcionSeleccionada = seleccionarOpcion.value;
    actualizarGraficos(opcionSeleccionada);
});

// Actualiza los gráficos inicialmente con la opción predeterminada
actualizarGraficos(seleccionarOpcion.value);
