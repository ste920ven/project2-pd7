var map;
var geocoder;
var directionDisplay;
var directionsService = new google.maps.DirectionsService();
var styles;
var minZoomLevel = 10;
var maxZoomLevel = 19;
var strictBounds = new google.maps.LatLngBounds(
    new google.maps.LatLng(40.473069,-74.31015), 
    new google.maps.LatLng(40.922852,-73.693542)
);

//W3C Geolocation
if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(successFunction, errorFunction);
} else {
    alert('It seems like Geolocation, which is required for this page, is not enabled in your browser. Please use a browser which supports it.');
}

function successFunction(position) {
    var lat = position.coords.latitude;
    var long = position.coords.longitude;
    alert('Your latitude is :'+lat+' and longitude is '+long);
}

function errorFunction(position) {
    alert('Error!');
}
//END GEOLOCATION

//GOOGLE API
function initialize() {
    var browser = BrowserDetect.browser;
    var bversion = BrowserDetect.version;
    if(browser != 'Chrome' && browser != 'Safari'){
	alert('Please use Google Chrome or Safari');
    }
    else{
	if(browser = 'Chrome'){
	    if(bversion < 10){
		var str = "Please update Chrome to 10 or higher for best results\nYour current version is "+bversion;
		alert(str);
	    }
	}
	if(browser = 'Safari'){
	    if(bversion < 5.1){
		var str = "Please update Safair to 5.1 or higher for best resulsts\nYour current version is "+bversion;
	    }
	}
    }
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
	if(map.zoom > maxZoomLevel) map.setZoom(maxZoomLevel);
    });
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
    
    var input = document.getElementById('target');
    var searchBox = new google.maps.places.SearchBox(input);
    var markers = [];
    
    google.maps.event.addListener(searchBox, 'places_changed', function() {
        var places = searchBox.getPlaces();
        for (var i = 0, marker; marker = markers[i]; i++) {
           marker.setMap(null);
        }
	
        markers = [];
        var bounds = new google.maps.LatLngBounds();
        for (var i = 0, place; place = places[i]; i++) {
            var image = new google.maps.MarkerImage(
                place.icon, new google.maps.Size(71, 71),
                new google.maps.Point(0, 0), new google.maps.Point(17, 34),
                new google.maps.Size(25, 25));
	    
            var marker = new google.maps.Marker({
		map: map,
		icon: image,
		title: place.name,
		position: place.geometry.location
            });
	    
            markers.push(marker);
	    
            bounds.extend(place.geometry.location);
        }
	
        map.fitBounds(bounds);
    });
    
    google.maps.event.addListener(map, 'bounds_changed', function() {
        var bounds = map.getBounds();
        searchBox.setBounds(bounds);
    });
    
    google.maps.event.addListener(map, 'bounds_changed', function() {
        var bounds = map.getBounds();
        searchBox.setBounds(bounds);
    });
    //var trafficLayer = new google.maps.TrafficLayer();
    //trafficLayer.setMap(map);
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

var BrowserDetect = {
    init: function () {
	this.browser = this.searchString(this.dataBrowser) || "An unknown browser";
	this.version = this.searchVersion(navigator.userAgent)
	    || this.searchVersion(navigator.appVersion)
	    || "an unknown version";
	this.OS = this.searchString(this.dataOS) || "an unknown OS";
    },
    searchString: function (data) {
	for (var i=0;i<data.length;i++)	{
	    var dataString = data[i].string;
	    var dataProp = data[i].prop;
	    this.versionSearchString = data[i].versionSearch || data[i].identity;
	    if (dataString) {
		if (dataString.indexOf(data[i].subString) != -1)
		    return data[i].identity;
	    }
	    else if (dataProp)
		return data[i].identity;
	}
    },
    searchVersion: function (dataString) {
	var index = dataString.indexOf(this.versionSearchString);
	if (index == -1) return;
	return parseFloat(dataString.substring(index+this.versionSearchString.length+1));
    },
    dataBrowser: [
	{
	    string: navigator.userAgent,
	    subString: "Chrome",
	    identity: "Chrome"
	},
	{ 	string: navigator.userAgent,
		subString: "OmniWeb",
		versionSearch: "OmniWeb/",
		identity: "OmniWeb"
	},
	{
	    string: navigator.vendor,
	    subString: "Apple",
	    identity: "Safari",
	    versionSearch: "Version"
	},
	{
	    prop: window.opera,
	    identity: "Opera",
	    versionSearch: "Version"
	},
	{
	    string: navigator.vendor,
	    subString: "iCab",
	    identity: "iCab"
	},
	{
	    string: navigator.vendor,
	    subString: "KDE",
	    identity: "Konqueror"
	},
	{
	    string: navigator.userAgent,
	    subString: "Firefox",
	    identity: "Firefox"
	},
	{
	    string: navigator.vendor,
	    subString: "Camino",
	    identity: "Camino"
	},
	{		// for newer Netscapes (6+)
	    string: navigator.userAgent,
	    subString: "Netscape",
	    identity: "Netscape"
	},
	{
	    string: navigator.userAgent,
	    subString: "MSIE",
	    identity: "Explorer",
	    versionSearch: "MSIE"
	},
	{
	    string: navigator.userAgent,
	    subString: "Gecko",
	    identity: "Mozilla",
	    versionSearch: "rv"
	},
	{ 		// for older Netscapes (4-)
	    string: navigator.userAgent,
	    subString: "Mozilla",
	    identity: "Netscape",
	    versionSearch: "Mozilla"
	}
    ],
    dataOS : [
	{
	    string: navigator.platform,
	    subString: "Win",
	    identity: "Windows"
	},
	{
			string: navigator.platform,
	    subString: "Mac",
	    identity: "Mac"
	},
	{
	    string: navigator.userAgent,
	    subString: "iPhone",
	    identity: "iPhone/iPod"
	},
	{
	    string: navigator.platform,
	    subString: "Linux",
	    identity: "Linux"
	}
    ]
    
};
BrowserDetect.init();

function changeBGC(str){
    if(str==='aliens'){
	$('body,html,#map_canvas').css('background','-webkit-linear-gradient(-45deg, #aebcbf 0%,#6e7774 50%,#0a0e0a 51%,#0a0809 100%)');
    }
    else if(str==='fire'){
	$('body,html,#map_canvas').css('background','-webkit-linear-gradient(-45deg, #fceabb 0%,#fccd4d 50%,#f8b500 51%,#fbdf93 100%)');
    }
    else if(str==='hurricane'){
	$('body,html,#map_canvas').css('background','-webkit-linear-gradient(-45deg, #6db3f2 0%,#54a3ee 50%,#3690f0 51%,#1e69de 100%)');
    }
    else{
	$('body,html,#map_canvas').css('background','-webkit-linear-gradient(-45deg, #bfd255 0%,#8eb92a 50%,#72aa00 51%,#9ecb2d 100%)');
    }
}