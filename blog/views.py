from django.shortcuts import render, get_object_or_404, redirect
from blog.forms import CommentForm, PostForm, ShareEmailForm
from .models import Post, Category, Comment
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.


def post_list(request):
    posts = Post.objects.all()
    template = 'blog/post_list.html'
    context = {'posts': posts,
               }
    return render(request, template, context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.blog_views = post.blog_views + 1
    post.save()

    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()

    template = 'blog/detail.html'
    context = {'post': post,
               'form': form,
               }
    return render(request, template, context)


@login_required
def create_post(request):
    form = PostForm(data=request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        post.tags.set(form.cleaned_data.get('tags'))
        form.save_m2m()

        messages.info(request, 'Your post has been created')
        return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_create.html', {'form': form})


@login_required
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        messages.success(request, "Your Post has been Updated")
        return redirect('post_list')

    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_create.html', {'form': form, 'post': post})


@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    messages.warning(request, 'Your post has been deleted successfully')
    return redirect('post_list')


def about(request):
    return render(request, 'blog/about.html', {})


@login_required
def comment_delete(request, pk):
    commenti = get_object_or_404(Comment, pk=pk)
    commenti.delete()
    messages.success(request, "The comment has been deleted successfully")
    return redirect('detail', commenti.post.pk)


def share_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = ShareEmailForm(request.POST or None)
    if form.is_valid():
        instance = form.cleaned_data
        subject = f"This is a post shared by {instance['name']},{instance['last_name']}"
        message = f'Read the {post.title} click on the link below \n https://http://127.0.0.1:8000/23/detail/'
        send_mail(subject=subject, message=message, from_email=settings.EMAIL_HOST_USER,
                  recipient_list=[instance['email']], fail_silently=False)
        messages.success(request, "Your Email has been sent!!")
        return redirect('detail', post.pk)
    else:
        form = ShareEmailForm()
    return render(request, 'blog/share.html', {'post': post,
                                               'form': form,
                                               })


def category_details(request, category):
    posts = Post.objects.filter(tags__name__contains=category)
    context = {'category': category,
               'posts': posts
               }
    return render(request, 'blog/category.html', context)




