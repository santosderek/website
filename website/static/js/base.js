window.onload = function () {
    $("#loading").hide();
    $("#content").show();

    let minWidth = 1400; 

    // If scroll spy is present
    if ($('#pageLocation').length > 0) {
        $('body').scrollspy({ target: '#pageLocation' })
        // Hide fixed nav if above Experience jumbotron
        $("#pageLocation").hide();
        var topOfOthDiv = $("#experience").offset().top - 200;
        $(window).scroll(function () {
            if ($(window).scrollTop() > topOfOthDiv && $(document).width() > minWidth) {
                $("#pageLocation").show();
            }
            else {
                $("#pageLocation").hide();
            }
        });
    }
}

