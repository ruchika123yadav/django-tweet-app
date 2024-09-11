from django.urls import path
from . import views 

 

urlpatterns = [
    path('',views.home,name='home'),
    path('Tweett/',views.Tweet,name='Tweet'),
    path('Tweet_list/',views.Tweet_list,name='Tweet_list'),
    path('Tweet_create/',views.Tweet_create,name='Tweet_create'),
    path('Tweet_edit/',views.Tweet_edit,name='Tweet_edit'),
    path('Tweet_delete/',views.Tweet_delete,name='Tweet_delete'),
    
] 
  