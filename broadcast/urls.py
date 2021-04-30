from django.urls import path, include
from broadcast import views

app_name = 'broadcast'
urlpatterns = [
    path('upload/text/', views.upload_text, name='upload_text'),
    path('upload/image/', views.upload_image, name='upload_image'),
    path('upload/ride/', views.upload_ride, name='upload_ride'),
    path('upload/direction/', views.upload_direction, name='upload_direction'),
    path('',views.index,name='index'),
    path('like/<broadcast_id>/', views.like_broadcast, name='like_broadcast'),
    path('rebc/<bc_id>/', views.rebc, name='rebc'),
    path('<bc_id>/view/', views.broadcast_view, name='view'),
    path('comment/<broadcast_id>/', views.comment, name='comment'),

]