$.ajax({
  url: '/json_estadisticas/',
  dataType: 'json',
  success: function(estadisticas){
    var ctx = document.getElementById("myChart");
    var ctx = document.getElementById("myChart").getContext("2d");
    var ctx = $('#myChart');
    var ctx = 'myChart';
    var miChart = new Chart(ctx,{
      type:"bar",
      data:{
        labels: [estadisticas[0][0],estadisticas[0][1],estadisticas[0][2],
                estadisticas[0][3],estadisticas[0][4],estadisticas[0][5],
                 estadisticas[0][7],estadisticas[0][8],estadisticas[0][6],
                 estadisticas[0][9]],
        datasets:[{
          label: '# de prestamos',
          data: [estadisticas[1][0],estadisticas[1][1],estadisticas[1][2],
                 estadisticas[1][3],estadisticas[1][4],estadisticas[1][5],
                 estadisticas[1][7],estadisticas[1][8],estadisticas[1][6],
                 estadisticas[1][9]],
          backgroundColor: ['rgba(255, 5, 5, 0.5)','rgba(22, 61, 252, 0.5)',
          'rgba(22, 252, 110, 0.5)','rgba(22, 221, 252, 0.5)','rgba(252, 248, 22, 0.5)',
          'rgba(53, 252, 22, 0.5)','rgba(0,0,0,0.5)','rgba(250, 25, 118, 0.5)',
          'rgba(239, 25, 250, 0.5)','rgba(250, 126, 25, 0.5)'],
          borderColor: ['rgba(255, 5, 5, 1)','rgba(22, 61, 252, 1)',
          'rgba(22, 252, 110, 1)','rgba(22, 221, 252, 1)','rgba(252, 248, 22, 1)',
          'rgba(53, 252, 22, 1)','rgba(0,0,0,1)','rgba(250, 25, 118, 1)',
          'rgba(239, 25, 250, 1)','rgba(250, 126, 25, 1)'],
          borderWidth: 1
        }]
      },
      options:{
        legend:{
          display: false
        },
        scales:{
          yAxes:[{
            ticks:{
              beginAtZero: true,
              stepSize: 1
            }
          }]
        }
      }
    })
  }
})
