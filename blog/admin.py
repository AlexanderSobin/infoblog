from django.contrib import admin
from blog.models import Article, Feedback, Comments

admin.site.register(Article)
#admin.site.register(Feedback)
admin.site.register(Comments)
