from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.CharField('title', max_length=256)
    content = models.TextField('content')

    pub_date = models.DateTimeField('publish-time', auto_now_add=True, editable=True)
    update_time = models.DateTimeField('update-time', auto_now=True, null=True)

    def __str__(self):
        return self.title
