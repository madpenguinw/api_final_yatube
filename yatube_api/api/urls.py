from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import GroupViewSet, PostViewSet, CommentViewSet, FollowViewSet


router_v1 = DefaultRouter()
router_v1.register('groups', GroupViewSet)
router_v1.register('posts', PostViewSet)
router_v1.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    path('v1/follow/', FollowViewSet.as_view(), name='follow'),
]
