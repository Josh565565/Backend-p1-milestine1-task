
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

schema_view = get_schema_view(
   openapi.Info(
      title="Backend team 1 python",
      default_version='v1',
      description="This is the backend APIs python team 1 backend",
    #   terms_of_service="",
      contact=openapi.Contact(email=""),
      license=openapi.License(name="Backend team 1 python"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('app.urls')),
    path('api/auth/', include('account.urls')),
    path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
