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

function getMoreData(searchterm) {


}

function initialize() {

	$.get('/sample', function (data) {
	//	alert(data);	
		tweetarray = $.parseJSON(data);
		for( var b=0; b < tweetarray.length; b++) {
			var tweet = tweetarray[b];
			var datamarker = new DataMarker(tweet.content, new google.maps.LatLng(tweet.latitude, tweet.longitude), tweet.time);
		}
	//	alert(tweetarray.length);
	});
	
$("#searchform").submit(function() {	
		var searchterm = $('#search').val();
		getMoreData(searchterm);
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
	for(i=0; i < 5; i++) {
	  //  var someTmarker = new TweetMarker("Yo",new google.maps.LatLng(i*37, 0,false), "someTime");	
	   imageSize = new google.maps.Size({height : 34,
					width : 20
				 	});
	   markerImage = new google.maps.MarkerImage("media/images/pink_MarkerO.png");
	   title = "Yo";
		// Latlng cannot accept lat values more than 90 or less than -90
	   datamarker = new DataMarker("Hello there!" , new google.maps.LatLng(0, i* 20, false), 1318717240 - 10000);
		
	  
	  // new google.maps.Marker({position: new google.maps.LatLng(0, i*50, false), map : map, title : title, icon : markerImage});
	    //addMarker(someTmarker);
	}
	//	addMarkerListener(datamarkerlist[0]);
	//alert(datamarkerlist.length);
        
}

function search(searchText) {

	//alert(searchText);
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
