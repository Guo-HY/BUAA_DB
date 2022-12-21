from re import L
from rest_framework.views import APIView, View
from rest_framework.response import Response  
from django.http import HttpResponse
from backend.mysql import Mysql
import random
from buaa_db.settings import MEDIA_ROOT
from animegan2.test import animegan2

# Create your views here.

class changeUserInfo(APIView):
  def post(self, request):
    print("---changeUserInfo---")
    userId = str(request.POST.get('userId', None))
    userName = str(request.POST.get('userName', None))
    gender = str(request.POST.get('gender', None))
    age = str(request.POST.get('age', None))
    address = str(request.POST.get('address', None))
    contact = str(request.POST.get('contact', None))
    print("userId=%s,userName=%s,gender=%s,age=%s,address=%s,contact=%s"%
          (str(userId),str(userName),str(gender),str(age),str(address),str(contact)))
    sql = Mysql()
    result = sql.changeUserInfo(userId, userName, contact, gender, age, address)
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

class getUserTag(APIView):
  def post(self, request):
    print("---getUserTag---")
    userId = str(request.POST.get('userId', None))
    sql = Mysql()
    tags = []
    result = sql.getUserTag(userId)
    for item in result:
      tags.append(item[0])
    return Response({'dynamicTags':tags})
  
class userDeleteTag(APIView):
  def post(self, request):
    print("---userDeleteTag---")
    userId = str(request.POST.get('userId', None))
    tagName = str(request.POST.get('tagName', None))
    sql = Mysql()
    sql.userDeleteTag(userId, tagName)
    return Response({'status' : 'success'})
    

class getUserInfo(APIView):
  def post(self, request):
    print("---getUserInfo---")
    userId = str(request.POST.get('userId', None))
    sql = Mysql()
    result = sql.getUserInfo(userId)
    r = {'userName':result[0][1], 'gender':result[0][5], 'age':result[0][6], 'address':result[0][7],'contact':result[0][4]}  
    return Response(r)

class createActivity(APIView):
  def post(self, request):
    print("---createActivity---")
    name = str(request.POST.get('name', None))
    desc = str(request.POST.get('desc', None))
    beginDate = str(request.POST.get('beginDate', None))
    endDate = str(request.POST.get('endDate', None))
    region = str(request.POST.get('region', None))
    activityNature = str(request.POST.get('activityNature', None))
    userId = str(request.POST.get('userId', None))
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
      acts.append({'name':item[1], 'desc':item[2], 'beginDate':item[3], 'endDate':item[4], 'region':item[5], 'activityNature':item[6]})
    
    return Response({'activities':acts})
  
class userLogin(APIView):
  def post(self, request):
    print("---userLogin---")
    name = str(request.POST.get('name', None))
    password = str(request.POST.get('password', None))
    sql = Mysql()
    result = sql.userLogin(name)
    if len(result) != 1:
      return Response({'status':"not_found", "userId" : "-1"})
    password_in_sql = str(result[0][2])
    if password != password_in_sql:
      return Response({'status':"password_wrong", "userId" : "-1"})
    return Response({'status':"success", "userId" : str(result[0][0])})
  
class userRegister(APIView):
  def post(self, request):
    print("---userRegister---")
    name = str(request.POST.get('name', None))
    password = str(request.POST.get('password', None))
    contact = str(request.POST.get('contact', None))
    gender = str(request.POST.get('gender', None))
    age = str(request.POST.get('age', None))
    address = str(request.POST.get('address', None))
    pic = request.FILES.get('pic', None)
    sql = Mysql()
    result = sql.userRegister(name, password, contact, gender, age, address)
    if result=="fail":
      return Response({'status' : result})
    userId = sql.getUserIdByName(name)[0][0]
    save_dir = '%s'%(MEDIA_ROOT)
    image_name = '%s.jpg'%(userId)
    save_path = '%s\\%s.jpg'%(MEDIA_ROOT, userId)
    sql_save_path = 'media/%s.jpg'%(userId)
    with open(save_path, 'wb') as f:
      for content in pic.chunks():
        f.write(content)
    result = sql.addUserProfilePic(userId, str(sql_save_path))
    print("run animegan2")
    animegan2(input_dir=save_dir, output_dir=save_dir, image_name=image_name)
    
    return Response({'status' : result})
  
