from re import L
from rest_framework.views import APIView
from rest_framework.response import Response

from backend.mysql import Mysql
# from .mysql import MySQL

# Create your views here.

class StudentLogin(APIView):
  # def get(self, request):
  #   print("---StudentLogin---")
  #   student_id = str(request.GET.get('student_id', None))
  #   student_password = str(request.GET.get('student_password', None))
  #   print(student_id + ' ' + student_password)
    
  #   sql = Mysql()
  #   result = sql.studentLogin(student_id, student_password)
  #   flag = not not result
    
  #   if flag:
  #     print(result)
  #   else:
  #     print('not found')
    
  #   if flag:
  #     if student_password == result[0][2]:
  #       return Response(dict([('status', 'success')]))
  #     else:
  #       return Response(dict([('status', 'student_password_wrong')]))
  #   else:
  #     return Response(dict([('status', 'student_id_not_found')]))
    
  def post(self, request):
    print("---StudentLogin---")
    student_id = str(request.POST.get('student_id', None))
    student_password = str(request.POST.get('student_password', None))
    print(student_id + ' ' + student_password)
    
    sql = Mysql()
    result = sql.studentLogin(student_id, student_password)
    flag = not not result
    
    if flag:
      print(result)
    else:
      print('not found')
    
    if flag:
      if student_password == result[0][2]:
        return Response(dict([('status', 'success')]))
      else:
        return Response(dict([('status', 'student_password_wrong')]))
    else:
      return Response(dict([('status', 'student_id_not_found')]))
    
class StudentRegister(APIView):
  # def get(self, request):
  #   print("---StudentRegister---")
  #   student_id = str(request.GET.get('student_id', None))
  #   student_password = str(request.GET.get('student_password', None))
  #   student_username = str(request.GET.get('student_username', None))
  #   student_grade = str(request.GET.get('student_grade', None))
  #   student_class = str(request.GET.get('student_class', None))
  #   print(student_id + ' ' + student_password + ' ' + student_username
  #         + ' ' + student_grade + ' ' + student_class)
    
  #   sql = Mysql()
  #   result = sql.studentRegister(student_id, student_password, student_username, 
  #                                student_grade, student_class)
    
  #   if result:
  #     return Response(dict([('status', 'success')]))
  #   else:
  #     return Response(dict([('status', 'fail')]))
    
  def post(self, request):
    print("---StudentRegister---")
    student_id = str(request.POST.get('student_id', None))
    student_password = str(request.POST.get('student_password', None))
    student_username = str(request.POST.get('student_username', None))
    student_grade = str(request.POST.get('student_grade', None))
    student_class = str(request.POST.get('student_class', None))
    print(student_id + ' ' + student_password + ' ' + student_username
          + ' ' + student_grade + ' ' + student_class)
    
    sql = Mysql()
    result = sql.studentRegister(student_id, student_password, student_username, 
                                 student_grade, student_class)
    
    if result:
      return Response(dict([('status', 'success')]))
    else:
      return Response(dict([('status', 'fail')]))
  
class StudentCurriculum(APIView):
  # def get(self, request):
  #   print("---StudentCurriculum---")
  #   student_id = str(request.GET.get('student_id', None))
  #   print(student_id)
  #   sql = Mysql()
  #   result = sql.studentCurriculum(student_id)
  #   courselist = []
  #   print(result)
  #   for item in result:
  #     courselist.append({'course_id':item[0], 'course_name':item[1], 
  #                        'course_intro':item[2], 'course_capacity':item[3], 'course_elected':item[4]})
  #   return Response(dict([("classes", courselist)]))
  
  def post(self, request):
    print("---StudentCurriculum---")
    student_id = str(request.POST.get('student_id', None))
    print(student_id)
    sql = Mysql()
    result = sql.studentCurriculum(student_id)
    courselist = []
    print(result)
    for item in result:
      courselist.append({'course_id':item[0], 'course_name':item[1], 
                         'course_intro':item[2], 'course_capacity':item[3], 'course_elected':item[4]})
    return Response(dict([("classes", courselist)]))
  
class StudentCourseSelection(APIView):
  # def get(self, request):
  #   print("---StudentCourseSelection---")
  #   student_id = str(request.GET.get('student_id', None))
  #   course_id = str(request.GET.get('course_id', None))
  #   sql = Mysql()
  #   result = sql.studentCourseSelection(student_id, course_id)
  #   if result:
  #     return Response(dict([('status', 'success')]))
  #   else:
  #     return Response(dict([('status', 'fail')]))
    
  def post(self, request):
    print("---StudentCourseSelection---")
    student_id = str(request.POST.get('student_id', None))
    course_id = str(request.POST.get('course_id', None))
    sql = Mysql()
    result = sql.studentCourseSelection(student_id, course_id)
    if result:
      return Response(dict([('status', 'success')]))
    else:
      return Response(dict([('status', 'fail')]))
    
class StudentCoursePost(APIView):
  # def get(self, request):
  #   print("---StudentCoursePost---")
  #   student_id = str(request.GET.get('student_id', None))
  #   sql = Mysql()
  #   result = sql.studentCoursePost(student_id)
  #   courselist = []
  #   print(result)
  #   for item in result:
  #     courselist.append({'course_id':item[0], 'course_name':item[1], 
  #                        'course_intro':item[2], 'course_capacity':item[3], 'course_elected':item[4]})
  #   return Response(dict([("classes", courselist)]))
  
  def post(self, request):
    print("---StudentCoursePost---")
    student_id = str(request.POST.get('student_id', None))
    sql = Mysql()
    result = sql.studentCoursePost(student_id)
    courselist = []
    print(result)
    for item in result:
      courselist.append({'course_id':item[0], 'course_name':item[1], 
                         'course_intro':item[2], 'course_capacity':item[3], 'course_elected':item[4]})
    return Response(dict([("classes", courselist)]))
  
class StudentCourseWithdraw(APIView):
  # def get(self, request):
  #   print("---StudentCourseWithdraw---")
  #   student_id = str(request.GET.get('student_id', None))
  #   course_id = str(request.GET.get('course_id', None))
  #   sql = Mysql()
  #   result = sql.studentCourseWithdraw(student_id, course_id)
  #   # if result:
  #   #   return Response(dict(['status', 'success']))
  #   # else:
  #   #   return Response(dict(['status', 'fail']))
  #   return Response(dict([('status', 'success')]))
  
  def post(self, request):
    print("---StudentCourseWithdraw---")
    student_id = str(request.POST.get('student_id', None))
    course_id = str(request.POST.get('course_id', None))
    sql = Mysql()
    result = sql.studentCourseWithdraw(student_id, course_id)
    # if result:
    #   return Response(dict(['status', 'success']))
    # else:
    #   return Response(dict(['status', 'fail']))
    return Response(dict([('status', 'success')]))