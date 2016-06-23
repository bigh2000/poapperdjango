from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import CommentForm

def show_main(request):
	post_list = Post.objects.all().order_by('-created_at')
	return render(request, 'main/main.html', {'post_list':post_list})

def post_detail(request, pk):
	post = Post.objects.get(pk=pk)
	return render(request, 'main/post_detail.html', {'post':post,})

def comment_new(request, pk):
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = Post.objects.get(pk=pk)
			form.save()
			return redirect('main.views.post_detail', pk)
	else:
		form = CommentForm()
	return render(request, 'main/post_form.html', {'form':form})

def comment_edit(request, post_pk, pk):
	comment = Comment.objects.get(pk=pk)
	
	if request.method == 'POST':
		form = CommentForm(request.POST, instance=comment)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = Post.objects.get(pk=post_pk)
			form.save()
			return redirect('main.views.post_detail', post_pk)
	else:
		form = CommentForm(instance=comment)
	return render(request, 'main/post_form.html', {'form':form})

def comment_delete(request, post_pk, pk):
	comment = Comment.objects.get(pk=pk)
	if request.method == 'POST':
		comment.delete()
		return redirect('main.views.post_detail', post_pk)
	return render(request, 'main/comment_delete_confirm.html', {'comment':comment})