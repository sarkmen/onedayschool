

function initialize() {

var myCenter = new google.maps.LatLng(37.466876, 126.948097);
var MapCenter = new google.maps.LatLng(37.473915, 126.952163);
var BusStop = new google.maps.LatLng(37.480344, 126.952496);

var image = '{% static "img/busstop.png" %}';
var mapProp = {
center:MapCenter,
zoom:14,
scrollwheel:true,
draggable:true,
mapTypeId:google.maps.MapTypeId.ROADMAP
};

var map = new google.maps.Map(document.getElementById("googleMap"),mapProp);
var marker = new google.maps.Marker({
position:myCenter,
icon : image,
});
var start = new google.maps.Marker({
position:BusStop,
icon : image,
});

marker.setMap(map);
start.setMap(map);

var lineSymbol = {
    path: google.maps.SymbolPath.CIRCLE,
    scale: 8,
    strokeColor: '#393'
  };
var line = new google.maps.Polyline({
    path: [{lat: 37.480344, lng: 126.952496},
    {lat: 37.477694, lng: 126.952273},
    {lat: 37.473318, lng: 126.953098},
    {lat: 37.471806, lng: 126.952826},
    {lat: 37.469101, lng: 126.951764},
    {lat: 37.468684, lng: 126.951528},
    {lat: 37.467620, lng: 126.949908},
    {lat: 37.467305, lng: 126.947827},
    {lat: 37.466876, lng: 126.948097}],
    icons: [{
      icon: lineSymbol,
      offset: '100%'
    }],
    strokeColor: '#a6a6a6',
    map: map
  });
animateCircle(line);
var contentString1 = '<div id="content">'+
      '<div id="siteNotice">'+
      '</div>'+
      '<h4 id="firstHeading" class="firstHeading">"서울대입구역" 버스정류장</h4>'+
      '<div id="bodyContent">'+
      '<p><b>5511, 5513, 5515번 버스</b>에 탑승하여<br> "서울대학교" 버스정류장 하차</p>'+
      '</div>'+
      '</div>';
var contentString2 = '<div id="content">'+
      '<div id="siteNotice">'+
      '</div>'+
      '<h4 id="firstHeading" class="firstHeading">"서울대학교" 버스정류장</h4>'+
      '<div id="bodyContent">'+
      '<p>"서울대학교" 버스정류장에서 하차 후<br> 서울대학교 정문으로 걸어서 이동</p>'+
      '</div>'+
      '</div>';
var infowindow1 = new google.maps.InfoWindow({
    content: contentString1
  });
var infowindow2 = new google.maps.InfoWindow({
    content: contentString2
  });
start.addListener('click', function() {
    infowindow1.open(map, start);
  });
marker.addListener('click', function() {
    infowindow2.open(map, marker);
  });
var lineSymbol_2 = {
    path: 'M 0,-1 0,1',
    strokeOpacity: 1,
    strokeColor: '#a6a6a6',
    scale: 4
  };

  // Create the polyline, passing the symbol in the 'icons' property.
  // Give the line an opacity of 0.
  // Repeat the symbol at intervals of 20 pixels to create the dashed effect.
  var line_2 = new google.maps.Polyline({
    path: [{lat: 37.480926, lng: 126.952422},
    {lat: 37.480344, lng: 126.952496}],
    strokeOpacity: 0,
    icons: [{
      icon: lineSymbol_2,
      offset: '0',
      repeat: '20px'
    }],
    map: map
  });
  var line_3 = new google.maps.Polyline({
    path: [{lat: 37.466876, lng: 126.948097},
    {lat: 37.466649, lng: 126.948342}],
    strokeOpacity: 0,
    icons: [{
      icon: lineSymbol_2,
      offset: '0',
      repeat: '20px'
    }],
    map: map
  });
}
function animateCircle(line) {
    var count = 0;
    window.setInterval(function() {
      count = (count + 1) % 400;

      var icons = line.get('icons');
      icons[0].offset = (count / 4) + '%';
      line.set('icons', icons);
  }, 20);
}
google.maps.event.addDomListener(window, 'load', initialize);

