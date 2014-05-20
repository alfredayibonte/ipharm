$(document).ready(init);
function init(){




    // mandrill start
    $("#email").on('click', email);

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
            {top:"-50px", height:"100%", marginTop:"-16%", marginLeft:'0%', width:'70%'}
           );
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
function er(){}
function suc(){}

//email function for sending email
function email(){
    // ajax to get users
    var token = $("input[name='csrfmiddlewaretoken']").val();
    var data = {

    };
    $.ajax({
        url:"/pharmacy/search/",
                dataType:"html",
                type:"POST",
                data: data,
                success:suc,
                error: er
    });
$.ajax({
  type: "POST",
  url: "https://mandrillapp.com/api/1.0/messages/send.json",
  data: {
    'key': 'OM0lDv3olFdqujMd9yckTQ',
    'message': {
      'from_email': 's****@gmail.com',
      'to': [
          {
            'email': 'd*****@gmail.com',
            'name': 'Test',
            'type': 'to'
          }
        ],
      'autotext': 'true',
      'subject': 'New subject',
      'html': 'YOUR EMAIL CONTENT HERE! YOU CAN USE HTML!'
    }
  }
});

}

