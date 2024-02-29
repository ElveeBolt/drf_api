from rest_framework.routers import SimpleRouter

from .views import UserViewSet, GroupViewSet

router = SimpleRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
