from django.urls import path
from . import views

urlpatterns = [
    path('', views.birthday_list, name='birthday_list'),
    path('birthday/<uuid:pk>/', views.birthday_detail, name='birthday_detail'),
    path('birthday/new/', views.birthday_create, name='birthday_create'),
    path('birthday/<uuid:pk>/delete/', views.birthday_delete, name='birthday_delete'),
    path('gifts/<pk>',views.normalview,name='butterflycatcher'),
    # path('thanks/<uuid:birthday_id>',views.thanks,name='thanks'),

]
