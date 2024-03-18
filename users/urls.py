from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.apps import UsersConfig
from users.views import UsersListView, UsersRetrieveAPIView, UsersUpdateView, UsersDeleteView, UsersCreateView, \
    UsersRegistrationView

app_name = UsersConfig.name

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path('token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),
    path('all/', UsersListView.as_view(), name='all_users'),
    path('<int:pk>/', UsersRetrieveAPIView.as_view(), name='user'),
    path('create/', UsersCreateView.as_view(), name='user_create'),
    path('registrate/', UsersRegistrationView.as_view(), name='user_registrate'),
    path('update/<int:pk>/', UsersUpdateView.as_view(), name='user_update'),
    path('delete/<int:pk>/', UsersDeleteView.as_view(), name='user_delete'),
]
