$( document ).ready(function() {
    $.getJSON( "/get_user_json", function( json ) {
        $("#user_name").append(json.name);
    });
});