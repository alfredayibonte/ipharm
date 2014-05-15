$(document).ready(init);
function init(){
    $("#search").keyup(function(){
        var search = $(this).val();
        var token = $("input[name='csrfmiddlewaretoken']").val();
        var data = {
            'search':search,
            'csrfmiddlewaretoken':token
        };
        $("#first_heading").hide();
        //$("#hide_me").hide();
        $("#find").css({top:"-50px", height:"100%", marginTop:"-16%", marginLeft:'-10%'});
        $("#site-header").css({height:"100%", position:"fixed"});
        $(".text-right").css({marginTop:"-0.5%"});

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



}

function success_func(response){
    $('#popups').html(response);
    console.log(response);
}
function error_func(err){
    console.log(err);

}
