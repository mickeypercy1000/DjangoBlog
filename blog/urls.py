from django.urls import path
from blog.views import HomePageView, AddPostView, ListPostsView, UpdatePostView, AddCategoryView, UpdateCategoryView, DeletePostView

urlpatterns = [
  path('', HomePageView, name = 'home'),
  path('add-post/', AddPostView, name = 'add-post'),
  path('update-post/<int:id>/', UpdatePostView, name = 'update-post'),
  path('posts/', ListPostsView, name = 'posts'),
  path('add-category/', AddCategoryView, name = 'add-category'),
  path('update-category/<int:id>/', UpdateCategoryView, name = 'update-category'),
  path('delete/<int:id>/', DeletePostView, name = 'delete-post'),

]