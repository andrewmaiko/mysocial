from django.db import models
from django.contrib.auth.models import User



class Comment(models.Model):
    siteCommenter = models.ForeignKey(User)
    comment_text = models.CharField(max_length=300, default='')
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return self.name
