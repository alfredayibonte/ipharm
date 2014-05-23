$(document).ready(init);
var lng;
var lat;
function init(){
    initialize();
}

$("#location").find("a").on('click',function(event){
    event.preventDefault();
    var $handler = $(this).parent().parent();
    lat = $handler.find("input[name='lat']").val();
    lng = $handler.find("input[name='lng']").val();
    console.log(lat+" this is the long "+lng);
    console.log("hello world");

});
