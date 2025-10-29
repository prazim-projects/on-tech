from django.shortcuts import render
from .models import Post, Comment
from django.http import HttpResponseRedirect
from blog.forms import CommentForm

def blog_home(request):
    posts = Post.objects.order_by('-created_at')[:5]
    context = {'posts': posts}
    return render(request, 'blog/index.html', context)


def post_category(request, category):
    posts = Post.objects.filter(categories__name=category).order_by('-created_at')
    context = {'posts': posts, 'category': category}
    return render(request, 'blog/post_category.html', context)


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data['author'],
                body=form.cleaned_data['body'],
                post=post
            )

            comment.save()
            return HttpResponseRedirect(request.path_info)
        
    comments = Comment.objects.filter(post=post).order_by('created_on')
    context = {'post': post, 'comments': comments, 'form': CommentForm()}
    return render(request, 'blog/post_detail.html', context)

