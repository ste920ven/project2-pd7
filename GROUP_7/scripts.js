var map;
var geocoder;
var directionDisplay;
var directionsService = new google.maps.DirectionsService();

var minZoomLevel = 10;

//commented out lines limit map panning to nyc; but interferes with geocode and directions if locations out of nyc
//var strictBounds = new google.maps.LatLngBounds(
//    new google.maps.LatLng(40.473069,-74.31015), 
//    new google.maps.LatLng(40.922852,-73.693542)
//);

function initialize() {
    geocoder = new google.maps.Geocoder();
    directionsDisplay = new google.maps.DirectionsRenderer();
    var latlng = new google.maps.LatLng(40.720461,-74.013519);
    var mapOptions = {
	zoom: minZoomLevel,
	center: new google.maps.LatLng(40.720461,-74.013519),
	mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    map = new google.maps.Map(document.getElementById('map_canvas'),
			      mapOptions);
    directionsDisplay.setMap(map);

    google.maps.event.addListener(map, 'zoom_changed', function() {
	if(map.zoom < minZoomLevel) map.setZoom(minZoomLevel);
    });

 /*   google.maps.event.addListener(map, 'dragend', function() {
	if (strictBounds.contains(map.getCenter())) return;
	var c = map.getCenter(),
        x = c.lng(),
        y = c.lat(),
        maxX = strictBounds.getNorthEast().lng(),
        maxY = strictBounds.getNorthEast().lat(),
        minX = strictBounds.getSouthWest().lng(),
        minY = strictBounds.getSouthWest().lat();
	
	if (x < minX) x = minX;
	if (x > maxX) x = maxX;
	if (y < minY) y = minY;
	if (y > maxY) y = maxY;
	
	map.setCenter(new google.maps.LatLng(y, x));
    });*/
}

function codeAddress() {
    var address = document.getElementById('address').value;
    geocoder.geocode( { 'address': address}, function(results, status) {
        if (status == google.maps.GeocoderStatus.OK) {
            map.setCenter(results[0].geometry.location);
            var marker = new google.maps.Marker({
                map: map,
                position: results[0].geometry.location
            });
        } else {
            alert('Geocode was not successful for the following reason: ' + status);
        }
    });
}

function calcRoute() {
    var start = document.getElementById('start').value;
    var end = document.getElementById('end').value;
    var selectedMode = document.getElementById('mode').value;
    var request = {
        origin:start,
        destination:end,
        travelMode: google.maps.TravelMode[selectedMode]
    };
    directionsService.route(request, function(response, status) {
        if (status == google.maps.DirectionsStatus.OK) {
            directionsDisplay.setDirections(response);
        }
    });
}

