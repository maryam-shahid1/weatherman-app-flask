var canvasList = document.querySelectorAll('.bar-chart');
canvasList.forEach(function(canvas) {
    var ctx = canvas.getContext('2d');
    var max_temp = canvas.getAttribute('max_temp');
    var min_temp = canvas.getAttribute('min_temp');
    var label = canvas.getAttribute('day');
    var chartWidth = 1500;
    var chartHeight = 30;

    var barLength1 = (max_temp / 100) * (chartWidth / 2);
    var barLength2 = (min_temp / 100) * (chartWidth / 2);

    ctx.fillStyle = 'red';
    ctx.fillRect(0, 0, barLength1, chartHeight);

    ctx.fillStyle = 'blue';
    ctx.fillRect(barLength1, 0, barLength2, chartHeight);

    ctx.fillStyle = 'black';
    ctx.font = '14px Arial';
    ctx.fillText('Hellllooooo', chartWidth + 10, chartHeight / 2 + 7);
});