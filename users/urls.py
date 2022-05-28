from django.urls import path

from users.views import login_api, get_user_data, register_api

from knox import views as knox_views

urlpatterns = [
    path('login/', login_api),
    path('user-data/', get_user_data),
    path('register/', register_api),
    path('logout/', knox_views.LogoutView.as_view()),
    path('logout-all/', knox_views.LogoutAllView.as_view()),
]
