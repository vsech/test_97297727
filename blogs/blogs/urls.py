"""
URL configuration for blogs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework_nested.routers import NestedDefaultRouter
from rest_framework import routers
from .views import GroupViewSet, UserViewSet, PostListViewSet, PostDetailViewSet, CommentViewSet, GalleryImageViewSet
from .settings import API_PREFIX
# router = routers.DefaultRouter()
parent_router = routers.DefaultRouter()
parent_router.register(r'users', UserViewSet)
parent_router.register(r'groups', GroupViewSet)
parent_router.register(r'posts', PostListViewSet, basename='posts')
parent_router.register(r'post', PostDetailViewSet, basename='post-detail')
router = NestedDefaultRouter(parent_router, 'posts')
router.register(r'comments', CommentViewSet,
                basename='post-comment')
router.register(r'gallery',
                GalleryImageViewSet, basename='post-gallery')

urlpatterns = [
    path('admin/', admin.site.urls),
    path(API_PREFIX, include(parent_router.urls)),
    path(API_PREFIX, include(router.urls)),
    path(f'{API_PREFIX}auth/',
         include('rest_framework.urls', namespace='rest_framework'))
]
