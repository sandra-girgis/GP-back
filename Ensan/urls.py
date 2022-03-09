from django.urls import path
from . import views
from rest_framework import routers
from .views import *
from django.conf.urls import include

router = routers.DefaultRouter()
router.register('persons', persons) # (route,viewset)
router.register('students', students)
router.register('instructors', instructors)
router.register('category', category)
router.register('classes', classes)
router.register('news', news)
router.register('collections', collections)
router.register('albums', albums)
router.register('albumPhotos', albumPhotos)

urlpatterns = [
    path('',include(router.urls)),
    path('albumphotonew/<int:Aid>',views.albumPhotosnew,name='albumPhotonew'),
]