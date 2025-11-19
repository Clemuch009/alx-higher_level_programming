$(document).ready(() => {
	$('DIV#toggle_header').on('click', ()=> {
		if ($('header').hasClass('red')) {
			$('header').removeClass('red').addClass('green');
		}else {
			$('header').removeClass('green').addClass('red');
		}
	})
})
