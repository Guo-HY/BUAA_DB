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
  
  
  def createActivity(self, userId, name, region, beginDate, endDate, desc, activitieNature):
    connect, cursor = self.connectDataBase()
    sql = "INSERT INTO activity(name, summary, begin_time, end_time, location, activity_nature, user_id) \
            VALUES(%s, %s, %s, %s, %s, %s, %s)"
    
    try:
      cursor.execute(sql, [name, desc, beginDate, endDate, region, activitieNature, userId])
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
    sql = "SELECT * FROM group"
    cursor.execute(sql)
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
    sql = "INSERT INTO group(post_num, group_name, group_desc, user_id)\
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
  
  def getSingleGroup(self, groupId):
    connect, cursor = self.connectDataBase()
    sql = "SELECT * FROM group WHERE group_id=%s"
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
  
  def userCreatePost(self, userId, groupId, post_name, context, post_time):
    connect, cursor = self.connectDataBase()
    sql = "INSERT INTO post(name, context, post_time, comment_num, likes_num, user_id, group_id)\
      VALUES(%s, %s, %s, %s, %s, %s, %s)"
    result = "success"
    try:
      cursor.execute(sql, [post_name, context, post_time, '0', '0', userId, groupId])
      connect.commit()
    except Exception as e:
      connect.rollback()
      print(e)
      result = "fail"
    self.closeDataBase(connect, cursor)
    return result
    
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
          
