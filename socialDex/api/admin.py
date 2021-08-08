from django.contrib import admin
from .models import Post, Profile,BetsStats,OpenBids,SiteSettings
from django.contrib.auth.models import User
# Register your models here.


class BetsStatsAdmin(admin.ModelAdmin):
    model = BetsStats
    list_display =["currency","lastPrice","currentPrice","green"]

class ProfileAdmin(admin.TabularInline):
    model = Profile
    #list_display = ["credit"]

class PostAdmin(admin.ModelAdmin):
    model = Profile
    list_display = ["title","user","datetime"]

class UserAdmin(admin.ModelAdmin):
    inlines = [ProfileAdmin ]

class OpenBidsAdmin(admin.ModelAdmin):
    model = OpenBids
    list_display = ["id","user","currency","bidAmount","vote","status"]

class SiteSettingsAdmin(admin.ModelAdmin):
    model = SiteSettings
    list_display = ["timeToNextUpdate", "creditsForTimeSlotView","timeSlotDuration","secondsToAPIRequest"]

#registers
admin.site.register(Post,PostAdmin)   
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(BetsStats,BetsStatsAdmin)
admin.site.register(OpenBids,OpenBidsAdmin)
admin.site.register(SiteSettings,SiteSettingsAdmin)

