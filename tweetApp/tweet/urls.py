from django.urls import path
from . import views 

 

urlpatterns = [
    path('',views.Tweet_list,name='Tweet_list'),
    path('create/',views.Tweet_create,name='Tweet_create'),
    path('<int:Tweet_id>/edit/',views.Tweet_edit,name='Tweet_edit'),
    path('<int:Tweet_id>/delete/',views.Tweet_delete,name='Tweet_delete'),
    
] 
  