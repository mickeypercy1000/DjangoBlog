from django.shortcuts import redirect, render

from blog.forms import PostsForm, CategoryForm
from blog.models import Posts

# Create your views here.
def HomePageView(request):
  return render(request, 'blog/HomePage.html')
 

def AddPostView(request):
    form = PostsForm(request.POST or None)
    if form.is_valid():
      form.save()
      return redirect('/posts/')
    return render(request, 'blog/AddPost.html', {'form': form})

def UpdatePostView(request, id = id):
    post = Posts.objects.get(pk =id)
    form  = PostsForm(instance = post)
    if request.method == "POST":
      form = PostsForm(request.POST, instance = post)
    if form.is_valid():
      form.save()
      return redirect('/posts/')
    return render(request, 'blog/UpdatePost.html', {'form': form})

def AddCategoryView(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
      form.save()
      return redirect('/add-post/')
    return render(request, 'blog/AddCategory.html', {'form': form})
 
def ListPostsView(request):
  context = {'posts' : Posts.objects.all()}
  return render(request, 'blog/PostsList.html', context)

def DeletePostsView(request, id = id):
  return render(request, "blog/ConfirmDelete.html")