from django.urls import path
from . import views

urlpatterns = [
    # 个人主页
    path('changeUserInfo',views.changeUserInfo.as_view()),
    path('userAddTag',views.userAddTag.as_view()),
    path('getUserInfo',views.getUserInfo.as_view()),
    path('getUserTag', views.getUserTag.as_view()),
    path('userDeleteTag', views.userDeleteTag.as_view()),
    # 活动页面
    path('createActivity',views.createActivity.as_view()),
    path('getActivity',views.getActivity.as_view()),
    # 漂流瓶主页面
    path('getOneRandomDriftBottleContent',views.getOneRandomDriftBottleContent.as_view()),
    path('getMySendDriftBottles', views.getMySendDriftBottles.as_view()),
    path('getMyReceivedBottleReplys', views.getMyReceivedBottleReplys.as_view()),
    path('agreeWithReply', views.agreeWithReply.as_view()),
    path('getMyRepliedBottles', views.getMyRepliedBottles.as_view()),
    # 登录页面
    path('userLogin', views.userLogin.as_view()),
    #注册页面
    path('userRegister', views.userRegister.as_view()),
    #社区页面
    path('getHotGroupPic', views.getHotGroupPic.as_view()),
    path('getHotGroupIntro', views.getHotGroupIntro.as_view()),
    path('userAddGroup', views.userAddGroup.as_view()),
    path('userDeleteGroup', views.userDeleteGroup.as_view()),
    # 圈子页面
    path('getGroupInfo', views.getGroupInfo.as_view()),
    path('userCreatePost', views.userCreatePost.as_view()),
    path('userAddTagToGroup', views.userAddTagToGroup.as_view()),
    path('userDeletePost', views.userDeletePost.as_view()),
    # 帖子页面
    path('getPostInfo', views.getPostInfo.as_view()),
    path('userLikePost', views.userLikePost.as_view()),
    path('userLikeComment', views.userLikeComment.as_view()),
    path('userCreateComment', views.userCreateComment.as_view()),
    path('userDeleteComment', views.userDeleteComment.as_view()),
    #好友列表
    path('getFriendsList', views.getFriendsList.as_view()),
]
