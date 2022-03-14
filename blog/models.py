from django.db import models

# Create your models here.
#class BlogCategories(models.Model):
 
class Categories(models.Model):
  blog_categories = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return self.blog_categories
        

class Posts(models.Model):
    blog_state= [
      ('Draft', 'draft'),
      ('Published', 'published')
    ]
  
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    status = models.CharField(choices = blog_state, default = 'Published', max_length=20)
    category = models.ForeignKey(Categories, on_delete = models.SET_NULL, null = True, blank = True)
    #author = 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']