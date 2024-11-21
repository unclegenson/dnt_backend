from rest_framework.routers import DefaultRouter
from django.urls import path,include
from . import views

router = DefaultRouter()
router.register('signup',views.SignUpUser,basename='signup')
router.register("userinfo",views.UserInfo,basename="userinfo")

urlpatterns = [
    path('',include(router.urls))
]