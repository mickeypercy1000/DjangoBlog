from django.shortcuts import redirect, render

from blog.forms import PostsForm, CategoryForm
from blog.models import Post, Categories

# Create your views here.
def HomePageView(request):
  context = {'trendingcategories' : Categories.objects.all()}
  return render(request, 'blog/body.html', context)
 
# Add Post.
def AddPostView(request):
    form = PostsForm(request.POST or None)
    if form.is_valid():
      form.save()
      return redirect('/posts/')
    return render(request, 'blog/AddPost.html', {'form': form})
# Update Post.
def UpdatePostView(request, id = id):
    post = Post.objects.get(pk =id)
    form  = PostsForm(instance = post)
    if request.method == "POST":
      form = PostsForm(request.POST, instance = post)
    if form.is_valid():
      form.save()
      return redirect('/posts/')
    return render(request, 'blog/UpdatePost.html', {'form': form})
  
# Add Category.
def AddCategoryView(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
      form.save()
      return redirect('/add-post/')
    return render(request, 'blog/AddCategory.html', {'form': form})
  
# Update Category.
def UpdateCategoryView(request, id = id):
    post = Categories.objects.get(pk =id)
    form  = CategoryForm(instance = post)
    if request.method == "POST":
      form = CategoryForm(request.POST, instance = post)
    if form.is_valid():
      form.save()
      return redirect('/add-category/')
    return render(request, 'blog/UpdateCategory.html', {'form': form})

# Create Post List.
def ListPostsView(request):
  context = {'posts' : Post.objects.all()}
  return render(request, 'blog/lister.html', context)

def DeletePostView(request, id = id):
  post = Post.objects.get(id=id)
  post.delete()
  return redirect('/posts/')