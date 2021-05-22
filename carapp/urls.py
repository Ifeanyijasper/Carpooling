from django.urls import path
from carapp import views

app_name = 'carapp'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('accounts/login/', views.login_user, name='login_user'),

    path('signup/', views.CreateUser.as_view(), name='sign_up'),

    path('user/(<pk>[0-9]+)/', views.view_user_id, name='profile'),

    path('profile/(<user_id>[a-zA_Z0-9]+)/', views.view_user_name, name='user-profile'),
    path('app/profile/<user_id>/', views.view_user_name, name='user-profile'),
    path('profile/<user_id>/', views.view_user_name, name='user-profile'),
    path('user/dashboard/', views.dashboard, name='dashboard'),
    path('user/dashboard/messages/', views.messages, name='dashboard_messages'),
    path('user/dashboard/notifications/', views.notifications, name='dashboard_notifications'),
    path('user/dashboard/timeline/', views.timeline, name='dashboard_timeline'),

    path('accounts/profile', views.create_profile, name='profile_make'),


    path('user/dashboard/sent/', views.sent, name='dashboard_sent'),

    path('user/dashboard/junk/', views.messages_junk, name='dashboard_junk'),
    path('user/dashboard/messages/(<message_id>[0-9]+)/read/', views.messages_read, name='dashboard_messages_read'),
    path('app/user/dashboard/messages/<message_id>/read/', views.messages_read, name='dashboard_messages_read'),
    path('user/dashboard/sent/(<message_id>[0-9]+)/read/', views.messages_read_sent, name='dashboard_messages_read_sent'),

    path('user/dashboard/messages/(<message_id>[0-9]+)/reply/', views.messages_reply, name='dashboard_messages_reply'),

    path('user/dashboard/messages/(<message_id>[0-9]+)/forward/', views.messages_forward, name='dashboard_messages_forward'),

    path('user/dashboard/messages/compose/', views.messages_compose, name='dashboard_messages_compose'),


    path('accounts/login/', views.login_user, name='login_user'),
    path('about/', views.about, name='about'),
    path('about_goride/', views.about_goride, name='about_goride'),
    path('contact/', views.contact, name='contact'),
    path('ride/(<user_id>[0-9]+)/', views.ride, name='ride'),
    path('ride/', views.ride, name='ride'),

    path('follow/(<followee>[0-9]+)/(<follower>[0-9]+)/',views.do_follow,name='follow'),

    path('user/(<pk>[0-9]+)/update-profile/', views.EditUser.as_view(), name='user_update'),

    path('logout/', views.logout_user, name='logout_user'),
    path('login/', views.do_login, name='login'),



    path('user/(<user_id>[0-9]+)/add-ride/', views.vehicle_create, name='add_ride'),

    path('user/(<user_id>[0-9]+)/view-rides/', views.vehicle_view, name='view_rides'),

    path('user/(<user_id>[0-9]+)/delete-ride/(<vehicle_id>[0-9]+)/', views.vehicle_delete, name='delete_ride'),

    path('user/(<user_id>[0-9]+)/share-ride/(<vehicle_id>[0-9]+)/', views.vehicle_share, name='share_ride'),

    path('user/(<user_id>[0-9]+)/view-shared/', views.vehicle_shared_view, name='view_shared'),

    path('user/<user_id>/search/', views.vehicle_search, name='search_ride'),

    path('user/(<user_id>[0-9]+)/request/(<ride_id>[0-9]+)', views.request_ride, name='request_ride'),

    path('app/sharing/<int:vehicle_share_id>/view/', views.view_single_ride, name='view_shared_ride'),

    path('app/ride/<ride_id>/view/', views.view_single_vehicle, name='view_shared_vehicle'),

    path('sharing/(<user_id>[0-9]+)/delete/(<vehicle_share_id>[0-9]+)/', views.vehicle_share_delete, name='delete_shared_ride'),

    path('requests/(<user_id>[0-9]+)/view', views.requests_driver_view, name='request_driver_view'),
    path('requests/all/',views.all_ride_requests, name='view_ride_requests'),
    path('request/(<request_id>[0-9]+)/approve/', views.request_approve, name='request_driver_approve'),
    path('request/(<request_id>[0-9]+)/deny/', views.request_deny, name='request_driver_deny'),

    # url(r'^requests/(?P<user_id>[0-9]+)/view$', views.requests_driver_view, name='request_driver_view'),

    path('app/request/<request_id>/view/', views.request_view, name='request_view'),
    path('user/<user_id>/requests/', views.requests_user_view, name='requests_user_view'),
    # path('user/<str:user_id>/requests/<', views.requests_user_view, name='requests_user_view'),

    path('request/(<request_id>[0-9]+)/delete/', views.request_delete, name='request_delete'),

    path('notification/read/', views.mark_as_read, name='mark_as_read'),

    path('user/messages/unread/', views.unread_messages, name='unread_messages'),
    path('app/user/messages/unread/', views.unread_messages, name='unread_messages'),
    path('user/messages/(<message_id>[0-9]+)/delete/', views.delete_message, name='delete_message'),

    path('user/preferences/', views.preferences, name='preferences'),

    path('user/preferences/image-update/', views.image_update, name='image_update'),

    path('user/preferences/basic-update', views.basic_update, name='basic_update'),
    path('user/preferences/user-update', views.user_update, name='user_update'),
    path('user/preferences/driver-update', views.driver_update, name='driver_update'),
    path('user/preferences/bio-update', views.bio_update, name='bio_update'),
    path('user/preferences/app-update', views.app_update, name='app_update'),
    path('user/preferences/social-update', views.social_update, name='social_update'),
    path('user/preferences/password-update', views.password_update, name='password_update'),




]



