$(document).ready(init);
function init(){
    $("#search").keyup(function(){
        var search = $(this).val();
        var token = $("input[name='csrfmiddlewaretoken']").val();
        console.log(search);
        var data = {
            'search':search,
            'csrfmiddlewaretoken':token
        };
        $.ajax({
            url:"/inventory/search/",
            dataType:"html",
            type:"POST",
            data: data,
            success:function(response){
                console.log(response);
            },
            error: function(er){
                console.log(er);
            }
        });

    });


}
