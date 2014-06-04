$(document).ready(init);


var drug;
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
    $('.page-container').hide();
    ajaxCall1();


    //search ajax
    $("#search").keyup(function() {
        $(".h3").hide();
        $(this).parent().parent().css({
            'marginTop': '-70px'
        });
        $("#first_heading").hide();

    });



}

function success_func(response) {
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
            $('.page-container').show();
            for (var i = 0; i < response.length; i++) {
                if (response[i].name == ui.item.value) {
                    $("#drug").html(response[i].name + ": ");
                    $("#description").html(response[i].description);
                    drug_id = response[i].id;
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

    if (response.length >= 1) {
        $("<h1>PHARMACIES</h1>", {}).appendTo("#boto");
        for (var i = 0; i < response.length; i++) {
            var name = "<h3 ><a href=\"/map/" + response[i].username + "/\" class='text-primary'>" + response[i].name + "</a><h3>";
            var email = "<i class=\"fa fa-envelope-square\"></i> &nbsp;<span class='change'>" + response[i].email + "</span>";
            var address = "<br><i class=\"fa fa-map-marker\"></i>&nbsp;<span class='change'>" + response[i].address + "</span>";
            var telephone = "<br><i class=\"fa fa-phone\"></i>&nbsp;<span class='change'>" + response[i].telephone + "</span>";
            $(name, {}).appendTo("#boto");
            $(email, {}).appendTo("#boto");
            $(address, {}).appendTo("#boto");
            $(telephone, {}).appendTo("#boto");

        }

    }


}