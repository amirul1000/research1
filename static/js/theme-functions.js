//Global var
var INSPIRO = {};

(function ($) {

    // USE STRICT
    "use strict";

    //----------------------------------------------------/
    // Predefined Variables
    //----------------------------------------------------/
    var $window = $(window),
        $document = $(document),
        $body = $('body'),
        
        //Utilites
        classFinder = ".";

    /* ---------------------------------------------------------------------------
     * MASONRY ISOTOPE
     * --------------------------------------------------------------------------- */
    INSPIRO.masonryIsotope = function () {

        var $isotops = $(".isotope");
        $isotops.each(function () {
            var isotopeTime,
                $elem = $(this),
                defaultFilter = $elem.data("isotopeDefaultFilter") || 0,
                id = $elem.attr("id"),
                mode = $elem.attr('data-isotope-mode') || "masonry",
                columns = $elem.attr('data-isotope-col') || "4",
                $elemContainer = $elem,
                itemElement = $elem.attr('data-isotope-item') || ".isotope-item",
                itemElementSpace = $elem.attr('data-isotope-item-space') || 0;


            $elem.isotope({
                    filter: defaultFilter,
                    itemSelector: itemElement,
                    layoutMode: mode,
                    transitionDuration: '0.6s',
                    resizesContainer: true,
                    resizable: true,
                    animationOptions: {
                        duration: 400,
                        queue: !1
                    }

                }),

                $window.resize(function () {


                    $elemContainer.css('margin-right', '-' + itemElementSpace + '%');

                    if ($body.hasClass('device-sm') || $body.hasClass('device-xs')) {
                        itemWidth(2, $elemContainer, itemElement, itemElementSpace);
                    } else if ($body.hasClass('device-xxs')) {
                        itemWidth(1, $elemContainer, itemElement, itemElementSpace);
                    } else {
                        itemWidth(columns, $elemContainer, itemElement, itemElementSpace);
                    }

                    if (columns == 1 && $body.hasClass('device-sm') || columns == 1 && $body.hasClass('device-xs')) {
                        itemWidth(1, $elemContainer, itemElement, itemElementSpace);
                    }

                    clearTimeout(isotopeTime), isotopeTime = setTimeout(function () {
                        $elem.isotope("layout");
                    }, 300);
                });




            var $menu = $('[data-isotope-nav="' + id + '"]');

            $menu.length && $menu.find("li:not('.link-only')").on("click", function (e) {
                var $link = $(this);

                $(".filter-active-title").empty().append($link.text());

                if (!$link.hasClass("ptf-active")) {
                    var selector = $link.attr("data-filter");
                    $link.parents(".portfolio-filter").eq(0).find(".ptf-active").removeClass("ptf-active"), $link.addClass("ptf-active"), $elem.isotope({
                        filter: selector
                    });
                }

                e.preventDefault();
                return false;
            }), $window.resize();


        });

    };

    // Intellegent Grid
    var itemWidth = function (columns, $elemContainer, itemElement, itemElementSpace) {

        var $findElement = $elemContainer.find(itemElement);
        var $findElementLarge = $elemContainer.find(".large-item");

        var itemElementMargins = {
            "margin-right": itemElementSpace + "%",
            "margin-bottom": itemElementSpace + "%",
        };

        if (columns == 1) {
            $findElement.width('100%');
            $findElementLarge.width('100%');
        }

        if (columns == 2) {
            $findElement.width(50 - itemElementSpace + '%').css(itemElementMargins);
            $findElementLarge.width(50 - itemElementSpace + '%').css(itemElementMargins);
        }

        if (columns == 3) {
            $findElement.width(33.33 - itemElementSpace + '%').css(itemElementMargins);
            $findElementLarge.width(66.66 - itemElementSpace + '%').css(itemElementMargins);
        }

        if (columns == 4) {
            $findElement.width(25 - itemElementSpace + '%').css(itemElementMargins);
            $findElementLarge.width(50 - itemElementSpace + '%').css(itemElementMargins);
        }

        if (columns == 5) {
            $findElement.width(20 - itemElementSpace + '%').css(itemElementMargins);
            $findElementLarge.width(40 - itemElementSpace + '%').css(itemElementMargins);
        }

        if (columns == 6) {
            $findElement.width(16.666666 - itemElementSpace + '%').css(itemElementMargins);
            $findElementLarge.width(33.333333 - itemElementSpace + '%').css(itemElementMargins);
        }

    };


    //Window load functions
    $window.load(function () {
        INSPIRO.masonryIsotope()
    });

})(jQuery);
