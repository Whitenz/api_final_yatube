from django.urls import include, path
from rest_framework import routers

from .views import PostViewSet

app_name = 'api_v1'

router = routers.DefaultRouter()
router.register(
    r'posts',
    PostViewSet,
    basename='posts'
)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
