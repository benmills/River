$(function() {
	$('a.show_edit_form, a.cancel_edit').click(function(e) {
		e.preventDefault();
		$('span.post_text').toggle();
		$('form.edit_form').toggle();
	});
	
	$('a.delete_soft_item_edit').click(function(e) {
		e.preventDefault();
		console.log($(this).siblings('input[type=checkbox]').attr('checked', 'true'));
		$(this).parent('p').hide();
	});
});