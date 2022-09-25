from django.urls import path
from . import views

urlpatterns = [
    path('studentLogin/',views.StudentLogin.as_view()),
    path('studentRegister/',views.StudentRegister.as_view()),
    path('studentCurriculum/',views.StudentCurriculum.as_view()),
    path('studentCourseSelection/',views.StudentCourseSelection.as_view()),
    path('studentCoursePost/',views.StudentCoursePost.as_view()),
    path('studentCourseWithdraw/',views.StudentCourseWithdraw.as_view()),
]
