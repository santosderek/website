var images = [];

function preload(imagesToPreload) {
    for (var i = 0; i < imagesToPreload.length; i++) {
        images[i] = new Image();
        images[i].src = imagesToPreload[i];
        console.log("Loaded " + images[i].src);
    }
}

function enableScrollSpy() {
    let minWidth = 1400;
    let isMinimumWidth = $(document).width() > minWidth;

    if ($('#pageLocationScrollSpy').length > 0 && isMinimumWidth) {
        $('body').scrollspy({ target: '#pageLocationScrollSpy' });
        $("#pageLocationScrollSpy").hide();
        $(window).scroll(() => {
            let topOfExperienceDiv = $("#experience").offset().top - 200;
            let isAboveExperienceDiv = $(window).scrollTop() > topOfExperienceDiv;
            if (isAboveExperienceDiv) {
                $("#pageLocationScrollSpy").show();
            }
            else {
                $("#pageLocationScrollSpy").hide();
            }
        });
    }
}

function revealContent() {
    $("#loading").hide();
    $("#content").show();
}

