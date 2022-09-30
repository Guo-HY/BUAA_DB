from re import L
from sqlite3 import Cursor
import pymysql

class Mysql:
  
  def connectDataBase(self):
    connect = pymysql.connect(host='localhost',
                              user='root',
                              password='123mysql',
                              database='buaa_db1')
    cursor = connect.cursor()
    return connect, cursor
  
  def closeDataBase(self,connect, cursor):
    connect.close()
    cursor.close()
  
  def studentLogin(self, student_id, student_password):
    connect, cursor = self.connectDataBase()
    
    sql = "SELECT * FROM students WHERE student_id=%s"
    cursor.execute(sql, [student_id])
    result = cursor.fetchall()
    self.closeDataBase(connect, cursor)
    return result
    
  def studentRegister(self, student_id, student_password, 
                      student_username, student_grade, student_class):
    connect, cursor = self.connectDataBase()
    sql = "INSERT INTO students(student_id, student_password, \
          student_username, student_grade, student_class) \
          VALUES (%s, %s, %s, %s, %s) "
    
    try:
      cursor.execute(sql, [student_id, student_password, student_username,
                           student_grade, student_class])
      connect.commit()
    except Exception as e:
      connect.rollback()
      print("error : can't register student")
      self.closeDataBase(connect, cursor)
      return False
    self.closeDataBase(connect, cursor)
    return True
  
  def studentCurriculum(self, student_id):
    connect, cursor = self.connectDataBase()
    sql = "SELECT * FROM courses WHERE course_id NOT IN ( \
      SELECT course_id FROM student_course WHERE student_id = %s)"

    cursor.execute(sql, [student_id])
    result = cursor.fetchall()
    self.closeDataBase(connect, cursor)
    return result
    
  def studentCourseSelection(self, student_id, course_id):
    connect, cursor = self.connectDataBase()
    sql = "INSERT INTO student_course(student_id, course_id) \
      VALUES (%s, %s)"
      
    try:
      cursor.execute(sql, [student_id, course_id])
      connect.commit()
    except Exception as e:
      connect.rollback()
      print("error in <studentCourseSelection>")
      self.closeDataBase(connect, cursor)
      return False
    return True
  
  def studentCoursePost(self, student_id):
    connect, cursor = self.connectDataBase()
    sql = "SELECT * FROM courses WHERE course_id IN ( \
      SELECT course_id FROM student_course WHERE student_id = %s)"

    cursor.execute(sql, [student_id])
    result = cursor.fetchall()
    self.closeDataBase(connect, cursor)
    return result
  
  def studentCourseWithdraw(self, student_id, course_id):
    connect, cursor = self.connectDataBase()
    sql = "DELETE FROM student_course WHERE student_id=%s AND course_id=%s"
    cursor.execute(sql, [student_id, course_id])
    connect.commit()
    self.closeDataBase(connect, cursor)
    return 
    