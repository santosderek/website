window.onload = function () {
    $("#loading").hide();
    $("#content").show();
    $('body').scrollspy({ target: '#pageLocation' })

    // Hide fixed nav if above Experience jumbotron
    $("#pageLocation").hide(); 
    var topOfOthDiv = $("#experience").offset().top;
    $(window).scroll(function() {
        if($(window).scrollTop() > topOfOthDiv && $(document).width() > 1400) {
            $("#pageLocation").show(); 
        }
        else{
            $("#pageLocation").hide(); 
        }
    });
}

