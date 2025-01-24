from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.addData, name='add'),
    path('details/', views.details, name='detail'),
    path('details/<int:id>', views.details, name='details'),
    path('update/', views.update, name='updates'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:pk>', views.deleteData, name='delete')
]
