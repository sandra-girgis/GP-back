from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

# from .models import Class, Rating

"""" 
Admin panel 

Keyword arguments:
model -- take the model 'table' from model.py
modelAdmin -- take the model that will display in the admin panel
Return: the admin panel that display when enter localhost:admin
"""
"""
custom display
Args:
    fieldsets : the display of create category form
    list_display : the display of the category list
    search_fields : search fields to custom the list display
"""
class CategoryAdmin(admin.ModelAdmin):
    fieldsets = (
        ['Category Details',{'fields':['name']}],
    )
    list_display = ('name',)
    search_fields = ['name']

class CollectionAdmin(admin.ModelAdmin):
    fieldsets = (
        ['Collection Details',{'fields':['name']}],
    )
    list_display = ('name',)
    search_fields = ['name']

class StudentAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'fields': ('username','email', 'password1','password2','is_staff','phoneNumber')
        }),
    )
    list_display = ('username','email','password','is_staff','phoneNumber')
    search_fields = ['username','email','password','is_staff','phoneNumber']

class InstructorAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'fields': ('username','email','password1','password2','is_staff','phoneNumber','salary' ,'picture' ,'bio')
        }),
    )
    list_display = ('username','email','password','salary' ,'phoneNumber','picture' ,'bio')
    search_fields = ['username','email','password','salary' ,'phoneNumber','picture' ,'bio']

class ClassAdmin(admin.ModelAdmin):
    fieldsets = ( 
        ['Class Details',{'fields':['title', 'content' ,'fromTime','toTime', 'day', 'Category_ID','Instructor_ID',
]}],
    )
    list_display = ( 
    'title', 'content' ,'fromTime','toTime', 'day', 'Category_ID','Instructor_ID',)
    

    search_fields = ['title', 'content']
    list_filter = ['title', 'content']

class AttendAdmin(admin.ModelAdmin):
    fieldsets = (
        ['Attend Details',{'fields':['paymentStatus','Student_ID','Class_ID']}],
    )
    list_display = ('paymentStatus','Student_ID','Class_ID')

class NewsAdmin(admin.ModelAdmin):
    fieldsets = (
        ['News Details',{'fields':['title','content','date','picture','Category_ID']}],
    )
    list_display = ('title','content','date','picture','Category_ID')

class AlbumAdmin(admin.ModelAdmin):
    fieldsets = (
        ['Album Details',{'fields':['name','Collection_ID']}], )
    list_display = ('name','Collection_ID') 

class AlbumPhotoAdmin(admin.ModelAdmin):
    fieldsets = (['AlbumPhoto Details',{'fields':['picture','Album_ID']}],
    )
    list_display = ('picture','Album_ID') 

admin.site.register(Category,CategoryAdmin)
admin.site.register(Collection,CollectionAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Instructor,InstructorAdmin)
admin.site.register(Class,ClassAdmin)
admin.site.register(Attend,AttendAdmin)
admin.site.register(News,NewsAdmin)
admin.site.register(Album,AlbumAdmin)
admin.site.register(AlbumPhoto,AlbumPhotoAdmin)
