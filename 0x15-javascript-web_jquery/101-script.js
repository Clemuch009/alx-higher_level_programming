$(document).ready(()=> {
	const new_element = $('<li>Item</li>');
	$('DIV#add_item').on('click', ()=> {
		$('UL.my_list').append(new_element);
	});
	$('DIV#remove_item').on('click', ()=> {
		$('UL.my_list').children().last().remove();
	});
	$('DIV#clear_list').on('click', () => {
		$('UL.my_list').empty();
	});
})
