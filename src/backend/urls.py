from django.urls import path
from . import views

urlpatterns = [
    path('changeUserInfo',views.changeUserInfo.as_view()),
    path('userAddTag',views.userAddTag.as_view()),
    path('getUserInfo',views.getUserInfo.as_view()),
    path('createActivity',views.createActivity.as_view()),
    path('getActivity',views.getActivity.as_view()),
    path('userLogin', views.userLogin.as_view()),
    path('userRegister', views.userRegister.as_view()),
    path('getHotGroupPic', views.getHotGroupPic.as_view()),
    path('getHotGroupIntro', views.getHotGroupIntro.as_view()),
    path('userAddGroup', views.userAddGroup.as_view()),
    path('getGroupInfo', views.getGroupInfo.as_view()),
    path('userCreatePost', views.userCreatePost.as_view()),
    path('userAddTagToGroup', views.userAddTagToGroup.as_view()),
]
