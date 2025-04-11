from django.contrib import admin
from watchlist_app.models import WatchList,SteramPlatform,Review
# Register your models here.
admin.site.register(WatchList)
admin.site.register(SteramPlatform)
admin.site.register(Review)