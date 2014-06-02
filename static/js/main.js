$(document).ready(init);

var lng;
var lat;
var search;
var inventory;
var drug;
var pharmacy;
var drug_id;

function ajaxCall1() {
    $.ajax({
        url: "/api/drugs/",
        dataType: "json",
        type: "GET",
        success: success_func,
        error: error_func
    });

}

function ajaxCall2(id) {
    $.ajax({
        url: "/api/find/?id=" + id,
        dataType: "json",
        type: "GET",
        success: inventory_success,
        error: error_func
    });
}



function init() {
    ajaxCall1();


    //search ajax
    $("#search").keyup(function() {
        $("#first_heading").hide();
        //$("#find").addClass("move_up");
        $(".header-features ").addClass("me");
    });



}

function success_func(response) {
    drug = response;
    var tags = [];
    for (var i = 0; i < response.length; i++) {
        tags.push(response[i].name);

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
            for (var i = 0; i < response.length; i++) {
                if (drug[i].name == ui.item.value) {
                    $("#drug").html(drug[i].name + ": ");
                    $("#description").html(response[i].description);
                    drug_id = drug[i].id;
                }
            }
            ajaxCall2(drug_id);
        }

    });






}

function error_func(err) {
    console.log(err);

}

function inventory_success(response) {
    inventory = response;
    for (var i = 0; i < response.length; i++) {
        var name = "<h3><a href='www.google.com'>" + inventory[i].name + "</a><h3>";
        var email = "<i class=\"fa fa-envelope-square\"></i> &nbsp;<span>" + inventory[i].email + "</span>";
        var address = "<br><i class=\"fa fa-map-marker\"></i>&nbsp;<span>" + inventory[i].address + "</span>";
        inventory[i].name;
        $(name, {}).appendTo("#boto");
        $(email, {}).appendTo("#boto");
        $(address, {}).appendTo("#boto");

    }

}