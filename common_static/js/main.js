function changeSliderPosition() {
    var partnersMargin = '-' + Math.round($('#partners').width() / 2) + 'px !important;';
    var partnersHeight = Math.round($('#partners').height()) + 'px;';
    $('footer').css("cssText", 'margin-bottom: ' + partnersHeight );
    $('#partners').css("cssText", 'margin-left: ' + partnersMargin );
}

function getInput(containerID) {
    var inputs = $('#' + containerID).find('input');
    return inputs;
}

function warningInput(inputs) {
    var isValid = true;
    for (var i = 0; i < inputs.length; i++) {
        var className = $(inputs[i]).attr('name');
        if ($(inputs[i]).val() == '' || $(inputs[i]).val() == ' ') {
            $('.' + className).html('This field is required')
            isValid = false;
        }
        else {
            $('.' + className).html('');
        }
    }
    return isValid;
} 

function checkForm() {
    var participantInput = getInput('about-participant');
    var contactInput = getInput('about-parent');
    var participantValid = warningInput(participantInput);
    var contactValid = warningInput(contactInput);
    if (participantValid && contactValid) {
        return true
    } 
    else {
        return false;
    }
}


function checkPrizeInput(inputs) {
    var isOneField = false;
    for (var i = 0; i < inputs.length; i++) {
        if ($(inputs[i]).val() != '' && $(inputs[i]).val() != ' ') {
            isOneField = true;
        }
    }
    return isOneField
}

function clearPrizeWarning() {
    var warnings = $('.prize-warning');
    for (var i = 0; i < warnings.length; i++) {
        $(warnings[i]).html('');
    }
}

function checkPrizeForm() {
    var worldwideInputs = getInput('worldwide');
    var europeanInputs = getInput('european');
    var nationalInputs = getInput('national');
    var returnFlag = true;
    var isValid = {}
    clearPrizeWarning();
    if (!checkPrizeInput(worldwideInputs) && !checkPrizeInput(europeanInputs) && !checkPrizeInput(nationalInputs)) {
        $('.global-warning').removeClass('d-none')
        return false;
    }
    if (checkPrizeInput(worldwideInputs)) {
        isValid.worldwideInputs = warningInput(worldwideInputs);
    }
    if (checkPrizeInput(europeanInputs)) {
        isValid.europeanIsValid = warningInput(europeanInputs);
    }
    if (checkPrizeInput(nationalInputs)) {
        isValid.nationalIsValid = warningInput(nationalInputs);
    }

    for(k in isValid) {
        if (isValid[k] == false) {
            returnFlag = false;
        }
    }

    return returnFlag;
}

function callFileInput(inputID) {
    $('input[name="' + inputID + '"]').click();
}

function checkCategory() {
    if ($('input[name="participant-category"]').val() == '') {
        $('.participant-category').html('Сhoose a category')
        return false
    }
    else {
        $('.participant-category').html('');
        return true;
    }
}

function displayFileName(inputID) {
    var filesContainer = $("div").find(`[data-files='${inputID}']`)
    $(filesContainer).html('');
    var files = $(`input[name="${inputID}"]`)[0].files;
    if (files.length > 0) {
        $("div").find(`[data-remove='${inputID}']`).removeClass('d-none');
        $('.' + inputID).html('');
        for (var i = 0; i < files.length; i++) {
            $(filesContainer).append(`<p>${files[i].name}</p>`)
        }
    }
}

function removeFiles(inputID) {
    var filesContainer = $("div").find(`[data-files='${inputID}']`)
    $(filesContainer).html('');
    $(`input[name="${inputID}"]`).val("");
}

