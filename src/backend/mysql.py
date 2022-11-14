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
  

  def changeUserInfo(self, userId, userName, gender, age, birth, contact):
    connect, cursor = self.connectDataBase()
    
    sql = "SELECT * FROM user WHERE user_id=%s"
    cursor.execute(sql, [userId])
    
    sql = "UPDATE user SET name=%s, gender=%s, age=%s, birth=%s, contact=%s WHERE user_id=%s"
    try:
      cursor.execute(sql, [userName, gender, age, birth, contact, userId])
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
    return result
  