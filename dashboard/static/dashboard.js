/* globals Chart:false, feather:false */

(() => {
  'use strict'

  feather.replace({ 'aria-hidden': 'true' })

  

  // Graphs
  const ctx = document.getElementById('myChart')
  // eslint-disable-next-line no-unused-vars
  const myChart = new Chart(ctx, {
    type: 'bar',
    data: {
      labels: dt2,
      datasets: [{
        data: dt,
        lineTension: 0,
        backgroundColor: 'white',
        borderColor: '#007bff',
        borderWidth: 4,
        pointBackgroundColor: 'rgba(0,0,0,0.1)'
      }]
    },
    options: {
      plugins: {
        legend: {
          display: true
        },
        tooltip: {
          boxPadding: 3
        }
      }
    }
  })
})()
