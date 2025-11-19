$(document).ready(() => {
	$('DIV#add_item').on('click', ()=> {
		const list = $('<li>Item</li>');
		$('UL.my_list').append(list)
	})
})
