$(document).ready(init);
var lng;
var lat;
var search;

function init() {
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



}

function success_func(response) {
    var tags = [];
    var id_list = []
    for (var i = 0; i < response.length; i++) {
        tags.push(response[i].name);
        id_list
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
            console.log(response);
        }

    });




}

function error_func(err) {
    console.log(err);

}