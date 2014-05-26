$(document).ready(init);
var lng;
var lat;
function init(){
$("#line").hide();
    $("#drugs").autocomplete({
    source: "/api/get_drugs/",
    minLength: 2
  });


    //search ajax
    $("#search").keyup(function(){
        var search = $(this).val();
        var token = $("input[name='csrfmiddlewaretoken']").val();
        var data = {
            'search':search,
            'csrfmiddlewaretoken':token
        };
        $("#first_heading").hide();

        $("#find").css(
            {top:"-50px", height:"100%", marginTop:"-16%", marginLeft:'-8.5%'}
           );

        if(search)
        {

            $.ajax({
                url:"/inventory/search/",
                dataType:"html",
                type:"POST",
                data: data,
                success:success_func,
                error: error_func
            });
        }
        else
        {
            $('#popups').html(" ");
        }



    });

//onclick
    $("#location").find("a").on('click', function(event){
        event.preventDefault();
         var $handler = $(this).parent().parent();
         lat = $handler.find("input[name='lat']").val();
         lng = $handler.find("input[name='lng']").val();
         console.log(lat+" this is the long "+lng);
         initialize();

    });


}

function success_func(response){
     $("#line").show();
    $('#popups').html(response);


}
function error_func(err){
    console.log(err);

}






//initialization
function initialize()
{
    var lng = parseFloat(lng);
    var lat = parseFloat(lat);
    var mapOptions;
    var marker;
    if(isNaN(lng) || isNaN(lat))
    {
        mapOptions = {
            zoom: 8,
            center: new google.maps.LatLng(5.55571, -0.19630)
        };
    }
    else
    {
        mapOptions = {
            zoom: 8,
            center: new google.maps.LatLng(lng, lat)
        };

    }

    var map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
    //inistantiation of marker
    marker = new google.maps.Marker({
        position: new google.maps.LatLng(lng, lat),
        map: map,
        draggable: true,
        animation:google.maps.Animation.BOUNCE
    });

    // This is what happens when you click the map.
    google.maps.event.addListener(map, 'click', function(event) {
        marker.setMap(map);
        marker.setPosition(event.latLng);
        lat = event.latLng.lat();
        lng = event.latLng.lng();
        document.getElementById("lng").value = lng;
        document.getElementById("lat").value = lat;


    });
    // This is what happens when you dragg the marker

    google.maps.event.addListener(marker, 'dragend',function(){
        lat = marker.getPosition().lat();
        lng = marker.getPosition().lng();
        document.getElementById("lng").value = lng;
        document.getElementById("lat").value =  lat;
        var myCenter=new google.maps.LatLng(lat, lng);
        marker.setPosition(myCenter);
    });

}


//Ajax call
function loadScript()
{
    var script = document.createElement('script');
    script.type = 'text/javascript';
    script.src = 'https://maps.googleapis.com/maps/api/js?key=AIzaSyBWDK8TRLNEAx8IP0G0WLzo3fErSXVajc4&sensor=false&' +
        'callback=initialize';
    document.body.appendChild(script);
}