# class getHotGroupPic(APIView):
#   def post(self, request):
#     print("---getHotGroupPic---")
#     userId = str(request.POST.get('userId', None))
#     sql = Mysql()
#     result = sql.getAllGroup()
#     groups = []
#     for item in result:
#       groups.append({'groupId' : item[0], 'pic' : '---', 'name' : item[2]})
#     return Response({'groups' : groups})
  
class getHotGroupIntro(APIView):
  def post(self, request):
    print("---getHotGroupIntro---")
    userId = str(request.POST.get('userId', None))
    sql = Mysql()
    sql_groups = sql.getAllGroup()
    groups = []
    for group in sql_groups:
      groupId = group[0]
      tags = []
      sql_tags = sql.getGroupTags(groupId)
      for tag in sql_tags:
        tags.append(tag[0])
      groups.append({'groupId':groupId, 'name':group[2], 'desc':group[3],'tags':tags})
    
    sql_hotpics = []
    num = 0
    for group in sql_groups:
      sql_hotpics.append({'groupId' : group[0],  'name' : group[2]})
      num = num + 1
      if num == 3:
        break
    
    return Response({'groups' : groups, 'hotpics' : sql_hotpics})

class userAddGroup(APIView):
  def post(self, request):
    print("---userAddGroup---")
    userId = str(request.POST.get('userId', None))
    group_name = str(request.POST.get('group_name', None))
    group_desc = str(request.POST.get('group_desc', None))
    print("userid"+userId+"name" + group_name + "desc" + group_desc)
    # pic = request.FILES.get('pic', None)
    
    # save_dir = '%s'%(MEDIA_ROOT)
    # image_name = 'group_%s.jpg'%(group_name)
    # save_path = save_dir + '\\' + image_name
    # sql_save_path = 'media/' + image_name
    # with open(save_path, 'wb') as f:
    #   for content in pic.chunks():
    #     f.write(content)
    
    sql = Mysql()
    # result = sql.userAddGroup(userId, group_name, group_desc, sql_save_path)
    result = sql.userAddGroup(userId, group_name, group_desc)
    return Response({'status' : result})
  
class userDeleteGroup(APIView):
  def post(self, request):
    print("---userDeleteGroup---")
    userId = str(request.POST.get('userId', None))
    groupId = str(request.POST.get('groupId', None))
    sql = Mysql()
    result = sql.userDeleteGroup(userId, groupId)
    return Response({'status' : result})

class getGroupInfo(APIView):
  def post(self, request):
    print("---getGroupInfo---")
    groupId = str(request.POST.get('groupId', None))
    sql = Mysql()
    sql_group = sql.getSingleGroup(groupId)[0]
    create_user_name = sql.getUserInfo(sql_group[4])[0][1]
    group_create_user_pic = sql.previewUserProfilePic(sql_group[4])[0][0]
    sql_tags = sql.getGroupTags(groupId)
    tags = []
    for item in sql_tags:
      tags.append(item[0])
    sql_posts = sql.getGroupPosts(groupId)
    posts = []
    for item in sql_posts:
      post_create_user_name = sql.getUserInfo(item[6])[0][1]
      post_create_user_pic = sql.previewUserProfilePic(item[6])[0][0]
      posts.append({'post_id':item[0], 'post_name':item[1],'content':item[2],
                    'post_time':item[3],'comment_num':item[4],'likes_num':item[5],
                    'create_user_name':post_create_user_name, 'create_user_pic' : post_create_user_pic})

    return Response({'group_name':sql_group[2],'group_desc':sql_group[3],
                     'post_num':sql_group[1],'create_user_name':create_user_name, 
                     'create_user_pic' : group_create_user_pic,
                     'tags':tags, 'posts':posts})
    
