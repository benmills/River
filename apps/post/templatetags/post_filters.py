from django import template
from django.core.urlresolvers import reverse
from django.template.defaultfilters import urlize
import re

from userprofile.models import Task

register = template.Library()	

@register.filter
def ispined(user, post):
	if user.get_profile().board.filter(id=post.id): return True
	else: return False
		
@register.filter
def istask(user, post):
	if Task.objects.filter(post=post, user=user): return True
	else: return False

@register.filter
def mediaize(obj):
	types = ('.jpg', '.jpeg', '.gif', '.png')
	line = obj.split(' ')
	output = ''
	
	for l in line:
		# Images
		is_image = -1
		for t in types:
			if l.find(t) > -1:
				is_image = 2
				break
		if is_image > 0:
			l = "<img src='"+l+"'>"
		
		# Youtube
		elif l.find('youtube.com') > 0:
			regex = re.compile(r"^(http://)?(www\.)?(youtube\.com/watch\?v=)?(?P<id>[A-Za-z0-9\-=_]{11})")
			match = regex.match(l)
			if match:
				video_id = match.group('id')
				l = """
						<object width="425" height="344">
						<param name="movie" value="http://www.youtube.com/watch/v/%s"></param>
						<param name="allowFullScreen" value="true"></param>
						<embed src="http://www.youtube.com/watch/v/%s" type="application/x-shockwave-flash" allowfullscreen="true" width="425" height="344"></embed>
						</object>
						""" % (video_id, video_id)
		
		# Vimeo
		elif l.find('vimeo.com') > 0:
			v = l.split('vimeo.com/')
			if len(v)>0: 
				l = """
				<object width="400" height="225">
				<param name="allowfullscreen" value="true" />
				<param name="allowscriptaccess" value="always" />
				<param name="movie" value="http://vimeo.com/moogaloop.swf?clip_id=%s&amp;server=vimeo.com&amp;show_title=1&amp;show_byline=1&amp;show_portrait=0&amp;color=&amp;fullscreen=1" />
				<embed src="http://vimeo.com/moogaloop.swf?clip_id=%s&amp;server=vimeo.com&amp;show_title=1&amp;show_byline=1&amp;show_portrait=0&amp;color=&amp;fullscreen=1" type="application/x-shockwave-flash" allowfullscreen="true" allowscriptaccess="always" width="400" height="225">
				</embed>
				</object>
				""" % (v[1], v[1])
			
		else:
			l = urlize(l)
		
		# Return
		output += l + " "
		
	return output