var redCanvasList = document.querySelectorAll('.red-bar-chart');
redCanvasList.forEach(function(canvas) {
        var ctx = canvas.getContext('2d');
        var max_temp = canvas.getAttribute('max_temp');
        var chartWidth = 1500;
        var chartHeight = 30;

        var barLength = (max_temp / 100) * chartWidth;

        ctx.fillStyle = 'red';
        ctx.fillRect(0, 0, barLength, chartHeight);

        ctx.fillStyle = 'red';
        ctx.font = '14px Arial';
        ctx.fillText(max_temp+'°C', barLength + 5, chartHeight / 2 + 7);
    });

var blueCanvasList = document.querySelectorAll('.blue-bar-chart');
blueCanvasList.forEach(function(canvas) {
        var ctx = canvas.getContext('2d');
        var min_temp = canvas.getAttribute('min_temp');
        var chartWidth = 1500;
        var chartHeight = 30;

        var barLength = (min_temp / 100) * chartWidth;

        ctx.fillStyle = 'blue';
        ctx.fillRect(0, 0, barLength, chartHeight);

        ctx.fillStyle = 'blue';
        ctx.font = '14px Arial';
        ctx.fillText(min_temp+'°C', barLength + 5, chartHeight / 2 + 7);
    });