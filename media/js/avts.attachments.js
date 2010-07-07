$(function(){
	var attachments_hidden = true;
	var todos_hidden = true;
	var attachments_single_hidden = false;
	var todos_single_hidden = false;
	
	//$("select#id_assigned").hide();
	$('div.assigner').hide();
	$('div.todos').hide();
	$('div.attachemnts').hide();
	
	if ($('div.attachemnts p').length > 1) {
		$('div.attachemnts').show();
		attachments_hidden = false;
		attachments_single_hidden = true;
		$('div.attachemnts p:last').hide();
	}
	
	if ($('div.todos p').length > 1) {
		$('div.todos').show();
		todos_hidden = false;
		todos_single_hidden = true;
		$('div.todos p:last').hide();
	}
	
	$("a.assign_poster").click(function(e){
		e.preventDefault();
		$(".assigner").toggle();
	});
	
	$('a.add_poster_file').click(function(e){
		e.preventDefault();
		if (attachments_hidden) {
			$('div.attachemnts').show();
			attachments_hidden = false;
			return;
		} else if (attachments_single_hidden) {
			$('div.attachemnts p:last').show();
			attachments_single_hidden = false;
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
		} else if (todos_single_hidden) {
				$('div.todos p:last').show();
				todos_single_hidden = false;
				return;
			}
		cloneMore('div.todos p:last', 'todos');
	});
	
	$('a.delete_soft_item').click(function(e){
		e.preventDefault();
		// Make sure we don't delete the last one
		if ($(this).parent('p').parent('div').children('p').length > 1) $(this).parent('p').remove();
		else {
			$(this).parent('p').parent('div').hide();
			if ($(this).parent('p').parent('div').attr('class') == 'todos') todos_hidden = true;
			if ($(this).parent('p').parent('div').attr('class') == 'attachemnts') attachments_hidden = true;
		}
	});
});