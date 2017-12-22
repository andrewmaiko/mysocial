from django.contrib import admin
from friendapp.models import Comment
from django.contrib.auth.models import User

class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ('siteCommenter', 'comment_text',)
    prepopulated_fields = {'slug' : ('comment_text',)}

admin.site.register(Comment, CommentAdmin)

# Register your models here.
