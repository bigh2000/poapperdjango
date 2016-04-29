from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=200)
	subtitle = models.CharField(max_length=100, blank=True, null=True)
	content = models.TextField(blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return self.title