from django.contrib import admin
from .models import *

"""" Admin panel 

Keyword arguments:
model -- take the model 'table' from model.py
modelAdmin -- take the model that will display in the admin panel
Return: the admin panel that display when enter localhost:admin
"""




class CategoryAdmin(admin.ModelAdmin):
    """custom display

    Args:
        fieldsets : the display of create category form
        list_display : the display of the category list
        search_fields : search fields to custom the list display
    """
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

class StudentAdmin(admin.ModelAdmin):
    fieldsets = (
        ['Student Details',{'fields':['username','email','password']}],
    )
    list_display = ('username','email','password')
    search_fields = ['username','email','password']

######################  student phone no.

class InstructorAdmin(admin.ModelAdmin):
    fieldsets = (
        ['Instructor Details',{'fields':['username','email','password',
    'salary','numberLectures' ,'picture' ,'bio']}],)
    list_display = ('username','email','password','salary','numberLectures' ,'picture' ,'bio')
    search_fields = ['username','email','password','salary','numberLectures' ,'picture' ,'bio']

######################  instructor phone no.
'title', 'content' ,'average_rate','fromTime','toTime', 'day', 'Category_ID','Instructor_ID'



class CourseAdmin(admin.ModelAdmin):
    fieldsets = ( 
        ['Course Details',{'fields':['title', 'content' ,'average_rate','fromTime','toTime', 'day', 'Category_ID','Instructor_ID'
]}],
    )
    list_display = ( 
'title', 'content' ,'average_rate','fromTime','toTime', 'day', 'Category_ID','Instructor_ID')


class ReviewAdmin(admin.ModelAdmin):
    fieldsets = (
        ['Review Details',{'fields':['rate','comment','Student_ID','Category_ID']}],
    )
    list_display = ('rate','comment','Student_ID','Category_ID')


class AttendAdmin(admin.ModelAdmin):
    fieldsets = (
        ['Attend Details',{'fields':['paymentStatus','Student_ID','Category_ID']}],
    )
    list_display = ('paymentStatus','Student_ID','Category_ID')



class NewsAdmin(admin.ModelAdmin):
    fieldsets = (
        ['News Details',{'fields':['title','content','date','Category_ID']}],
    )
    list_display = ('title','content','date','Category_ID')

class NewsPhotoAdmin(admin.ModelAdmin):
    fieldsets = (
        ['NewsPhoto Details',{'fields':['picture','News_ID']}],
    )
    list_display = ('picture','News_ID')


class AlbumAdmin(admin.ModelAdmin):
    fieldsets = (
        ['Album Details',{'fields':['name','Collection_ID']}], )
    list_display = ('name','Collection_ID') 

# class AlbumPhotoAdmin(admin.ModelAdmin):
#     fieldsets = (['AlbumPhoto Details',{'fields':['picture','Album_ID']}],
#     )
#     list_display = ('picture ','Album_ID') 


admin.site.register(Category,CategoryAdmin)
admin.site.register(Collection,CollectionAdmin)
admin.site.register(Student,StudentAdmin)
admin.site.register(Instructor,InstructorAdmin)
admin.site.register(Course,CourseAdmin)
admin.site.register(Attend,AttendAdmin)
admin.site.register(Review,ReviewAdmin)
admin.site.register(NewsPhoto,NewsPhotoAdmin)
admin.site.register(News,NewsAdmin)

admin.site.register(Album,AlbumAdmin)
# admin.site.register(AlbumPhoto,AlbumPhotoAdmin)
