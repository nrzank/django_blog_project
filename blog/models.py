from django.db import models

from django.contrib.auth import get_user_model


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)


    def __str__(self):
        return f"{self.name} ({self.pk})"



class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    categories = models.ManyToManyField(Category)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # class Meta:
    #     db_table = 'posts'
    #     ordering = ('created_at', )
    #
    #


    @property
    def post_info(self):
        return f"Title: {self.title}," \
               f"Post: {self.content}"


    def __str__(self):
        return f"{self.title} ({self.pk})"



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")  # related_name: comment_set
    text = models.CharField(max_length=200)

    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # class Meta:
    #     db_table = 'comments'
    #     ordering = ('created_at',)
    #     unique_together = ('text', 'author')
    #     default_related_name = 'comments'

    def __str__(self):
        return f"{self.text} ({self.pk})"
