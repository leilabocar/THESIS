var map;
var latlong;
var directionsRenderer = new google.maps.DirectionsRenderer();
var directionsService = new google.maps.DirectionsService();
var marker;
var markers =  [];
var marker1 = [];
var infoStart =[];
var infoEnd = [];
var step = [];
$(function() {
	// clickTd();
	initMap();
	// getMapLatLong();
});
function initMap(){
	map = new google.maps.Map(document.getElementById("map"), {
		center: { lat: 14.3642225, lng: 120.9093891 },
		zoom: 18.5,
		zoomControl: true,
		// gestureHandling: "none",
		disableDoubleClickZoom: true,
		mapTypeId: "terrain",
		provideRouteAlternatives: false,
		draggableCursor:"default"

	});
}

function clickViewButton(lat,long){
	// $("tr#trclick").on('click',function(e){
		
	// });
	// e.stopPropagation();
	removeMarkersAndLines();
	// himlayan of general trias gate coordinates = 14.3638833,120.9090871
	// var latlong = $(this).closest("tr").find(".latlong").text();
	// var seperateLatLong = latlong.split(",");
	// var lat= seperateLatLong[0];
	// var long = seperateLatLong[1];
	var m1 = new google.maps.Marker({
		map: map,
		title: "start",
		position: new google.maps.LatLng(14.3636834,120.9092979)
	  });
	var m2 = new google.maps.Marker({
		map: map,
		title: "end",
		position: new google.maps.LatLng(lat,long)
	  });
	var startInfo= "You are here";
	var endInfo= "Here is the Destination";
	var info1 = new google.maps.InfoWindow({
		content: startInfo,
		ariaLabel: "Uluru",
	})
	var info2 = new google.maps.InfoWindow({
		content: endInfo,
		ariaLabel: "Uluru",
	})
	infoStart.push(info1);
	infoEnd.push(info2);
	markers.push(m2);
	marker1.push(m1);
	info1.open({
		anchor: m1,
		map,
	  });
	info2.open({
		anchor: m2,
		map,
	});
	calcRoute(new google.maps.LatLng(14.3636834,120.9092979),new google.maps.LatLng(lat,long));
}
function setMapOnAll(map) {
	for (let i = 0; i < marker.length; i++) {
		marker[i].setMap(map);
	}
  }
