$(document).ready(function(){initialize();});
var datamarkerlist= new Array();

function DataMarker(message, latlng, timestamp) {
	 this.message = message;
	 this.latlng = latlng;
	 this.timestamp = timestamp;
	 this.marker = new google.maps.Marker({ position : this.latlng,
						map : map,
						title : message + " at " + timestamp,
						icon : "/media/images/pink_MarkerO.png"
					     });	
	DataMarker.averageAge = null;
 	datamarkerlist.push(this);


}

function initialize() {

	var mapOptions = {
		zoom : 2,
		mapTypeId : google.maps.MapTypeId.TERRAIN,
		center :  new google.maps.LatLng(0.0,0.0)
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
		datamarker = new DataMarker("Hello there!" , new google.maps.LatLng(0, i* 20, false), "thetime");
	  
	  // new google.maps.Marker({position: new google.maps.LatLng(0, i*50, false), map : map, title : title, icon : markerImage});
	    //addMarker(someTmarker);
	}
        
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
