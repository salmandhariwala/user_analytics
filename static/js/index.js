// this function will initialize date picker
function init_date_picker(){

	$('input[name="inputDateRange"]').daterangepicker({
		maxDate: moment.utc().startOf('day').add(23, 'hours'),
		// minDate: moment.utc().add(-60, 'days').startOf('day'),
		startDate: startMoment,
		endDate: endMoment,
		// dateLimit: {days: 60},
		timePicker: true,
		timePickerIncrement: 60,
		format: 'YYYY/MM/DD HH:mm',
		timeZone: '00:00'
	}
	);

	var startMoment = moment().subtract(1, "days");
	var endMoment = moment();

	$('#inputDateRange').data('daterangepicker').setStartDate(startMoment);
	$('#inputDateRange').data('daterangepicker').setEndDate(endMoment);
}

// this function will return date time from date picker
function get_time() {
	//get date 
	input_date = $('#inputDateRange').val();

	var start_date = moment.utc(input_date.split(' - ')[0],'YYYY/MM/DD HH:mm').unix();
	var end_date =  moment.utc(input_date.split(' - ')[1],'YYYY/MM/DD HH:mm').unix();
	
	// console.log(start_date);
	// console.log(end_date);

	return {
		start : start_date,
		end : end_date
	}

}

var load_chart = function(){

	var start_time = get_time()["start"];
	var end_time = get_time()["end"];

	var post_body ={};
	post_body["start_time"] = start_time;
	post_body["end_time"] = end_time;
	post_body["entity"] = $("#entity option:selected").val();

	// console.log($("#entity option:selected").val());

	console.log(post_body)

	// step 3 :sample post
	$.ajax({
		type:"POST",
		url:"/test/post", 
		headers:{ "Content-Type": "application/json" },
		data:JSON.stringify(post_body),
		success:function(data){
			console.log("success of post ");
			console.log(data);
			render_chart(data)
		},
		error:function(data){
			console.log("fail * post request");
			console.log(data);
		},
		dataType: "json"
	});

}



var render_chart = function(data_graph){

	var data_to_render = [];
	var index = 0;

	console.log("data in render : ");
	console.log(data_graph)

	for (var i = 0; i < data_graph.length; i++) {
		data_to_render[i] = [data_graph[i].entity,data_graph[i].score]

	}

	console.log(data_to_render);


	$("#container").empty();


	Highcharts.chart('container', {
		chart: {
			type: 'column'
		},
		xAxis: {
			type: 'category',
			labels: {
				rotation: -45,
				style: {
					fontSize: '13px',
					fontFamily: 'Verdana, sans-serif'
				}
			}
		},
		yAxis: {
			min: 0,
			title: {
				text: 'Score'
			}
		},
		legend: {
			enabled: false
		},
		tooltip: {
			pointFormat: '<b>{point.y:.1f}</b>'
		},
		series: [{
			data: data_to_render,
			dataLabels: {
				enabled: true,
				rotation: -90,
				color: '#FFFFFF',
				align: 'right',
            format: '{point.y:.1f}', // one decimal
            y: 10, // 10 pixels down from the top
            style: {
            	fontSize: '13px',
            	fontFamily: 'Verdana, sans-serif'
            }
        }
    }]
});

}

// execution start here : main function
var main_func = function() {

	console.log("dom loaded");

	init_date_picker();

	$("#load_chart").click(load_chart)	
	

}


$(main_func);