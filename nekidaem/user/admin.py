from django.contrib import admin

from blog.models import UserSubscription, Blog
from post.models import UserWatchedPosts, Post
from user.models import User

admin.site.register(User)
admin.site.register(UserSubscription)
admin.site.register(Blog)
admin.site.register(UserWatchedPosts)
admin.site.register(Post)