$(document).ready(function() {

    var newsPageNum = 2;
    var shopPageNum = 2;

    // ===================== ALL PAGES =====================

    //  Partners-slider


    $('.partners-slider').slick({
        infinite: true,
        arrows: false,
        slidesToShow: 2,
        slidesToScroll: 2,
        dots: false,
        responsive: [
            {
                breakpoint: 992,
                settings: {
                    slidesToShow: 1,
                    slidesToScroll: 1
                }
            }
        ],
        autoplay: true,
        autoplaySpead: 1000
    });
    changeSliderPosition()
    $(window).resize(changeSliderPosition);

    // Menu
    
    $('.menu-button').click(function(event) {
        $(".small-menu").slideToggle("slow", function() {});
    });
    $('.small-menu').click(function(event) {
        $(this).slideToggle("slow", function() {});
    });

    $('.category-button').click(function(event) {
        $(this).toggleClass('category-button_active');
    });

    // ===================== MAIN PAGE =====================


    if (window.screen.width >= 982) {
        new WOW().init();
        $(window).scroll(function(event) {
            if($("#event").offset().top - $(window).scrollTop() <= 0) {
                $("#event").css({
                    position: 'fixed',
                    top: '0',
                    zIndex: '999'
                });
                $("#event").children('.container').css({
                    background: '#343434',
                    borderTop: 'none' 
                });
            }

            if($(".events-description__first").offset().top - $(window).scrollTop() - $('#event').height() > 0) {
                $("#event").css({
                    position: 'static',
                    top: '100px',
                });
                $("#event").children('.container').css({
                    background: '#343434',
                    borderTop: '2px solid #6d6d6d' 
                });
            }
        });
    }

    //   Banner-slider 
    
    $('.banner-slider').slick({
        infinite: true,
        slidesToShow: 1,
        slidesToScroll: 1,
        dots: true,
        autoplay: true,
        autoplaySpead: 2000,
        prevArrow: '<button class="banner-prev banner-arrow"><img src="static/img/banner-slide-prev.png" class="img-fluid" alt="Prev" /></button>',
        nextArrow: '<button class="banner-next banner-arrow"><img src="static/img/banner-slide-next.png" class="img-fluid" alt="Next" /></button>',
        responsive: [
            {
                breakpoint: 1200,
                settings: {
                    arrows: false
                }
            }
        ]
    });

    // Ajax news loader

    $('#see-more-news').click(function(event) {
        event.preventDefault();
        var csrftoken = Cookies.get('csrftoken');

        $.ajaxSetup({
            cache: false,
            beforeSend: function(xhr, settings) {
                if (!this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });

        $.ajax({
            url: 'http://127.0.0.1:8000/',
            type: 'GET',
            data: {
                page: newsPageNum
            },
            success: function(html){
                newsPageNum += 1;
                $('#see-more-news').before(html);
            }
        });
    });

    // ===================== Shop PAGE =====================

    // Ajax products loader

    $('#see-more-goods').click(function(event) {
        event.preventDefault();
        var csrftoken = Cookies.get('csrftoken');

        $.ajaxSetup({
            cache: false,
            beforeSend: function(xhr, settings) {
                if (!this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            }
        });

        $.ajax({
            url: 'http://127.0.0.1:8000/shop/',
            type: 'GET',
            data: {
                page: shopPageNum
            },
            success: function(html){
                shopPageNum += 1;
                $('#see-more-goods').before(html);
            }
        });

    });

    // Modal window

    $('#buy-button').click(function(event) {
        $('#buy-modal').arcticmodal();

    });

    $('#buy-ticket').click(function(event) {
        event.preventDefault();
        window.open($(this).attr('href'));
    });

    $('.detail-view').click(function(event) {
        event.preventDefault();
        window.open($(this).attr('href'));
    });


    // ===================== APPLAY PAGE =====================

    // Applay form

    var activeContainer;

    $('.category-button').click(function(event) {
        if (activeContainer == undefined) {
            $(this).addClass('category-button_active')
        }
        else {
            $(activeContainer).removeClass('category-button_active');
            $(this).addClass('category-button_active');
        }
        activeContainer = $(this);
        $('input[name="participant-category"]').val($(this).html())
    });

    $('#send-data').click(function(event) {
        event.preventDefault();
        if (checkCategory() && checkForm() && checkPrizeForm()) {
            $(this).parent('form').submit(function() {
                $("input").each(function(index, obj){
                    if ($(obj).val() == "") {
                        $(obj).remove();
                    }
                })
            });
            $(this).parent('form').submit();
        }
    });

    $('#download-worldwide').click(function(event) {
       event.preventDefault();
       callFileInput('download-worldwide')
    });
    $('#download-national').click(function(event) {
       event.preventDefault();
       callFileInput('download-national')
    });
    $('#download-european').click(function(event) {
       event.preventDefault();
       callFileInput('download-european')
    });

    $('input[name="download-worldwide"]').change(function(event) {
        displayFileName('download-worldwide');
    });
    $('input[name="download-national"]').change(function(event) {
        displayFileName('download-national');
    });
    $('input[name="download-european"]').change(function(event) {
        displayFileName('download-european');
    });

    $('.remove-files').click(function(event) {
        event.preventDefault();
        var inputID =  $(this).attr('data-remove');
        $(this).addClass('d-none');
        removeFiles(inputID);
    });

});