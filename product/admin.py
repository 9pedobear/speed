from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms


class ProductAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Product
        fields = '__all__'



class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = ('id', 'get_photo',
        'title', 'description', 'created', 'updated', 'is_published', 'price')
    list_display_links = ('id', 'title')
    list_filter = ('price', 'created')
    search_fields = ('title', 'price')
    list_editable = ('is_published',)
    fields = (
        'title', 'description',  'is_published', 'price')
    readonly_fields = ('get_photo', 'created', 'updated', 'price')
    save_on_top = True

    def get_photo(self, obj):
        if obj.file:
            return mark_safe(f'<img src="{obj.file.url}" width=80')
        else:
            return '-'



admin.site.register(Product, ProductAdmin)
admin.site.register(Contact)
admin.site.register(Feedback)
