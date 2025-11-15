from django.shortcuts import render
from .models import Post, Comment
from django.http import HttpResponseRedirect
from blog.forms import CommentForm

def home(request):
    buttons = [
        {'text': 'Our Services', 'url': '#services'},
        {'text': 'Start CTF', 'url': '#ctf'},
        {'text': 'Goto Blogs', 'url': '#blogs'},
    ]

    nav = [
        ["Home", "home"],
        ["Blog", "blog_home"],
    ]

    nav_1 = [
        ["CTF", "challenge_list"],

    ]

    if request.user.is_authenticated:
        nav_1 += [
            ["Dashboard", "dashboard"],
        ]
    else:
        nav_1 += [
            ["Login", "login"],
        ]

    latest_posts = Post.objects.order_by('-created_at')[:4] 

    context = {'nav': nav, 'nav_1': nav_1, 'buttons': buttons, 'latest_posts': latest_posts}
    return render(request, 'home.html', context)


def blog_home(request):
    posts = Post.objects.order_by('-created_at')[:5]
    nav = [
        ["Home", "home"], 
        ["Blog", "blog_home"],    
    ]

    nav_1 = [
        ["CTF", "challenge_list"],

    ]

    if request.user.is_authenticated:
        nav_1 += [
            ["Dashboard", "dashboard"],
        ]
    else:
        nav_1 += [
            ["Login", "login"],
        ]

    context = {'posts': posts, 'nav': nav, 'nav_1': nav_1}
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