class userCreatePost(APIView):
  def post(self, request):
    print("---userCreatePost---")
    userId = str(request.POST.get('userId', None))
    groupId = str(request.POST.get('groupId', None))
    post_name = str(request.POST.get('post_name', None))
    content = str(request.POST.get('content', None))
    post_time = str(request.POST.get('post_time', None))
    sql = Mysql()
    result = sql.userCreatePost(userId, groupId, post_name, content, post_time)
    return Response({'status':result})
  
class userDeletePost(APIView):
  def post(self, request):
    print("---userDeletePost---")
    userId = str(request.POST.get('userId', None))
    postId = str(request.POST.get('postId', None))
    sql = Mysql()
    result = sql.userDeletePost(userId, postId)
    return Response({'status':result})
    
  
class userAddTagToGroup(APIView):
  def post(self, request):
    print("---userAddTagToGroup---")
    userId = str(request.POST.get('userId', None))
    groupId = str(request.POST.get('groupId', None))
    tagName = str(request.POST.get('tagName', None))
    sql = Mysql()
    tagId = sql.addTag(tagName)
    if int(tagId) == -1:
      return Response({'status':'fail'})
    result = sql.addGroupTag(groupId, tagId)
    return Response({'status':result})
  
class getOneRandomDriftBottleContent(APIView):
  def post(self, request):
    print("---getOneRandomDriftBottleContent---")
    userId = str(request.POST.get('userId', None))
    sql = Mysql()
    allBottles = sql.getAllBottle()
    randPtr = 0
    while True:
      randPtr = random.randint(0, len(allBottles) - 1)
      if str(allBottles[randPtr][2]) != userId:
        break
    
    content = allBottles[randPtr][1]
    return Response({'content' : content})
  
class getMySendDriftBottles(APIView):
  def post(self, request):
    print("---getMySendDriftBottles---")
    userId = str(request.POST.get('userId', None))
    sql = Mysql()
    sql_bottles = sql.getUserSendBottle(userId)
    bottles = []
    for item in sql_bottles:
      bottles.append({'content' : item[1]})
    
    return Response({'bottles' : bottles})
  
class getMyReceivedBottleReplys(APIView):
  def post(self, request):
    print("---getMyReceivedBottleReplys---")
    userId = str(request.POST.get('userId', None))
    sql = Mysql()
    sql_bottlesAndReplys = sql.getMyReceivedBottleReplys(userId)
    bottlesAndReplys = []
    for item in sql_bottlesAndReplys:
      bottlesAndReplys.append({'content' : item[0], 'reply' : item[1], 'replyUserId' : item[2]})
      
    return Response({'bottlesAndReplys' : bottlesAndReplys})
  
class agreeWithReply(APIView):
  def post(self, request):
    print("---agreeWithReply---")
    userId = str(request.POST.get('userId', None))
    replyUserId = str(request.POST.get('replyUserId', None))
    sql = Mysql()
    r = sql.addUserFriend(userId, replyUserId)
    print(r)
    return Response({'status' : 'success'})
  
class getMyRepliedBottles(APIView):
  def post(self, request):
    print("---getMyRepliedBottles---")
    userId = str(request.POST.get('userId', None))
    sql = Mysql()
    sql_bottles = sql.getMyRepliedBottles(userId)
    bottles = []
    for item in sql_bottles:
      bottles.append({'content' : item[0], 'myReply' : item[1]})
    
    return Response({'bottles' : bottles})
  
class sendText(APIView):
  def post(self, request):
    print("---sendText---")
    userId = str(request.POST.get('userId', None))
    content = str(request.POST.get('content', None))
    sql = Mysql()
    result = sql.sendText(userId, content)
    return Response({'status' : result})
  
class sendReplyText(APIView):
  def post(self, request):
    print("---sendReplyText---")
    userId = str(request.POST.get('userId', None))
    bottleId = str(request.POST.get('bottleId', None))
    content = str(request.POST.get('content', None))
    sql = Mysql()
    result = sql.sendReplyText(userId, bottleId, content)
    return Response({'status' : result})

