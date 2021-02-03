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

    let minWidth = 1400; 

    if ($('#pageLocationScrollSpy').length > 0) {
        $('body').scrollspy({ target: '#pageLocationScrollSpy' });
        // Hide fixed nav if above Experience jumbotron
        $("#pageLocationScrollSpy").hide();
        
        $(window).scroll(() => {
            let topOfExperienceDiv = $("#experience").offset().top - 200;
            let isAboveExperienceDiv = $(window).scrollTop() > topOfExperienceDiv;
            let isMinimumWidth = $(document).width() > minWidth;
            
            if (isAboveExperienceDiv && isMinimumWidth) {
                $("#pageLocationScrollSpy").show();
            }
            else {
                $("#pageLocationScrollSpy").hide();
            }
        });
    }

    $("#loading").hide();
    $("#content").show();
}

