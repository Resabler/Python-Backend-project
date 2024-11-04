from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns=[
    path('admin/', admin.site.urls),
    path('api/employees/', views.Listcreate.as_view()),
        # For listing and creating employees
    path('api/employees/<int:id>/', views.Retrieveupdatedelete.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
