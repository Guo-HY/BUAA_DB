CREATE DATABASE if not exists buaa_db1 DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE buaa_db1;

DROP TABLE IF EXISTS `student_course`;
DROP TABLE IF EXISTS `students`;
CREATE TABLE `students`
(
  `student_id` INT(20) PRIMARY KEY NOT NULL,
  `student_username` VARCHAR(255) NOT NULL,
  `student_password` VARCHAR(255) NOT NULL,
  `student_grade` INT(20) NOT NULL,
  `student_class` INT(20) NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `courses`;
-- 创建课程表
CREATE TABLE `courses`
(
  `course_id` INT(20) PRIMARY KEY NOT NULL,
  `course_name` VARCHAR(255) NOT NULL,
  `course_intro` VARCHAR(10000) DEFAULT NULL,
  `course_capacity` INT(20) NOT NULL,
  `course_elected` INT(20) NOT NULL DEFAULT 0,
  CHECK(`course_elected` <= `course_capacity`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `student_course`;
-- 创建学生选课表 
CREATE TABLE `student_course`
(
  `student_id` INT(20) NOT NULL,
  `course_id` INT(20) NOT NULL,
  FOREIGN KEY(`student_id`) REFERENCES `students`(`student_id`),
  FOREIGN KEY(`course_id`) REFERENCES `courses`(`course_id`),
  PRIMARY KEY(`student_id`, `course_id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
  
INSERT INTO `students` 
(student_id, student_username, student_password, student_grade, student_class)
VALUES
(1, 'ghy', '123ghy', 1, 1),
(2, 'zal', '123zal', 2, 2),
(3, 'zlb', '123zlb', 3, 3);

INSERT INTO `courses` 
(course_id, course_name, course_intro, course_capacity, course_elected)
VALUES
(1, 'A', 'aaa', 2, 0),
(2, 'B', 'bbb', 2, 0),
(3, 'C', 'ccc', 4, 0);

INSERT INTO `student_course` 
(student_id, course_id)
VALUES
(1, 1),
(2, 2),
(3, 3);