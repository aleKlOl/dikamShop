from django.contrib import admin

from .models import Category, Item, ItemImage

class ItemImageInline(admin.TabularInline):
    model = ItemImage
    extra = 1

class ItemAdmin(admin.ModelAdmin):
    inlines = [ItemImageInline]

admin.site.register(Category)
admin.site.register(Item, ItemAdmin)
admin.site.register(ItemImage)