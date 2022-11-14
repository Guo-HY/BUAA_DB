from re import L
from rest_framework.views import APIView
from rest_framework.response import Response

from backend.mysql import Mysql
# from .mysql import MySQL

# Create your views here.

class changeUserInfo(APIView):
  def post(self, request):
    print("---changeUserInfo---")
    userId = str(request.POST.get('userId', None))
    userName = str(request.POST.get('userName', None))
    gender = str(request.POST.get('gender', None))
    age = str(request.POST.get('age', None))
    birth = str(request.POST.get('birth', None))
    contact = str(request.POST.get('contact', None))
    print("userId=%s,userName=%s,gender=%s,age=%s,birth=%s,contact=%s"%
          (str(userId),str(userName),str(gender),str(age),str(birth),str(contact)))
    sql = Mysql()
    result = sql.changeUserInfo(userId, userName, gender, age, birth, contact)
    if result:
      return Response(dict([('status', 'success')]))
    else:
      return Response(dict([('status', 'fail')]))
    
class userAddTag(APIView):
  def post(self, request):
    print("---userAddTag---")
    userId = str(request.POST.get('userId', None))
    tagName = str(request.POST.get('tagName', None))
    sql = Mysql()
    print("userId=%s,tagName=%s"%(str(userId), str(tagName)))
    result = sql.userAddTag(userId, tagName)
    if result:
      return Response(dict([('status', 'success')]))
    else:
      return Response(dict([('status', 'fail')]))
    
class getUserInfo(APIView):
  def post(self, request):
    print("---getUserInfo---")
    userId = str(request.POST.get('userId', None))
    sql = Mysql()
    tags = []
    result = sql.getUserTag(userId)
    for item in result:
      tags.append(item[0])
    
    result = sql.getUserInfo(userId)
    r = {'userName':result[0][1], 'gender':result[0][5], 'age':result[0][6], 'birth':result[0][7],'contact':result[0][4], 'dynamicTags':tags}
    
    return Response(r)
  
  
class createActivity(APIView):
  def post(self, request):
    print("---createActivity---")
    userId = str(request.POST.get('userId', None))
    name = str(request.POST.get('name', None))
    region = str(request.POST.get('region', None))
    beginDate = str(request.POST.get('beginDate', None))
    endDate = str(request.POST.get('endDate', None))
    desc = str(request.POST.get('desc', None))
    activityNature = str(request.POST.get('activityNature', None))
    sql = Mysql()
    r = sql.createActivity(userId, name, region, beginDate, endDate, desc, activityNature)
    if r:
      return Response(dict([('status', 'success')]))
    else:
      return Response(dict([('status', 'fail')]))
    
class getActivity(APIView):
  def post(self, request):
    print("---getActivity---")
    sql = Mysql()
    result = sql.getActivity()
    acts = []
    for item in result:
      acts.append({'name':item[1], 'region':item[5], 'beginDate':item[3], 'endDate':item[4], 'desc':item[2], 'activitieNature':item[6]})
    
    return Response({'activities':acts})
  
