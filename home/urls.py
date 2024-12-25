from django.urls import path
from . import views

urlpatterns = [
    path('',views.main1,name="one"),
    path('2',views.main2,name="two"),
    path('3',views.main3,name="three"),
    path('4',views.main4,name="four"),
    path('5',views.main5,name="five")
]
