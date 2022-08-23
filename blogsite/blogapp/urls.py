from django.urls import path

from . import views

# ----x--------x-----
urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),

    path('profile/<str:id>/',views.profile,name='profile'), 
    path('create_post/',views.create_post,name='create_post'),

    path('post_view/<str:id>/',views.post_view,name='post_view'),
    

]