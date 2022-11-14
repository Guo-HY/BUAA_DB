DROP DATABASE buaa_db2;
CREATE DATABASE if not exists buaa_db2 DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE buaa_db2;

DROP TABLE IF EXISTS `user`;
DROP TABLE IF EXISTS `group`;
DROP TABLE IF EXISTS `post`;
DROP TABLE IF EXISTS `comment`;
DROP TABLE IF EXISTS `bottle`;
DROP TABLE IF EXISTS `bottle_reply`;
DROP TABLE IF EXISTS `activity`;
DROP TABLE IF EXISTS `message`;
DROP TABLE IF EXISTS `tag`;
DROP TABLE IF EXISTS `user_like_comment`;
DROP TABLE IF EXISTS `user_like_post`;
DROP TABLE IF EXISTS `user_tag`;
DROP TABLE IF EXISTS `user_user`;
DROP TABLE IF EXISTS `user_activity`;

CREATE TABLE `user`
(
  `user_id`       INT(20)       NOT NULL AUTO_INCREMENT PRIMARY KEY ,
  `name`          VARCHAR(255)  NOT NULL UNIQUE ,
  `password`      VARCHAR(255)  NOT NULL ,
  `head_portrait` VARCHAR(255) ,
  `contact`       VARCHAR(255) ,
  `gender`        VARCHAR(255) ,
  `age`           INT(20) ,
  `birth`         VARCHAR(255)

)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `group`
(
  `group_id`          INT(20)       NOT NULL AUTO_INCREMENT PRIMARY KEY ,
  `post_num`          INT(20)       NOT NULL ,
  `group_name`        VARCHAR(255)  NOT NULL ,
  `group_description` VARCHAR(1000) NOT NULL ,
  `user_id`           INT(20)       NOT NULL ,
  FOREIGN KEY(`user_id`) REFERENCES `user`(`user_id`)

)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `post`
(
  `post_id`     INT(20)         NOT NULL AUTO_INCREMENT PRIMARY KEY ,
  `name`        VARCHAR(255)    NOT NULL ,
  `context`     VARCHAR(10000)  NOT NULL ,
  `post_time`   VARCHAR(255)    NOT NULL ,
  `comment_num` INT(20)         NOT NULL ,
  `likes_num`   INT(20)         NOT NULL ,
  `user_id`     INT(20)         NOT NULL ,
  `group_id`    INT(20)         NOT NULL ,
  FOREIGN KEY(`user_id`) REFERENCES `user`(`user_id`) ,
  FOREIGN KEY(`group_id`) REFERENCES `group`(`group_id`)

)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `comment`
(
  `comment_id`    INT(20)         NOT NULL AUTO_INCREMENT PRIMARY KEY ,
  `context`       VARCHAR(10000)  NOT NULL ,
  `comment_time`  VARCHAR(255)    NOT NULL ,
  `likes_num`     INT(20)         NOT NULL ,
  `user_id`       INT(20)         NOT NULL ,
  `post_id`       INT(20)         NOT NULL ,
  FOREIGN KEY(`user_id`) REFERENCES `user`(`user_id`) ,
  FOREIGN KEY(`post_id`) REFERENCES `post`(`post_id`)

)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `bottle`
(
  `bottle_id` INT(20)         NOT NULL AUTO_INCREMENT PRIMARY KEY ,
  `context`   VARCHAR(10000)  NOT NULL ,
  `user_id`   INT(20)         NOT NULL ,
  FOREIGN KEY(`user_id`) REFERENCES `user`(`user_id`) 

)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `bottle_reply`
(
  `bottle_reply_id` INT(20)         NOT NULL AUTO_INCREMENT PRIMARY KEY ,
  `context`         VARCHAR(10000)  NOT NULL ,
  `user_id`         INT(20)         NOT NULL ,
  `bottle_id`       INT(20)         NOT NULL ,
  FOREIGN KEY(`user_id`) REFERENCES `user`(`user_id`) ,
  FOREIGN KEY(`bottle_id`) REFERENCES `bottle`(`bottle_id`)

)ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE `activity`
(
  `activity_id` INT(20)         NOT NULL AUTO_INCREMENT PRIMARY KEY ,
  `name`        VARCHAR(255)    NOT NULL ,
  `summary`     VARCHAR(1000)   NOT NULL ,
  `begin_time`  VARCHAR(255)    NOT NULL ,
  `end_time`    VARCHAR(255)    NOT NULL ,
  `location`    VARCHAR(255)    NOT NULL ,
  `activity_nature` VARCHAR(255) NOT NULL, 
  `user_id`     INT(20)         NOT NULL ,
  FOREIGN KEY(`user_id`) REFERENCES `user`(`user_id`) 

)ENGINE=InnoDB DEFAULT CHARSET=utf8; 

