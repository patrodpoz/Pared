from django.urls import path, include
from . import views  
urlpatterns = [
    path('', views.login),
    path('create_user', views.create_user),
    path('login', views.log_in),
    path('pared', views.pared),
    path('message', views.post_message),
    path('comment/<int:msg_id>', views.post_comment),
    path('logout', views.logout),
]