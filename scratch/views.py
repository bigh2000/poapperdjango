from django.shortcuts import render
from .models import Post

def show_main(request):
	post_list = Post.objects.all().order_by('-created_at')
	return render(request, 'scratch/main.html', {'post_list':post_list})

def post_detail(request, pk):
	post = Post.objects.get(pk=pk)
	return render(request, 'scratch/post_detail.html', {'post':post,})