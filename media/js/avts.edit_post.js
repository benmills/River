$(function(){
	var attachments_hidden = true;
	var todos_hidden = true;
	
	$("select#id_assigned").hide();
	$('div.attachemnts').hide();
	$('div.todos').hide();
	
	$("a.assign_poster").click(function(e){
		e.preventDefault();
		$("select#id_assigned").show();
	});
	
	$('a.add_poster_file').click(function(e){
		e.preventDefault();
		if (attachments_hidden) {
			$('div.attachemnts').show();
			attachments_hidden = false;
			return;
		}
		cloneMore('div.attachemnts p:last', 'files');
	});
	
	$('a.add_poster_todo').click(function(e){
		e.preventDefault();
		if (todos_hidden) {
			$('div.todos').show();
			todos_hidden = false;
			return;
		}
		cloneMore('div.todos p:last', 'todos');
	});
	
	$('a.delete_soft_item').click(function(e){
		e.preventDefault();
		// Make sure we don't delete the last one
		if ($(this).parent('p').parent('div').children('p').length > 1) $(this).parent('p').remove();
	});
});