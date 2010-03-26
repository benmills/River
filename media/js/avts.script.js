$(function() {
	$('textarea#poster_textarea').focus(function() {
		$(this).html('');
	});
	
	$('#main_poster').submit(function(e){
		var submitting = $('textarea#poster_textarea').val();
		if (submitting.replace(/\s/g, "").length <= 0 || submitting == 'Type your message here...') 
		return false;
	});
});