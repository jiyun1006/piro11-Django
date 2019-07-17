from django.urls import path
from . import views

urlpatterns =[

    path('sum/', views.mysum),
    path('hello/',views.hello),
]