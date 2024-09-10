from django.urls import path

from . import views
urlpatterns=[
    path('',views.input1,name='input1'),
    path('input2',views.input2,name='input2'),
    
    path('equip1',views.equip1,name='equip1'),
]