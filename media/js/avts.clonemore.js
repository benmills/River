function cloneMore(selector, type) {
	var newElement = $(selector).clone(true);
	var total = $('#id_' + type + '-TOTAL_FORMS').val();
	
	newElement.find(':input').each(function() {
			var name = $(this).attr('name').replace('-' + (total-1) + '-','-' + total + '-');
			var id = 'id_' + name;
			if ($(this).is('[type="checkbox"]')) $(this).attr({'name': name, 'id': id}).removeAttr('checked');
			else $(this).attr({'name': name, 'id': id}).val('').removeAttr('checked');
	});
	
	newElement.find('label').each(function() {
			var newFor = $(this).attr('for').replace('-' + (total-1) + '-','-' + total + '-');
			$(this).attr('for', newFor);
	});
	
	total++;
	$('#id_' + type + '-TOTAL_FORMS').val(total);
	console.log($(selector).html());
	console.log(newElement);
	$(selector).after(newElement);
}