from rest_framework.routers import DefaultRouter
from django.urls import path
from users.views import UserViewSet, RegisterView

router = DefaultRouter()

router.register(r'', UserViewSet)

urlpatterns = router.urls + [
    path('register/', RegisterView.as_view(), name='register'),
]
