$(document).ready(init);
var lng;
var lat;
var search;

function init() {
    $("#line").hide();
    $("#first_heading").hide();
    $.ajax({
        url: "/drug_list/",
        dataType: "json",
        type: "GET",
        success: success_func,
        error: error_func
    });


    //search ajax
    $("#search").keyup(function() {

        $("#find").addClass("move_up");
    });

    //onclick
    $("#location").find("a").on('click', function(event) {
        event.preventDefault();
        var $handler = $(this).parent().parent();
        lat = $handler.find("input[name='lat']").val();
        lng = $handler.find("input[name='lng']").val();
        console.log(lat + " this is the long " + lng);
        initialize();

    });


}

function success_func(response) {
    var tags = [];
    for (var i = 0; i < response.length; i++) {
        tags.push(response[i].name)
    }

    $("#search").autocomplete({
        source: function(request, response) {
            var matcher = new RegExp("^" + $.ui.autocomplete.escapeRegex(request.term), "i");
            response($.grep(tags, function(item) {
                return matcher.test(item);
            }));
        },
        select: function(event, ui) {
            console.log(ui.item.value);
        },
        maxItems: 5
    });




}

function error_func(err) {
    console.log(err);

}