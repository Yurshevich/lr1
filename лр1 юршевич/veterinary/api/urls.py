from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('orders/', views.OrdersList.as_view()),
    path('orders/<int:pk>', views.OrderDetail.as_view()),
    path('categories/', views.CategoriesList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)