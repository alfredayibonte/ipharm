function initialize()
{
	var mapProp = {
		center:new google.maps.LatLng(5.508742,0.256350),
		zoom:10,
		mapTypeId:google.maps.MapTypeId.ROADMAP
	};
	var map=new google.maps.Map(document.getElementById("googleMap")
		,mapProp);
}

google.maps.event.addDomListener(window, 'load', initialize);