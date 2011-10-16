$(document).ready(function(){initialize();});
var datamarkerlist= new Array();

function DataMarker(message, latlng, timestamp) {
	 this.latlng = latlng;
	 this.timestamp = timestamp;
	 this.marker = new google.maps.Marker({ position : this.latlng,
						map : map,
						title : content + " at " + timestamp,
						icon : "/media/images/pink_MarkerO.png",
						animation : google.maps.Animation.DROP
					     });	
	 this.content = message;
	 this.infoWindow = new google.maps.InfoWindow({ 
			
		//content : "From " + this.latlng + " " + this.content + "at " + timestamp
		content : '<div style="clear : both; margin: 5px 10px 10px 10px">' + this.content + ' </div> <div style="float:left; font-size: 10px">' + this.latlng + '</div> <div style="float: right; font-size: 10px" >' + formatDateNicely(this.timestamp) + '</div>'

	});

	addMarkerListener(this);
		
	
	DataMarker.averageAge = null;
 	datamarkerlist.push(this);



}

function formatDateNicely(unixtime) {
	var date = new Date(unixtime*1000);
	var currentTime = Date.UTC();
	
	if(morethanaday(unixtime, currentTime / 1000)) {
		if(morethanaweek(unixtime / 1000, currentTime/1000)) {
			return date.getDate() + "/" + date.getMonth() + "/" +  date.getYear();
		} else {
			return date.getDay() + " " + date.getHours() + ":" + date.getMinutes();
		}
		
		return date.getHours() + ":" + date.getMinutes();
	}

}

function morethanaweek(currentunixtime, tweetunixtime) {
	if((currentunixtime - tweetunixtime) > 7*60*60*24) {
		return true;
	} else {
 		return false;
	}
}

function morethanaday(currentunixtime, tweetunixtime) {
	if((currentunixtime - tweetunixtime) > 60*60*24) {
		return true;
	} else {
 		return false;
	}
}

function addMarkerListener(datamarker) {

	google.maps.event.addListener(datamarker.marker, 'click', function() {

		datamarker.infoWindow.open(map, datamarker.marker);
		
	});

}

function initialize() {

	$.get('/sample', function (data) {	
		tweetarray = $.parseJSON(data);
		for( var b=0; b < tweetarray.length; b++) {
			var tweet = tweetarray[b];
			var datamarker = new DataMarker(tweet.content, new google.maps.LatLng(tweet.latitude, tweet.longitude), tweet.time);
		}
		
		reset_slider();
	});
	
	$("#searchform").submit(function() {	
		var searchterm = $('#search').val();
		search(searchterm);
		//e.preventDefault();
		return false;
	});
	var mapOptions = {
		zoom : 2,
		mapTypeId : google.maps.MapTypeId.TERRAIN,
		center :  new google.maps.LatLng(0.0,0.0),
		disableDefaultUI : true,
		zoomControl : true,
		panControl : true
	};
	
	map = new google.maps.Map(document.getElementById("map"), mapOptions);
		
	var center = map.getCenter();
    
    initialize_slider();
}

function search(searchText) {
	$("#titlebar_left").html(searchText);
	
	return false;
}

/*
function addMarker(tweetmarker) {

	marker = new google.maps.Marker({position: tweetmarker.pos,
					 map : map,
					 title: tweetmarker.message
					});
	data.marker = marker;	
	tweetmarkerlist.push(tweetmarker);

}
*/
function updateView() {

	for( var b = 0; b < tweetmarkerlist.length; b++) {
		tweetmarker[b].timestamp;
	}
}

/*
	Slider stuff
*/
	
function initialize_slider() {
	$("#date_display_box").hide();
	$("#slider").slider({
		animate: true,
     	range: "min",
		value: 0,
		min: 0,
		max: 1,
		step: 1,

		start: function(event, ui) {
			$("#date_display_box").fadeIn('fast');
			$("#date_display").html(" ");
		},
		
		stop: function(event, ui) {
			$("#date_display_box").fadeOut('fast');
			$("#date_display").html(" ");
		},
		
		//this gets a live reading of the value and prints it on the page
		slide: function(event, ui) {
			$("#date_display").html(ui.value + parseInt(current_min_timestamp));
			$.each(datamarkerlist, function(index, value) {
				if (value.timestamp <= ui.value + parseInt(current_min_timestamp)) {
					value.marker.setVisible(true)
				} else {
					value.marker.setVisible(false);
				}
			});
		},

		//this updates the hidden form field so we can submit the data using a form
		change: function(event, ui) {
			$.each(datamarkerlist, function(index, value) {
				if (value.timestamp <= ui.value + parseInt(current_min_timestamp)) {
					value.marker.setVisible(true)
				} else {
					value.marker.setVisible(false);
				}
			});
		}
	});
	
	reset_slider();
}

var current_min_timestamp = 1;

function reset_slider() {
	current_min_timestamp = getMinTimestamp();
	var max_timestamp = getMaxTimestamp() - current_min_timestamp;
	var min_timestamp = 0;
	$("#slider").slider("option", "min", min_timestamp);
	$("#slider").slider("option", "max", max_timestamp);
	$("#slider").slider("option", "value", max_timestamp);
}

function getMinTimestamp() {
	if (datamarkerlist.length > 0) {
		return datamarkerlist.reduce(function(a, b) {if(a.timestamp < b.timestamp) return a; return b;}).timestamp;
	}
	return 0;
}

function getMaxTimestamp() {
	if (datamarkerlist.length > 0) {
		return datamarkerlist.reduce(function(a, b) {if(a.timestamp > b.timestamp) return a; return b;}).timestamp;
	}
	return 1;
}

/*
	Replay Data
*/
var PLAY_LENGTH_DEFAULT = 30;
var play_length = 0;
var current_time = 0;
var date_increase_amount = 1;

function play() {
	clearInterval("next_play_stage()");
	current_time = 0;
	
	if (datamarkerlist.length < PLAY_LENGTH_DEFAULT) {
		play_length = datamarkerlist.length
	} else {
		play_length = PLAY_LENGTH_DEFAULT;
	}
	
	var max_timestamp = getMaxTimestamp();
	var min_timestamp = getMinTimestamp();	
	var difference = max_timestamp - min_timestamp;
	date_increase_amount = difference / play_length;
	
	setInterval("next_play_stage()", 1000);
}

function next_play_stage() {
	if (current_time > play_length) {
		clearInterval("next_play_stage()");
		return;
	}
	$('title').html(Math.floor(current_time * date_increase_amount));
	$("#slider").slider("option", "value", Math.floor(current_time * date_increase_amount));
	current_time += 1;
}