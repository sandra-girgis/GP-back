from django.urls import path
from . import views

urlpatterns = [
    path('all-classes',views.all_classes,name='all-classes'),
    path('all-students',views.all_students,name='all-students'),
    path('all-instructors',views.all_instructors,name='all-instructors'),
    path('all-category',views.all_category,name='all-category'),
    path('all-albumPhotos',views.all_albumPhotos,name='all-albumPhotos'),
    path('all-albums',views.all_albums,name='all-albums'),
    path('all-news',views.all_news,name='all-news'),
    path('all-newsPhoto',views.all_newsPhoto,name='all-newsPhoto'),
    path('all-collections',views.all_collections,name='all-collections'),



    # path('api-add', views.api_add_student,name='api-add'),
    # path('api-edit/<st_id>', views.api_edit_student,name='api-edit'),
    # path('api-del/<st_id>', views.api_del_student,name='api-del'),
]



