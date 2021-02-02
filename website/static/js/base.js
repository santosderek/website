var images = [];

function preload() {
    for (var i = 0; i < arguments.length; i++) {
        images[i] = new Image();
        images[i].src = preload.arguments[i];
        console.log("Loaded " + images[i].src);
    }
}

function revealContent(imagesToPreload) {

    for (var count = 0; count < imagesToPreload.length; count++) {
        preload(imagesToPreload[count]);
    }

    $("#loading").hide();
    $("#content").show();

    let minWidth = 1400; 

    // If scroll spy is present
    if ($('#pageLocationScrollSpy').length > 0) {
        $('body').scrollspy({ target: '#pageLocationScrollSpy' })
        // Hide fixed nav if above Experience jumbotron
        $("#pageLocationScrollSpy").hide();
        var topOfOthDiv = $("#experience").offset().top - 200;
        $(window).scroll(function () {
            if ($(window).scrollTop() > topOfOthDiv && $(document).width() > minWidth) {
                $("#pageLocationScrollSpy").show();
            }
            else {
                $("#pageLocationScrollSpy").hide();
            }
        });
    }
}