var extra1 = [];
var extra2 = [];
function calcRoute(start,end) {
	// var start = new google.maps.LatLng(14.3636834,120.9092979); // start of himlayan gate
	// var end = new google.maps.LatLng(lat,long); // destination for lot
	directionsService.route({
		origin: start,
		destination: end,
		travelMode: google.maps.TravelMode.WALKING
	  }, function(response, status) {
		if (status === google.maps.DirectionsStatus.OK) {
		  // directionsDisplay.setDirections(response);
		  renderDirectionsPolylines(response, start, end);
		} else {
		  window.alert('Directions request failed due to ' + status);
		}
	  });
  }
  var polylineOptions = {
	strokeColor: '#FFC300',
	strokeOpacity: 1,
	strokeWeight: 4
  };
  var walkingPolylineOptions = {
	strokeColor: '#FFC300',
	strokeOpacity: 0,
	strokeWeight: 4,
	icons: [{
	  icon: {
		path: google.maps.SymbolPath.CIRCLE,
		fillColor: '#FFC300',
		fillOpacity: 1,
		scale: 2,
		strokeColor: '#FFC300',
		strokeOpacity: 1,
	  },
	  offset: '0',
	  repeat: '10px'
	}]
  };
  var walkingPolylineOptions2 = {
	strokeColor: '#FFC300',
	strokeOpacity: 0,
	strokeWeight: 4,
	icons: [{
	  icon: {
		path: google.maps.SymbolPath.CIRCLE,
		fillColor: '#FFC300',
		fillOpacity: 1,
		scale: 2,
		strokeColor: '#FFC300',
		strokeOpacity: 1,
	  },
	  offset: '0',
	  repeat: '10px'
	}]
  };
  var extraLine1;
  var extraLine2;
  var stepPolyline;
  var bounds;
  var extra1 = [];
  var extra2 = [];
  function renderDirectionsPolylines(response, start, end) {
	if(stepPolyline !=null || stepPolyline !=undefined){
		stepPolyline.setMap(null);
	}
	var legs = response.routes[0].legs;
	if(bounds != null || bounds != undefined){
		bounds = null;
	}
	bounds = new google.maps.LatLngBounds();
	for (i = 0; i < legs.length; i++) {
	  var steps = legs[i].steps;
	  for (j = 0; j < steps.length; j++) {
		var nextSegment = steps[j].path;
		stepPolyline = new google.maps.Polyline(polylineOptions);
		if (steps[j].travel_mode == google.maps.TravelMode.WALKING) {
		  stepPolyline.setOptions(walkingPolylineOptions)
		}
		for (k = 0; k < nextSegment.length; k++) {
		  stepPolyline.getPath().push(nextSegment[k]);
		  bounds.extend(nextSegment[k]);
		}
		step.push(stepPolyline);
		stepPolyline.setMap(map);
	  }
	}
	if (google.maps.geometry.spherical.computeDistanceBetween(start, stepPolyline.getPath().getAt(0)) > 1) {
	  // add "dotted line"
			extraLine1 = new google.maps.Polyline(walkingPolylineOptions2);
			extra1.push(extraLine1);
			extraLine1.setPath([stepPolyline.getPath().getAt(stepPolyline.getPath().getLength() - 1), end]);
			extraLine1.setMap(map);
	}
	if (google.maps.geometry.spherical.computeDistanceBetween(end, stepPolyline.getPath().getAt(stepPolyline.getPath().getLength() - 1)) > 1) {
	  // add "dotted line"
			extraLine2 = new google.maps.Polyline(walkingPolylineOptions2);
			extra2.push(extraLine2);
			extraLine2.setPath([stepPolyline.getPath().getAt(stepPolyline.getPath().getLength() - 1), end]);
			extraLine2.setMap(map);
	}
	map.fitBounds(bounds);
  }
  	function removeMarkersAndLines()
	{
		m1 = [];
		m2 = [];
		if(markers.length != 0 || markers != null || markers != undefined || markers != []){
			for(var i=0; i < markers.length; i++){
				markers[i].setMap(null);
			}
			
		}
		if(marker1.length != 0 || marker1 != null || marker1 != undefined || marker1 != []){
			for(var i=0; i < marker1.length; i++){
				marker1[i].setMap(null);
			}
				
		}
		if(extra1.length != 0 || extra1 != null || extra1 != undefined || extra1 != []){
			for(var i=0; i < extra1.length; i++){
				extra1[i].setMap(null);
			}
				
		}
		if(extra2.length != 0 || extra2 != null || extra2 != undefined || extra2 != []){
			for(var i=0; i < extra2.length; i++){
				extra2[i].setMap(null);
			}
				
		}
		if(step.length != 0 || step != null || step != undefined || step != []){
			for(var i=0; i < step.length; i++){
				step[i].setMap(null);
			}
				
		}
		if(infoStart.length != 0 || infoStart != null || infoStart != undefined || steinfoStartp != []){
			for(var i=0; i < infoStart.length; i++){
				infoStart[i].setMap(null);
			}
				
		}
		if(infoEnd.length != 0 || infoEnd != null || infoEnd != undefined || infoEnd != []){
			for(var i=0; i < infoEnd.length; i++){
				infoEnd[i].setMap(null);
			}
				
		}
	}	

  function getMapLatLong(){
	$("#lat").prop("readonly", true);
	$("#lng").prop("readonly", true);
	var lat;
	var long;
	google.maps.event.addListener(map, 'click', function(event) {
		if(marker != null || marker != undefined){
			marker.setMap(null);
			marker = new google.maps.Marker({
				animation: google.maps.Animation.DROP,
				map: map,
				position: event.latLng
			});
			marker.setMap(map);
			lat = event.latLng.lat();
			long = event.latLng.lng();
		}else{
			marker = new google.maps.Marker({
				animation: google.maps.Animation.DROP,
				map: map,
				position: event.latLng
			});
			marker.setMap(map);
			lat = event.latLng.lat();
			long = event.latLng.lng();
		}
		console.log(lat,long);
		$('input#lat').val(lat);
		$('input#lng').val(long);
	});
	
	
  }