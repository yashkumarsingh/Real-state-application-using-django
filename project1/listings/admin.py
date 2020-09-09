from django.contrib import admin

from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'is_published', 'price', 'list_date','realtor')
    list_display_links = ('title',)
    list_filter = ('realtor','is_published')
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'address', 'zipcode', 'state','city','price')
    list_per_page = 4
admin.site.register(Listing,ListingAdmin)

