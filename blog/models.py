from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name.last_name

class Post(models.Model):
  Title = models.CharField(max_length=200)
  Text = models.TextField()
  Author = models.ForeignKey(Author, on_delete=models.CASCADE)
  Created_date = models.DateTimeField(auto_now_add=True)
  Published_date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
        return self.Title