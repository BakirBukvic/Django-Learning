from . import views
from django.urls import path



app_name = 'food'
urlpatterns=[
    path('',views.IndexClassView.as_view(), name='index'),
    path('<int:pk>/', views.FoodDetail.as_view(), name='detail'),
    path('add-item/', views.CreateItem.as_view(), name='add-item'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete')
   
   
]