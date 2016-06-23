from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=200)
	subtitle = models.CharField(max_length=100, blank=True, null=True)
	content = models.TextField(blank=True, null=True)
	photo = models.ImageField(blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	def __unicode__(self):
		return self.title

class Comment(models.Model):
	post = models.ForeignKey(Post)
	author = models.CharField(max_length=10)
	message = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	def comment_set_reverse(self):	# why doesn't it work?
		return self.comment_set.all().order_by('-created_at')
	def __unicode__(self):
		return self.message