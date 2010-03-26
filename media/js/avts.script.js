var title_changed = false;

$(function() {
	$('textarea#poster_textarea').focus(function() {
		$(this).html('');
	});
	
	$('input#poster_title').keypress(function() {
		title_changed = true;
	});
	
	$('textarea#poster_textarea').keyup(function(e){
		$('input#poster_title').show();
		val = $(this).val()
		if (val.length < 20 && !title_changed)
			$("input#poster_title").val($(this).val());
	});
	
	$('#main_poster').submit(function(e){
		var submitting = $('textarea#poster_textarea').val();
		if (submitting.replace(/\s/g, "").length <= 0 || submitting == 'Type your message here...') 
		return false;
	});
});