class getPostInfo(APIView):
  def post(self, request):
    print("---getPostInfo---")
    postId = str(request.POST.get('postId', None))
    sql = Mysql()
    postinfo = sql.getOnePost(postId)
    sql_comments = sql.getPostComments(postId)
    create_user_name = sql.getUserInfo(postinfo[0][6])[0][1]
    post_create_user_pic = sql.previewUserProfilePic(postinfo[0][6])[0][0]
    comments = []
    for item in sql_comments:
      comment_user_pic = sql.previewUserProfilePic(item[4])[0][0]
      comments.append({'comment_id' : item[0], 'content' : item[1], 
                       'comment_time' : item[2], 'likes_num' : item[3], 
                       'comment_user_id' : item[4], 'comment_user_pic' : comment_user_pic})
    postinfo = postinfo[0]
    return Response({'post_name' : postinfo[1], 'content' : postinfo[2], 
                     'post_time' : postinfo[3], 'comment_num' : postinfo[4],
                     'likes_num' : postinfo[5], 'create_user_name' : create_user_name,
                     'create_user_pic' : post_create_user_pic,
                     'comments' : comments})
  
class userLikePost(APIView):
  def post(self, request):
    print("---userLikePost---")
    userId = str(request.POST.get('userId', None))
    postId = str(request.POST.get('postId', None))
    sql = Mysql()
    r = sql.userLikePost(userId, postId)
    print(r)
    return Response({'status' : 'success'})
  
class userLikeComment(APIView):
  def post(self, request):
    print("---userLikePost---")
    userId = str(request.POST.get('userId', None))
    commentId = str(request.POST.get('commentId', None))
    sql = Mysql()
    r = sql.userLikeComment(userId, commentId)
    print(r)
    return Response({'status' : 'success'})


class userCreateComment(APIView):
  def post(self, request):
    print("---userCreateComment---")
    userId = str(request.POST.get('userId', None))
    postId = str(request.POST.get('postId', None))
    content = str(request.POST.get('content', None))
    comment_time = str(request.POST.get('comment_time', None))
    sql = Mysql()
    r = sql.userCreateComment(userId, postId, content, comment_time)
    print(r)
    return Response({'status' : 'success'})
  
class userDeleteComment(APIView):
  def post(self, request):
    print("---userDeleteComment---")
    userId = str(request.POST.get('userId', None))
    commentId = str(request.POST.get('commentId', None))
    sql = Mysql()
    result = sql.userDeleteComment(userId, commentId)
    return Response({'status' : result})
  
class getFriendsList(APIView):
  def post(self, request):
    print("---getFriendsList---")
    userId = str(request.POST.get('userId', None))
    sql = Mysql()
    result = sql.getFriendsList(userId)
    friends = []
    for item in result:
      friends.append({'userId': item[0], 'userName' : item[1]})
    
    return Response({'friends' : friends})
  
class uploadUserProfilePic(APIView):
  def post(self, request):
    print("---uploadUserProfilePic---")
    pic = request.FILES.get('pic', None)
    # print(type(pic))
    userId = request.POST.get('userId', None)
    save_dir = '%s'%(MEDIA_ROOT)
    image_name = '%s.jpg'%(userId)
    save_path = '%s\\%s.jpg'%(MEDIA_ROOT, userId)
    sql_save_path = 'media/%s.jpg'%(userId)
    with open(save_path, 'wb') as f:
      for content in pic.chunks():
        f.write(content)
    sql = Mysql()
    result = sql.addUserProfilePic(userId, str(sql_save_path))
    # animegan2
    print("run animegan2")
    # from animegan2.test import animegan2
    animegan2(input_dir=save_dir, output_dir=save_dir, image_name=image_name)
    # with open(save_path, 'rb') as f:
      # img = f.read()
    # return HttpResponse(img, content_type="image/jpg")
    return Response({'status' : result})
  
class previewUserProfilePic(APIView):
  def post(self, request):
    print("---previewUserProfilePic---")
    userId = request.POST.get('userId', None)
    sql = Mysql()
    result = sql.previewUserProfilePic(userId)
    if len(result) == 0:
      print("len(result)=0")
      return Response({'pic_path' : 'fail'})
    return Response({'pic_path' : result[0][0]})