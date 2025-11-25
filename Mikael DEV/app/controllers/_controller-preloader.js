/***********************************************
 * SITE: PRELOADER
 ***********************************************/
(function ($) {
	'use strict';
	// check if plugin defined
	if (typeof $.fn.animsition == 'undefined') {
		return;
	}
	var el = $('.animsition');
	if (!el.length) {
		return;
	}
	el.animsition({
		inDuration: 500,
		outDuration: 500,
		linkElement: 'a:not([target="_blank"]):not([href^="#"]):not([rel="nofollow"]):not([href~="#"]):not([href^=mailto]):not([href^=tel]):not(.sf-with-ul)',
		loadingClass: 'animsition-loading-2',
		loadingInner: '<div class="spinner"><span class="double-bounce-one"></span><span class="double-bounce-two"></span></div>',
	});
	el.on('animsition.inEnd', function () {
		VLTJS.window.trigger('vlt.preloader_done');
		VLTJS.html.addClass('vlt-is-page-loaded');
	});

	// Fallback: Force preloader to finish after 3 seconds
	setTimeout(function() {
		if (!VLTJS.html.hasClass('vlt-is-page-loaded')) {
			VLTJS.window.trigger('vlt.preloader_done');
			VLTJS.html.addClass('vlt-is-page-loaded');
			$('.animsition-loading-2').fadeOut();
		}
	}, 3000);
})(jQuery);