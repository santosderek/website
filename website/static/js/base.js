window.onload = function () {
    $("#loading").hide();
    $("#content").show();
    $('body').scrollspy({ target: '#pageLocation' })

    // Hide fixed nav if above Experience jumbotron
    $("#pageLocation").hide(); //hide your div initially
    var topOfOthDiv = $("#experience").offset().top;
    $(window).scroll(function() {
        if($(window).scrollTop() > topOfOthDiv) { //scrolled past the other div?
            $("#pageLocation").show(); //reached the desired point -- show div
        }
        else{
            $("#pageLocation").hide(); //else above the desired point -- hide div
        }
    });
}

