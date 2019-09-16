from django.urls import include, path
from rest_framework.routers import DefaultRouter
from alerts.api import views as av


router = DefaultRouter()
router.register(r"alerts", av.AlertViewSet)

urlpatterns = [
    path("", include(router.urls))
]