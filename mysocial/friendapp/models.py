from django.db import models
from django.contrib.auth.models import User

class SiteCommenter(models.Model):
    user = models.OneToOneField(User)
    
    def __unicode__(self):
        return self.name

class Comment(models.Model):
    siteCommenter = models.ForeignKey(SiteCommenter)
    comment_text = models.CharField(max_length=300)

    def __unicode__(self):
        return self.name
