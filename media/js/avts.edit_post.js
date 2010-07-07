$(function(){
	$('.todos input[type=checkbox], .attachemnts input[type=checkbox]').hide();
	$('a.delete_soft_item').click(function(e){
		e.preventDefault();
		// Make sure we don't delete the last one
		if ($(this).parent('p').parent('div').children('p').length > 1) $(this).parent('p').remove();
	});
	
	$('a.edit_post_link').click(function(e) {
		e.preventDefault();
		$('.info').toggle();
		$('.comment_div').toggle();
		$('.edit_form').toggle();
		$('.item_content').toggle();
	})
});