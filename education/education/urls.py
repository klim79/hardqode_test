"""
URL configuration for education project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from . import settings
from courses.views import LessonViewSet, ProductViewSet, UserProgressViewSet

router = routers.SimpleRouter()
router.register(r'lessons', LessonViewSet, basename='lessonlist')
router_product = routers.SimpleRouter()
router_product.register(r'myproducts', ProductViewSet, basename='myproducts')
router_user_progress = routers.SimpleRouter()
router_user_progress.register(r'userprogress', UserProgressViewSet, basename='userprogress')

#
# from courses.views import UserDataViewSet
#
# router = routers.SimpleRouter()
# router.register(r'userdata', UserDataViewSet, basename='userdata')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/', include(router.urls)),
    path('api/v1/', include(router_product.urls)),
    path('api/v1/', include(router_user_progress.urls)),
    # path('api/v1/', include(router.urls)),
    # path('api/v1/userdatalist/', UserDataViewSet.as_view())
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)