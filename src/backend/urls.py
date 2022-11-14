from django.urls import path
from . import views

urlpatterns = [
    path('changeUserInfo',views.changeUserInfo.as_view()),
    path('userAddTag',views.userAddTag.as_view()),
    path('getUserInfo',views.getUserInfo.as_view()),
    path('createActivity',views.createActivity.as_view()),
    path('getActivity',views.getActivity.as_view()),
]
