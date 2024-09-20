from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path, reverse_lazy
from django.views.generic.base import RedirectView
# from drf_yasg import openapi
# from drf_yasg.views import get_schema_view
# from rest_framework import permissions
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

from .users.views import UserCreateViewSet, UserViewSet
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

# schema_view = get_schema_view(
#     openapi.Info(
#         title="Chapiana API",
#         default_version="v1",
#         description="An API for contacts developed majorly using Python's framework called Django Rest Framework.",
#         contact=openapi.Contact(email="bikocodes@gmail.com"),
#         license=openapi.License(name="MIT License"),
#     ),
#     public=True,
#     permission_classes=[permissions.AllowAny],
# )

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="user")
router.register(r"users", UserCreateViewSet, basename="create_user")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api-token-auth/", views.obtain_auth_token),
    
    path("token/obtain-pair/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),

    path("accounts/", include("rest_framework.urls", namespace="rest_framework")),
    path("contacts/", include("src.contacts.urls"), name="contacts_app"),
    
    # path("", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    # path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI
    path('api/schema/swaggger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc', SpectacularRedocView.as_view(url_name='schema'), 'redoc'),

    re_path(r"^$", RedirectView.as_view(url=reverse_lazy("api-root"), permanent=False)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
