from django.urls import  path
from . import views
urlpatterns =[
    path('views/', views.post_list),
    path('<int:id>/', views.post_detail),


]


