
document.addEventListener("DOMContentLoaded", function() {
    const ctx = document.getElementById('sectoresChart').getContext('2d');
    const sectoresChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: window.chartLabels,  // Usamos las variables globales
            datasets: [{
                label: '',
                data: window.chartData,  // Usamos las variables globales
                backgroundColor: [
                        'rgba(34,19,89,0.7)',
                        'rgb(0, 212, 96, 0.7)',
                        'rgba(11, 72, 129, 0.7)',
                        'rgba(102, 193, 234, 0.7)',
                    ],
                borderWidth: 1
            }]
        },
        options: {
            plugins: {
                legend: {
                    display: false,
                }
            },
            responsive: true,
            scales: {
                y: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Personas Inscritas'
                    }
                },

            }
        }
    });
});

// static/tu_app/chart.js
document.addEventListener('DOMContentLoaded', function () {
    const ctx = document.getElementById('myPieChart').getContext('2d');
    const myPieChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['Favoritos', 'Aspirantes'],
            datasets: [{
                label: 'Número',
                data: [chartData.num_favoritos, chartData.num_aspirantes],
                backgroundColor: [
                    'rgb(0, 212, 96, 0.7)',
                    'rgb(34,19,89,0.7)',
                ],
                hoverOffset: 4

            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    display: true,
                    position: 'top',
                },
            }
        }
    });
});

document.addEventListener("DOMContentLoaded", function() {
    const ctx = document.getElementById('salarioChart').getContext('2d');
    const salarioChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: chartData_salario.sectores,
            datasets: [{
                data: chartData_salario.salarios,
                backgroundColor: [
                        'rgba(34,19,89,0.7)',
                        'rgb(0, 212, 96, 0.7)',
                        'rgba(11, 72, 129, 0.7)',
                        'rgba(102, 193, 234, 0.7)',
                    ],
                borderWidth: 1
            }]
        },
        options: {
            plugins: {
                legend: {
                    display: false,
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'Salario Promedio (COP)'
                    }
                },

            }
        }
    });
});

document.addEventListener("DOMContentLoaded", function() {
    const ctx = document.getElementById('grafico_modalidades').getContext('2d');
    const grafico_modalidades = new Chart(ctx, {
        type: 'doughnut',  // Tipo de gráfico
        data: {
            labels: chartData_modalidades.modalidades,
            datasets: [{
                label: 'Modalidades preferidas',
                data: chartData_modalidades.valores,
                backgroundColor: [
                        'rgba(34,19,89,0.7)',
                        'rgb(0, 212, 96, 0.7)',
                        'rgba(11, 72, 129, 0.7)',
                        'rgba(102, 193, 234, 0.7)',
                    ],
                hoverOffset: 4
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    display: true,
                    position: 'top',
                },
            }
        }
    });
});


