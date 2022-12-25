import pymysql
import sys
# sys.path.append("d:\\BUAA_study\\DataBase\\project\\BUAA_DB\\src")
# print(sys.path)
# exit(1)
from buaa_db.settings import DATABASE_KEY, DATA_BASE_NAME

class Mysql:
  
  def connectDataBase(self):
    connect = pymysql.connect(host='localhost',
                              user='root',
                              password=DATABASE_KEY, 
                              database=DATA_BASE_NAME)
    cursor = connect.cursor()
    return connect, cursor
  
  def closeDataBase(self,connect, cursor):
    connect.close()
    cursor.close()
  

  def changeUserInfo(self, userId, userName,contact, gender, age, address):
    connect, cursor = self.connectDataBase()
    
    sql = "SELECT * FROM user WHERE user_id=%s"
    cursor.execute(sql, [userId])
    
    sql = "UPDATE user SET name=%s, gender=%s, age=%s, address=%s, contact=%s WHERE user_id=%s"
    try:
      cursor.execute(sql, [userName, gender, age, address, contact, userId])
      connect.commit()
    except Exception as e:
      connect.rollback()
      print("error in changeUserInfo : can't update info")
      self.closeDataBase(connect, cursor)
      return False
    self.closeDataBase(connect, cursor)
    return True
    
  def addTag(self, tagName):
    connect, cursor = self.connectDataBase()
    sql = "SELECT * FROM tag WHERE tag_name=%s"
    cursor.execute(sql, [tagName])
    result = cursor.fetchall()
    r = str(-1)
    if len(result) == 0:
      insert_sql = "INSERT INTO tag(tag_name) VALUES(%s)"
      try:
        cursor.execute(insert_sql, [tagName])
        connect.commit()
      except Exception as e:
        connect.rollback()
        print(e)
        self.closeDataBase(connect, cursor)
        return r
    cursor.execute(sql, [tagName])
    result = cursor.fetchall()
    r = str(result[0][0])
    self.closeDataBase(connect, cursor)
    return r
  
  # 在tag表里首先查找是否存在tag，不存在就新建
  def userAddTag(self, userId, tagName):
    connect, cursor = self.connectDataBase()
    
    sql = "SELECT * FROM tag WHERE tag_name=%s"
    cursor.execute(sql, [tagName])
    result = cursor.fetchall()
    
    if len(result) == 0:
      insert_sql = "INSERT INTO tag(tag_name) VALUES(%s)"
      try:
        cursor.execute(insert_sql, [tagName])
        connect.commit()
      except Exception as e:
        connect.rollback()
        print("error in userAddTag : can't add tag")
        self.closeDataBase(connect, cursor)
        return False
      cursor.execute(sql, [tagName])
      result = cursor.fetchall()
    
    if len(result) != 1:
      print("error in userAddTag : result != 1")
      self.closeDataBase(connect, cursor)
      return False
    
    tagId = result[0][0]
    sql = "INSERT INTO user_tag(user_id, tag_id) VALUES(%s, %s)"
    try:
      cursor.execute(sql, [userId, tagId])
      connect.commit()
    except Exception as e:
      connect.rollback()
      print("error in userAddTag : can't insert user_tag")
      self.closeDataBase(connect, cursor)
      return False
    self.closeDataBase(connect, cursor)
    return True
  
  def userDeleteTag(self, userId, tagName):
    connect, cursor = self.connectDataBase()
    sql = "SELECT tag_id FROM tag WHERE tag_name=%s"
    cursor.execute(sql, [tagName])
    tagId = cursor.fetchall()[0]
    result = "success"
    try:
      sql = "DELETE FROM user_tag WHERE user_id=%s AND tag_id=%s"
      cursor.execute(sql, [userId, tagId])
      connect.commit()
    except Exception as e:
      connect.rollback()
      print(e)
      result = "fail"
    self.closeDataBase(connect, cursor)
    return result
  
  def getUserInfo(self, userId):
    connect, cursor = self.connectDataBase()
    sql = "SELECT * FROM user WHERE user_id=%s"
    cursor.execute(sql, [userId])
    result = cursor.fetchall()
    self.closeDataBase(connect, cursor)
    return result
  
  def getUserTag(self, userId):
    connect, cursor = self.connectDataBase()
    sql = "SELECT tag_name FROM tag WHERE tag_id IN (SELECT tag_id FROM user_tag WHERE user_id=%s)"
    cursor.execute(sql, [userId])
    result = cursor.fetchall()
    self.closeDataBase(connect, cursor)
    return result
  
  
  def createActivity(self, userId, name, region, beginDate, endDate, desc, activityNature):
    connect, cursor = self.connectDataBase()
    sql = "INSERT INTO activity(name, summary, begin_time, end_time, location, activity_nature, user_id) \
            VALUES(%s, %s, %s, %s, %s, %s, %s)"
    
    try:
      cursor.execute(sql, [name, desc, beginDate, endDate, region, activityNature, userId])
      connect.commit()
    except Exception as e:
      connect.rollback()
      print(e)
      self.closeDataBase(connect, cursor)
      return False
    self.closeDataBase(connect, cursor)
    return True
      
  def getActivity(self):
    connect, cursor = self.connectDataBase()
    sql = "SELECT * FROM activity"
    cursor.execute(sql)
    result = cursor.fetchall()
    self.closeDataBase(connect, cursor)
    return result
  
  def userLogin(self, name):
    connect, cursor = self.connectDataBase()
    sql = "SELECT * FROM user WHERE name=%s"
    cursor.execute(sql, [name])
    result = cursor.fetchall()
    self.closeDataBase(connect, cursor)
    return result
  
  def userRegister(self, name, password, contact, gender, age, address):
    connect, cursor = self.connectDataBase()
    sql = "SELECT * FROM user WHERE name=%s"
    cursor.execute(sql, [name])
    result = cursor.fetchall()
    if len(result) != 0:
      self.closeDataBase(connect, cursor)
      return "name has an account registered. please log in."
    sql = "INSERT INTO user(name, password, head_portrait, contact, gender, age, address)\
      VALUES(%s, %s, %s, %s, %s, %s, %s)"
    
    try:
      cursor.execute(sql, [name, password, "---", contact, gender, age, address])
      connect.commit()
    except Exception as e:
      connect.rollback()
      print(e)
      self.closeDataBase(connect, cursor)
      return "unknown_fail"
    self.closeDataBase(connect, cursor)
    return "success"
  
  def getAllGroup(self):
    connect, cursor = self.connectDataBase()
    sql = "SELECT * FROM `group`"
    cursor.execute(sql)
    result = cursor.fetchall()
    self.closeDataBase(connect, cursor)
    return result
  
  def getAllUserId(self):
    connect, cursor = self.connectDataBase()
    sql = "select `user_id` from `user`"
    cursor.execute(sql)
    result = cursor.fetchall()
    self.closeDataBase(connect, cursor)
    return result
  
  def getAllGroupId(self):
    connect, cursor = self.connectDataBase()
    sql = "select `group_id` from `group`"
    cursor.execute(sql)
    result = cursor.fetchall()
    self.closeDataBase(connect, cursor)
    return result
  
  def getAllUserGroupScore(self):
    connect, cursor = self.connectDataBase()
    sql = "SELECT * FROM  `user_group_score`"
    cursor.execute(sql)
    result = cursor.fetchall()
    self.closeDataBase(connect, cursor)
    return result
  
  def getOneUserGroupScore(self, userId, groupId):
    connect, cursor = self.connectDataBase()
    sql = "SELECT `score` from `user_group_score` where user_id=%s and group_id=%s"
    cursor.execute(sql, [userId, groupId])
    result = cursor.fetchall()
    self.closeDataBase(connect, cursor)
    return result
  
  def getGroupTags(self, groupId):
    connect, cursor = self.connectDataBase()
    sql = "SELECT tag_name FROM tag WHERE tag_id IN\
      (SELECT tag_id FROM group_tag WHERE group_id=%s)"
    cursor.execute(sql, [groupId])
    result = cursor.fetchall()
    self.closeDataBase(connect, cursor)
    return result
    
  def userAddGroup(self, userId, group_name, group_desc):
    connect, cursor = self.connectDataBase()
    result = "success"
    sql = "INSERT INTO `group`(post_num, group_name, group_desc, user_id)\
      VALUES(%s, %s, %s, %s)"
    try:
      cursor.execute(sql, ['0', group_name, group_desc, userId])
      connect.commit()
    except Exception as e:
      connect.rollback()
      print(e)
      result = "fail"
    self.closeDataBase(connect, cursor)
    return result
  
  def userDeleteGroup(self, userId, groupId):
    connect, cursor = self.connectDataBase()
    result = "success"
    sql = "SELECT user_id FROM `group` WHERE group_id=%s"
    cursor.execute(sql, [groupId])
    r = cursor.fetchall()
    if len(r) == 0:
      self.closeDataBase(connect, cursor)
      return "fail"
    create_user_id = r[0][0]
    # print("create_user_id=" + str(create_user_id))
    if str(userId) != str(create_user_id):
      self.closeDataBase(connect, cursor)
      return "fail"
    sql = "DELETE FROM `group` WHERE group_id=%s"
    try:
      cursor.execute(sql, [groupId])
      connect.commit()
    except Exception as e:
      connect.rollback()
      print(e)
      result = "fail"
    self.closeDataBase(connect, cursor)
    return result
  
  def getSingleGroup(self, groupId):
    connect, cursor = self.connectDataBase()
    sql = "SELECT * FROM `group` WHERE group_id=%s"
    cursor.execute(sql, [groupId])
    result = cursor.fetchall()
    self.closeDataBase(connect, cursor)
    return result
    
  
  def getGroupPosts(self, groupId):
    connect, cursor = self.connectDataBase()
    sql = "SELECT * FROM post WHERE group_id=%s"
    cursor.execute(sql, [groupId])
    result = cursor.fetchall()
    self.closeDataBase(connect, cursor)
    return result
  
  def userCreatePost(self, userId, groupId, post_name, content, post_time):
    connect, cursor = self.connectDataBase()
    sql = "INSERT INTO post(name, content, post_time, comment_num, likes_num, user_id, group_id)\
      VALUES(%s, %s, %s, %s, %s, %s, %s)"
    result = "success"
    try:
      cursor.execute(sql, [post_name, content, post_time, '0', '0', userId, groupId])
      connect.commit()
    except Exception as e:
      connect.rollback()
      print(e)
      result = "fail"
    self.closeDataBase(connect, cursor)
    return result
  
  def userDeletePost(self, userId, postId):
    connect, cursor = self.connectDataBase()
    result = "success"
    sql = "SELECT user_id, group_id FROM post WHERE post_id=%s"
    cursor.execute(sql, [postId])
    r = cursor.fetchall()
    if len(r) == 0:
      self.closeDataBase(connect, cursor)
      return "fail"
    create_user_id = r[0][0]
    groupId = r[0][1]
    if str(userId) != str(create_user_id):
      self.closeDataBase(connect, cursor)
      return "fail"
    sql = "DELETE FROM post WHERE post_id=%s"
    try:
      cursor.execute(sql, [postId])
      connect.commit()
    except Exception as e:
      connect.rollback()
      print(e)
      result = "fail"
    sql = "update `group` set `post_num`=`post_num` - 1 where `group`.`group_id`=%s"
    try:
      cursor.execute(sql, [groupId])
      connect.commit()
    except Exception as e:
      connect.rollback()
      print(e)
      result = "fail"
    self.closeDataBase(connect, cursor)
    return result
  
  def addGroupTag(self, groupId, tagId):
    connect, cursor = self.connectDataBase()
    sql = "SELECT * FROM group_tag WHERE group_id=%s AND tag_id=%s"
    cursor.execute(sql,[groupId, tagId])
    result = cursor.fetchall()
    r = "success"
    if len(result) != 0:
      return r
    
    sql = "INSERT group_tag(group_id, tag_id) VALUES(%s, %s)"
    try:
      cursor.execute(sql, [groupId, tagId])
      connect.commit()
    except Exception as e:
      connect.rollback()
      print(e)
      r = "fail"
    self.closeDataBase(connect, cursor)
    return r
  
  def getAllBottle(self):
    connect, cursor = self.connectDataBase()
    sql = "SELECT * FROM bottle"
    cursor.execute(sql)
    result = cursor.fetchall()
    self.closeDataBase(connect, cursor)
    return result

  def getUserSendBottle(self, userId):
    connect, cursor = self.connectDataBase()
    sql = "SELECT * FROM bottle WHERE user_id=%s"
    cursor.execute(sql, [userId])
    result = cursor.fetchall()
    self.closeDataBase(connect, cursor)
    return result
  
  def getMyReceivedBottleReplys(self, userId):
    connect, cursor = self.connectDataBase()
    sql = "SELECT content, reply, bottle_reply.user_id FROM bottle, bottle_reply\
            WHERE bottle.bottle_id=bottle_reply.bottle_id AND bottle.user_id=%s"
    
    cursor.execute(sql, [userId])
    result = cursor.fetchall()
    self.closeDataBase(connect, cursor)
    return result
  
  def addUserFriend(self, user1_id, user2_id):
    connect, cursor = self.connectDataBase()
    sql = "INSERT user_user(user1_id, user2_id) VALUES(%s, %s)"
    r = "success"
    try:
      cursor.execute(sql, [user1_id, user2_id])
      connect.commit()
    except Exception as e:
      connect.rollback()
      print(e)
      r = "fail"
    self.closeDataBase(connect, cursor)
    return r
  
  def getMyRepliedBottles(self, userId):
    connect, cursor = self.connectDataBase()
    sql = "SELECT content, reply FROM bottle, bottle_reply \
          WHERE bottle.bottle_id=bottle_reply.bottle_id AND bottle_reply.user_id=%s"
    
    cursor.execute(sql, [userId])
    result = cursor.fetchall()
    self.closeDataBase(connect, cursor)
    return result
  
  def sendText(self, userId, content):
    connect, cursor = self.connectDataBase()
    sql = "INSERT bottle(user_id, content) VALUES(%s, %s)"
    r = "success"
    try:
      cursor.execute(sql, [userId, content])
      connect.commit()
    except Exception as e:
      connect.rollback()
      print(e)
      r = "fail"
    self.closeDataBase(connect, cursor)
    return r
  
  def sendReplyText(self, userId, bottleId, content):
    connect, cursor = self.connectDataBase()
    sql = "INSERT bottle_reply(user_id, bottle_id, reply) VALUES(%s, %s, %s)"
    r = "success"
    try:
      cursor.execute(sql, [userId, bottleId, content])
      connect.commit()
    except Exception as e:
      connect.rollback()
      print(e)
      r = "fail"
    self.closeDataBase(connect, cursor)
    return r
          
  def getOnePost(self, postId):
    connect, cursor = self.connectDataBase()
    sql = "SELECT * FROM post WHERE post_id=%s"
    cursor.execute(sql, [postId])
    result = cursor.fetchall()
    self.closeDataBase(connect, cursor)
    return result
  
  def getPostComments(self, postId):
    connect, cursor = self.connectDataBase()
    sql = "SELECT * FROM comment WHERE post_id=%s"
    cursor.execute(sql, [postId])
    result = cursor.fetchall()
    self.closeDataBase(connect, cursor)
    return result
  
  def userLikePost(self, userId, postId):
    connect, cursor = self.connectDataBase()
    sql = "INSERT user_like_post(user_id, post_id) VALUES(%s, %s)"
    r = "success"
    try:
      cursor.execute(sql, [userId, postId])
      connect.commit()
    except Exception as e:
      connect.rollback()
      print(e)
      r = "fail"
      self.closeDataBase(connect, cursor)
      return r

    # sql = "UPDATE post SET likes_num=likes_num+1 WHERE post_id=%s"
    # try: 
    #   cursor.execute(sql, [postId])
    #   connect.commit()
    # except Exception as e:
    #   connect.rollback()
    #   print(e)
    #   r = "fail"
    return r
      
  def userLikeComment(self, userId, commentId):
    connect, cursor = self.connectDataBase()
    sql = "INSERT user_like_comment(user_id, comment_id) VALUES(%s, %s)"
    r = "success"
    try:
      cursor.execute(sql, [userId, commentId])
      connect.commit()
    except Exception as e:
      connect.rollback()
      print(e)
      r = "fail"
      self.closeDataBase(connect, cursor)
      return r
    
    # sql = "UPDATE comment SET likes_num=likes_num+1 WHERE comment_id=%s"
    # try: 
    #   cursor.execute(sql, [commentId])
    #   connect.commit()
    # except Exception as e:
    #   connect.rollback()
    #   print(e)
    #   r = "fail"
    return r
  
  def userCreateComment(self, userId, postId, content, comment_time):
    connect, cursor = self.connectDataBase()
    sql = "INSERT comment(content, comment_time, likes_num, user_id, post_id)\
            VALUES (%s, %s, %s, %s, %s)"

    r = "success"
    try:
      cursor.execute(sql, [content, comment_time, '0', userId, postId])
      connect.commit()
    except Exception as e:
      connect.rollback()
      print(e)
      r = "fail"
      
    self.closeDataBase(connect, cursor)
    return r
  
  def userDeleteComment(self, userId, commentId):
    connect, cursor = self.connectDataBase()
    result = "success"
    sql = "SELECT user_id, post_id FROM comment WHERE comment_id=%s"
    cursor.execute(sql, [commentId])
    r = cursor.fetchall()
    if len(r) == 0:
      self.closeDataBase(connect, cursor)
      return "fail"
    create_user_id = r[0][0]
    postId = r[0][1]
    if str(userId) != str(create_user_id):
      self.closeDataBase(connect, cursor)
      return "fail"
    sql = "DELETE FROM comment WHERE comment_id=%s"
    try:
      cursor.execute(sql, [commentId])
      connect.commit()
    except Exception as e:
      connect.rollback()
      print(e)
      result = "fail"
    sql = "update post set comment_num=comment_num - 1 where post.post_id=%s"
    try:
      cursor.execute(sql, [postId])
      connect.commit()
    except Exception as e:
      connect.rollback()
      print(e)
      result = "fail"
    self.closeDataBase(connect, cursor)
    return result
  
  def getFriendsList(self, userId):
    connect, cursor = self.connectDataBase()
    sql = "SELECT * FROM user WHERE user_id IN \
          (SELECT user2_id FROM user_user WHERE user1_id=%s)"
    
    cursor.execute(sql, [userId])
    result = cursor.fetchall()
    self.closeDataBase(connect, cursor)
    return result
  
  def addUserProfilePic(self, userId, picPath):
    connect, cursor = self.connectDataBase()
    sql = "DELETE FROM user_profile_pic WHERE user_id=%s"
    cursor.execute(sql, [userId])
    sql = "INSERT INTO user_profile_pic(user_id, pic_path) VALUES(%s, %s)"
    # sql = "UPDATE user_profile_pic SET user_id=%s, pic_path=%s"
    result = "success"
    try:
      cursor.execute(sql, [userId, picPath])
      connect.commit()
    except Exception as e:
      connect.rollback()
      print(e)
      result = "fail"
    self.closeDataBase(connect, cursor)
    return result
  
  def previewUserProfilePic(self, userId):
    connect, cursor = self.connectDataBase()
    sql = "SELECT pic_path FROM user_profile_pic WHERE user_id=%s"
    cursor.execute(sql, [userId])
    result = cursor.fetchall()
    if len(result) == 0:
      result = (('media/0.jpg',),)
    self.closeDataBase(connect, cursor)
    return result
  
  def getUserIdByName(self, userName):
    connect, cursor = self.connectDataBase()
    sql = "SELECT user_id FROM user WHERE name=%s"
    cursor.execute(sql, [userName])
    result = cursor.fetchall()
    self.closeDataBase(connect, cursor)
    return result
    