CREATE TABLE  `message`
(   
  `message_id`  INT(20)         NOT NULL AUTO_INCREMENT PRIMARY KEY ,
  `context`     VARCHAR(10000)  NOT NULL ,
  `send_time`   VARCHAR(255)    NOT NULL ,
  `send_id`     INT(20)         NOT NULL ,
  `receive_id`  INT(20)         NOT NULL ,
  FOREIGN KEY(`send_id`) REFERENCES `user`(`user_id`) ,
  FOREIGN KEY(`receive_id`) REFERENCES `user`(`user_id`) 

)ENGINE=InnoDB DEFAULT CHARSET=utf8; 

CREATE TABLE  `tag`
(
  `tag_id`    INT(20)       NOT NULL AUTO_INCREMENT PRIMARY KEY ,
  `tag_name`  VARCHAR(255)  NOT NULL 

)ENGINE=InnoDB DEFAULT CHARSET=utf8; 

CREATE TABLE  `user_like_comment`
(
  `user_id`     INT(20)       NOT NULL,
  `comment_id`  INT(20)       NOT NULL,
  FOREIGN KEY(`user_id`) REFERENCES `user`(`user_id`) ,
  FOREIGN KEY(`comment_id`) REFERENCES `comment`(`comment_id`) ,
  PRIMARY KEY(`user_id`, `comment_id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8; 

CREATE TABLE  `user_like_post`
(
  `user_id` INT(20)       NOT NULL , 
  `post_id` INT(20)       NOT NULL , 
  FOREIGN KEY(`user_id`) REFERENCES `user`(`user_id`) ,
  FOREIGN KEY(`post_id`) REFERENCES `post`(`post_id`) ,
  PRIMARY KEY(`user_id`, `post_id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8; 

CREATE TABLE  `user_tag`
(
  `user_id`   INT(20)       NOT NULL ,  
  `tag_id`  INT(20)       NOT NULL , 
  FOREIGN KEY(`user_id`) REFERENCES `user`(`user_id`) ,
  FOREIGN KEY(`tag_id`) REFERENCES `tag`(`tag_id`) ,
  PRIMARY KEY(`user_id`, `tag_id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8; 

CREATE TABLE  `group_tag`
(
  `group_id`  INT(20)       NOT NULL ,
  `tag_id`  INT(20)       NOT NULL ,
  FOREIGN KEY(`group_id`) REFERENCES `group`(`group_id`) ,
  FOREIGN KEY(`tag_id`) REFERENCES `tag`(`tag_id`) ,
  PRIMARY KEY(`group_id`, `tag_id`)

)ENGINE=InnoDB DEFAULT CHARSET=utf8; 

CREATE TABLE  `user_user`
(
  `user1_id` INT(20)       NOT NULL ,
  `user2_id` INT(20)       NOT NULL ,
  FOREIGN KEY(`user1_id`) REFERENCES `user`(`user_id`) ,
  FOREIGN KEY(`user2_id`) REFERENCES `user`(`user_id`) ,
  PRIMARY KEY(`user1_id`, `user2_id`)

)ENGINE=InnoDB DEFAULT CHARSET=utf8; 

CREATE TABLE  `user_acitivity`
(
  `user_id`     INT(20)       NOT NULL ,
  `activity_id` INT(20)       NOT NULL ,
  FOREIGN KEY(`user_id`) REFERENCES `user`(`user_id`) ,
  FOREIGN KEY(`activity_id`) REFERENCES `activity`(`activity_id`) ,
  PRIMARY KEY(`user_id`, `activity_id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8; 

INSERT INTO `user` 
(name, password, head_portrait, contact, gender, age, birth)
VALUES
('ghy', '123ghy', '123', '456', 'm', 20, '789'),
('zal', '123zal', '123', '456', 'f', 20, '789'),
('zlb', '123zlb', '123', '456', 'm', 20, '789');

INSERT INTO `activity`
(name, summary, begin_time, end_time, location, activity_nature, user_id)
VALUES
('act1', 'this is act1', '2022-11-14', '2022-11-15', 'voc', 'act', 1),
('act2', 'this is act2', '2022-11-16', '2022-11-17', 'as', 'gcc', 2),
('act3', 'this is act3', '2022-11-18', '2022-11-19', 'vasd', 'vdst', 3);

INSERT INTO `tag`
(tag_name)
VALUES
('tag1'),('tag2'),('tag3');

INSERT INTO  `user_tag`
(user_id, tag_id)
VALUES
(1, 1),
(2, 2),
(3, 3);

