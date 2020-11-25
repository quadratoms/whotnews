from django.contrib import admin
from .models import Newsmodel, Comment, cartegory, Source

admin.site.register(Newsmodel)
admin.site.register(Comment)
admin.site.register(cartegory)
admin.site.register(Source)


# Register your models here.
