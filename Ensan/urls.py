from django.urls import path
from . import views

urlpatterns = [
    path('all-classes', views.all_classes,name='all-classes'),
    # path('api-one/<st_id>', views.api_one_student,name='api-one'),
    # path('api-add', views.api_add_student,name='api-add'),
    # path('api-edit/<st_id>', views.api_edit_student,name='api-edit'),
    # path('api-del/<st_id>', views.api_del_student,name='api-del'),
]
