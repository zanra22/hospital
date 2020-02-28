var BarsChart = (function () {

    //
    // Variables
    //

    var $chart = $('#total-diseases');


    //
    // Methods
    //

    // Init chart
    function initChart($chart) {

        // Create chart
        var ordersChart = new Chart($chart, {
            type: 'bar',
            data: {
                labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
                datasets: [{
                    label: 'Dengue',
                    data: [20, 18, 17, 19, 23, 20, 18, 29, 10, 9, 11, 27]
                },
                {
                    label: 'HIV',
                    data: [25, 20, 30, 22, 17, 29, 25, 20, 30, 22, 17, 29]
                }]
            }
        });

        // Save to jQuery object
        $chart.data('chart', ordersChart);
    }


    // Init chart
    if ($chart.length) {
        initChart($chart);
    }

})();