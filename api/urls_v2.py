from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView

from apps.user.v2.urls import router as user_router

app_name = 'api_v2'

router = DefaultRouter()
router.registry.extend(user_router.registry)

urlpatterns = [
    path('', include(router.urls)),
    path('schema/', SpectacularAPIView.as_view(api_version='v2'), name='schema'),
    path('doc/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),
]
