$(document).ready(init);


function init(){
    $("#edit_me").toggle();
    $('#edit').on('click',function(event){
        event.preventDefault();
       $("#profile_me").toggle();
        $("#edit_me").toggle();

    });
}