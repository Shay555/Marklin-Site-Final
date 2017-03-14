from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
from .forms import BlogPostForm
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def post_list(request):
    """
    Create a view that will return a
    list of Posts that were published prior to'now'
    and render them to the 'blogposts.html' template
    """
    posts = Post.objects.filter(published_date__lte=timezone.now()
                                ).order_by('-published_date')

    paginator = Paginator(posts, 6)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, "blogposts.html", {'posts': posts})


def post_detail(request, id):
    post  = get_object_or_404(Post, pk=id)
    post.views += 1 # clock up the number of post views
    post.save()
    return render(request, "postdetail.html",{'post': post})


def new_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect(post_detail, post.pk)
    else:
        form = BlogPostForm()
    return render(request, 'blogpostform.html', {'form': form})

def edit_post(request, id):
   post = get_object_or_404(Post, pk=id)
   if request.method == "POST":
       form = BlogPostForm(request.POST, request.FILES, instance=post)
       if form.is_valid():
           post = form.save(commit=False)
           post.author = request.user
           post.published_date = timezone.now()
           post.save()
           return redirect(post_detail, post.pk)
   else:
       form = BlogPostForm(instance=post)
   return render(request, 'blogpostform.html', {'form': form})


# def listing(request):
#     blog_list = Post.objects.all()
#     paginator = Paginator(blog_list, 4)
#
#     page = request.GET('page')
#     try:
#         blog = paginator.page(page)
#     except PageNotAnInteger:
#         # If page is not an integer, deliver first page.
#         blog = paginator.page(1)
#     except EmptyPage:
#         # If page is out of range (e.g. 9999), deliver last page of results.
#         blog = paginator.page(paginator.num_pages)
#
#     return render(request, 'postdetail.html', {'blog': blog})