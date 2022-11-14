import sys
# sys.path.append("d:\\BUAA_study\\DataBase\\project\\BUAA_DB\\src\\backend")
from mysql import *
from rest_framework.test import APIRequestFactory

mysql = Mysql()
factory = APIRequestFactory()

# r = mysql.changeUserInfo(1, 'wjs','m',21,'---','---')
# print(r)
# print(type(r))
'''
{"userId" : 1, "userName": "wjs", "gender":"f", "age" : 21, "birth":"---", "contact":"456"}
'''
# request = factory.post('/api/changeUserInfo', {"userId" : 1, "userName": "wjs", "gender":"f", "age" : 21, "birth":"---", "contact":"456"})

# r = mysql.userAddTag(1, 'userId=1 add this new tag')
# print(r)
# print(type(r))
'''
{"userId":1, "tagName" : "this is 1 add a tag"}
'''

# r = mysql.getUserInfo(1)
# print(r)
# print(type(r))

# r = mysql.getUserTag(1)
# print(r)
# print(type(r))

# r = mysql.createActivity(1, 'userId=1 created', 'home', '123', '456', '---', '---')
# print(r)
# print(type(r))

# r = mysql.getActivity()
# print(r)
# print(type(r))

