const $Barra1 = document.querySelector("#Ef_Mediciones");
const $Barra2 = document.querySelector("#Ef_Calculos");

const Etiquetas = ["Enero", "Febrero", "Marzo"];

const Datos_CO2 = {
    label : "CO2 Medido",
    data : [300, 500, 100],
    backgroundColor: 'rgba(54, 162, 235, 0.2)',
    borderColor: 'rgba (54, 162, 235, 1)',
    borderWidth: 1,
};

const Datos_Mitigaciones = {
    label : "CO2 Mitigado",
    data : [100, 600, 700],
    backgroundColor: 'rgba(255, 159, 64, 0.2)',
    borderColor: 'rgba (255, 159, 64, 1)',
    borderWidth: 1,
};

new Chart($Barra1, {
    type: 'bar',
    data: {
        labels: Etiquetas,
        datasets: [
            Datos_CO2,
            Datos_Mitigaciones,
        ]
    },
    options: {
        title: {
            display: true,
            text: "Efectividad segun mediciones",
        },
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero:true
                }
            }],
        },
    }
});

new Chart($Barra2, {
    type: 'bar',
    data: {
        labels: Etiquetas,
        datasets: [
            Datos_CO2,
            Datos_Mitigaciones,
        ]
    },
    options: {
        title: {
            display: true,
            text: "Efectividad segun calculos",
        },
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero:true
                }
            }],
        },
    }
});