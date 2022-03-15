from . import views
from .views import *
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from rest_framework.authtoken.views import obtain_auth_token

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
router.register('ratings', RatingViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('albumphotonew/<int:Aid>',views.albumPhotosnew,name='albumPhotonew'),
    path('strate/<int:stid>/<int:insid>',views.strate,name='strate'),


    
    ##################
    path('albumsnew/<int:cid>',views.albumsnew,name='albumsnew'),
    path('get_user/<id>',views.get_user,name='get_user'),
    ####################
    path('api-auth',include('rest_framework.urls')),
    path('authtoken/', obtain_auth_token),
    # path('change_password/<int:pk>',views.change_password,name='change_password'),
]