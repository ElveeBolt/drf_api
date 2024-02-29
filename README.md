# DRF API
Example of an application using the approach to API version management with Django Rest Framework.

## Concept
In this approach, API v1 and v2 use a common model, but have their own serializer views and URLs.

Among the disadvantages, it is worth noting the following:
- The necessity to duplicate folders with versions for each application.
- There is no possibility to use different models in various versions (though I do not consider this critical, as often the changes are related to serializers).

## Routers
Each application exposes router which is DRF SimpleRouter

```python
router = SimpleRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
```

The main **urls.py** is created based on **urls_v1.py** and **urls_v2.py**, each of which creates an instance of DefaultRouter and extends it using application routers.

```python
from apps.user.v1.urls import router as user_router

app_name = 'api_v1'

router = DefaultRouter()
router.registry.extend(user_router.registry)

urlpatterns = [
    path('', include(router.urls)),
    path('schema/', SpectacularAPIView.as_view(api_version='v1'), name='schema'),
    path('doc/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),
]
```

```python
urlpatterns = [
    path('api/v1/', include('api.urls_v1', namespace='v1')),
    path('api/v2/', include('api.urls_v2', namespace='v2')),

    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
```

## DRF documentation
Versioning is accomplished using the [drf-spectacular](https://drf-spectacular.readthedocs.io/en/latest/index.html "drf-spectacular") module. In addition, schema generation for documenting this API is implemented here. Documentation for each API version is available at a link: `/api/v1/doc/`

## Author
Developed and maintained by [ElveeBolt](https://github.com/ElveeBolt).

Thanks to everybody that has contributed pull requests, ideas, issues, comments and kind words.