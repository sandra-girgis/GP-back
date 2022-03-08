from django.urls import path
from . import views
from rest_framework import routers
from .views import *
from django.conf.urls import include

router = routers.DefaultRouter()
router.register('persons', persons)# rout viewset
router.register('students', students)
router.register('instructors', instructors)

urlpatterns = [
    path('',include(router.urls)),
    path('classes',views.classes,name='classes'),
    # path('students',views.students,name='students'),
    # path('instructors',views.instructors,name='instructors'),
    path('category',views.category,name='category'),
    path('albumphotos',views.albumPhotos,name='albumPhotos'),
    path('albums',views.albums,name='albums'),
    path('news',views.news,name='news'),
    path('collections',views.collections,name='collections'),

    path('albumphotonew/<int:colid>/<int:Aid>',views.albumPhotosnew,name='albumPhotonew'),
]



