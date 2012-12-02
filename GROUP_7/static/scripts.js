var map;
var geocoder;
var directionDisplay;
var directionsService = new google.maps.DirectionsService();
var styles;
var minZoomLevel = 10;

var strictBounds = new google.maps.LatLngBounds(
    new google.maps.LatLng(40.473069,-74.31015), 
    new google.maps.LatLng(40.922852,-73.693542)
);

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

    changeMS('aliens');
    google.maps.event.addListener(map, 'dragend', function() {
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
    });
}

function changeMS(str){
    if(str === 'zombies'){
	styles = [
	    {
		stylers: [
		    { "hue": "#ff2b00"},
		    { "saturation": -7 }
		]
	    }];
    }
    else if(str === 'aliens'){
	styles = [
	    {
		stylers: [
		    { "hue": "#08ff00"},
		    { "saturation": -52 }
		]
	    }];
    }
    else{
	styles = [];
    }
    map.setOptions({styles: styles});
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

// END GOOGLE STUFF

function changeBGC(str){
    if(str==='aliens'){
	$('body,html,#map_canvas').css('background','-webkit-linear-gradient(45deg, rgba(191,210,85,1) 0%,rgba(142,185,42,1) 85%,rgba(158,203,45,1) 100%)');
    }
    else if(str==='fire'){
	$('body,html,#map_canvas').css('background','-webkit-linear-gradient(45deg, rgba(252,234,187,1) 0%,rgba(248,181,0,1) 6%,rgba(252,205,77,1) 50%,rgba(251,223,147,1) 100%)');
    }
    else if(str==='hurricane'){
	$('body,html,#map_canvas').css('background','-webkit-linear-gradient(45deg, rgba(254,255,255,1) 0%,rgba(221,241,249,1) 35%,rgba(160,216,239,1) 100%)');
    }
    else{
	$('body,html,#map_canvas').css('background','-webkit-linear-gradient(45deg, rgba(241,111,92,1) 5%,rgba(248,80,50,1) 33%,rgba(240,47,23,1) 67%,rgba(246,41,12,1) 84%,rgba(231,56,39,1) 100%)');
    }
}