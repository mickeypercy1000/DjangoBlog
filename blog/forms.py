from django import forms
from blog.models import Post, Categories

class PostsForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ('title', 'slug', 'body', 'status', 'category')
    
  def __init__(self, *args, **kwargs):
    super(PostsForm, self).__init__(*args, **kwargs)
    self.fields['status'].empty_label = 'select post status'
    self.fields['category'].empty_label = 'select post category'
    
class CategoryForm(forms.ModelForm):
  class Meta:
    model = Categories
    fields = ('blog_categories', 'category_summary')