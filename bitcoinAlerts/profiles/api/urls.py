from django.urls import include, path
from rest_framework.routers import DefaultRouter
from profiles.api import views as pv


router = DefaultRouter()
router.register(r"profiles", pv.ProfileViewSet)

urlpatterns = [
    path("", include(router.urls))
]