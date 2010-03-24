$(function() {
	$('a.show_edit_form, a.cancel_edit').click(function(e) {
		e.preventDefault();
		$('span.post_text').toggle();
		$('form.edit_form').toggle();
	});
});