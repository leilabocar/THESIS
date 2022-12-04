var map;
var latlong;
var marker;
$(function() {
	initMap();
	getMapLatLong();
    enterLatLng();

});
function initMap(){
	map = new google.maps.Map(document.getElementById("mapAdmin"), {
		center: { lat: 14.3642225, lng: 120.9093891 },
		zoom: 18.5,
		zoomControl: false,
		gestureHandling: "none",
		mapTypeId: "terrain",
	});
	
}
  function setMarker(latitude,longitude){
    if(marker != null || marker != undefined){
        marker.setMap(null);
        marker = new google.maps.Marker({
            animation: google.maps.Animation.DROP,
            map: map,
            position: new google.maps.LatLng(latitude,longitude)
        });
        marker.setMap(map);
    }else{
        marker = new google.maps.Marker({
            animation: google.maps.Animation.DROP,
            map: map,
            position: new google.maps.LatLng(latitude,longitude)
        });
        marker.setMap(map);
    }
  }
  var lat;
  var long;
  function getMapLatLong(){
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
		$('input#lat').val(lat);
		$('input#lng').val(long);
	});
}
function getLatLongBoolean(){
    var lat = $('input#lat').val().length;
    var lng = $('input#lng').val().length;
    if(lat != 0 && lng != 0){
        return true;
    }else{
        return false
    }
}

function enterLatLng(){
    $('input#lat').keypress(function(e){
        if(getLatLongBoolean()){
            setTimeout(() => {
                setMarker($('input#lat').val(),$('input#lng').val());
            }, "2000")
        }
    });
    $('input#lng').keypress(function(e){
        if(e.keyCode == 13)
        {
            if(getLatLongBoolean()){
                setTimeout(() => {
                    setMarker($('input#lat').val(),$('input#lng').val());
                }, "2000")
            }
        }
    });
    
}