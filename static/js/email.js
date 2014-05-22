$(document).ready(function() {
    var to = [];
    var email;
    var mylist = [];
    // grabbing value in check boxes
    $("input[type='checkbox']").on('click', function() {
        var state = $(this).prop('checked');
        email = $(this).parent().parent().find("span[class='title']").html();
        if (state) {
            to.push(email);
            $(this).prop('checked', true);
            $('#to').val(to.join(', '));
        } else {

            to.splice(email, 1);
            $(this).prop('checked', false);
            $('#to').val(to.join(', '));
        }
    });

    $("#send").on('click', function(event) {
        event.preventDefault();
        var from = $("input[name='username']").val();
        console.log(from);
        to = $('#to').val();
        var subject = $('#subject').val();
        var message = $("textarea[class='textarea form-control']").val();
        var arraylist = $('#to').val().split(',');
        for (var i = 0; i < arraylist.length; i++) {

            console.log(arraylist[i].trim());
            mylist.push({
                'email': arraylist[i].trim()
            });
        }

        //mandrill api implementation
        $.ajax({
            type: "POST",
            url: "https://mandrillapp.com/api/1.0/messages/send.json",
            data: {
                'key': 'OM0lDv3olFdqujMd9yckTQ',
                'message': {
                    'from_email': from,
                    'to': mylist,
                    'autotext': 'true',
                    'subject': subject,
                    'html': message
                }
            },
            success: success_func,
            error: error_func
        });

    });
});

function success_func(data) {

    location.reload();
    $('#success').show();
}

function error_func(er) {

    location.reload();

}