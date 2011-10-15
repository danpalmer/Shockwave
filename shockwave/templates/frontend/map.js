var tweetmarkerlist= new Array();

function Tweetmarker =  function(message, latlng, timestamp) {
	 this.message = message;
	 this.latlng = latlng;
	 this.timestamp = timestamp;


}

function initialize() {

	var mapOptions = {
		zoom : 4,
		mapTypeId : google.maps.MapTypeId. HYBRID
	};
	var map = new google.maps.Map(document.getElementById("map"), mapOptions);
	for(i=0; i < 5; i++) {
	     var someTmarker = now TweetMarker("Yo",LatLng(i*37, 0,false), "someTime");	
	     addMarker(someTmarker);
	}
        
}

function addMarker(tweetmarker) {

	marker = new google.maps.Marker({position: tweetmarker.pos,
					 map : map,
					 title: tweetmarker.message
					});
	tweetmarker.marker = marker;	

}
