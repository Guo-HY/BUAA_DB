-- 使用分号作为结束符
delimiter ;
-- 如果存在数据库就先删除
DROP DATABASE buaa_db2;
CREATE DATABASE if not exists buaa_db2 DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE buaa_db2;

-- 删除表
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
DROP TABLE IF EXISTS `group_tag`;
DROP TABLE IF EXISTS `user_user`;
DROP TABLE IF EXISTS `user_activity`;
DROP TABLE IF EXISTS `user_profile_pic`;

-- init table
-- 新建user表，user_id是自增主键
CREATE TABLE `user`
(
  `user_id`       INT(20)       NOT NULL AUTO_INCREMENT PRIMARY KEY ,
  `name`          VARCHAR(255)  NOT NULL UNIQUE ,
  `password`      VARCHAR(255)  NOT NULL ,
  `head_portrait` VARCHAR(255) ,
  `contact`       VARCHAR(255) ,
  `gender`        VARCHAR(255) ,
  `age`           INT(20) ,
  `address`       VARCHAR(255)

)ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 新建group表，其中user_id是外键，group_id是自增主键。
CREATE TABLE `group`
(
  `group_id`          INT(20)       NOT NULL AUTO_INCREMENT PRIMARY KEY ,
  `post_num`          INT(20)       NOT NULL ,
  `group_name`        VARCHAR(255)  NOT NULL ,
  `group_desc`        VARCHAR(1000) NOT NULL ,
  `user_id`           INT(20)       NOT NULL ,
  FOREIGN KEY(`user_id`) REFERENCES `user`(`user_id`)

)ENGINE=InnoDB DEFAULT CHARSET=utf8;
-- 新建post表，post_id是自增主键，user_id，group_id是外键
CREATE TABLE `post`
(
  `post_id`     INT(20)         NOT NULL AUTO_INCREMENT PRIMARY KEY ,
  `name`        VARCHAR(255)    NOT NULL ,
  `content`     VARCHAR(10000)  NOT NULL ,
  `post_time`   VARCHAR(255)    NOT NULL ,
  `comment_num` INT(20)         NOT NULL ,
  `likes_num`   INT(20)         NOT NULL ,
  `user_id`     INT(20)         NOT NULL ,
  `group_id`    INT(20)         NOT NULL ,
  FOREIGN KEY(`user_id`) REFERENCES `user`(`user_id`) ,
  FOREIGN KEY(`group_id`) REFERENCES `group`(`group_id`)

)ENGINE=InnoDB DEFAULT CHARSET=utf8;
-- 新建评论表，comment_id是自增主键，user_id，post_id是外键
CREATE TABLE `comment`
(
  `comment_id`    INT(20)         NOT NULL AUTO_INCREMENT PRIMARY KEY ,
  `content`       VARCHAR(10000)  NOT NULL ,
  `comment_time`  VARCHAR(255)    NOT NULL ,
  `likes_num`     INT(20)         NOT NULL ,
  `user_id`       INT(20)         NOT NULL ,
  `post_id`       INT(20)         NOT NULL ,
  FOREIGN KEY(`user_id`) REFERENCES `user`(`user_id`) ,
  FOREIGN KEY(`post_id`) REFERENCES `post`(`post_id`)

)ENGINE=InnoDB DEFAULT CHARSET=utf8;
-- 新建bottle表，bottle_id是自增主键，user_id是外键
CREATE TABLE `bottle`
(
  `bottle_id` INT(20)         NOT NULL AUTO_INCREMENT PRIMARY KEY ,
  `content`   VARCHAR(10000)  NOT NULL ,
  `user_id`   INT(20)         NOT NULL ,
  FOREIGN KEY(`user_id`) REFERENCES `user`(`user_id`) 

)ENGINE=InnoDB DEFAULT CHARSET=utf8;
-- 新建bottle_reply表，bottle_reply_id是自增主键，
-- user_id，bottle_id是外键
CREATE TABLE `bottle_reply`
(
  `bottle_reply_id` INT(20)         NOT NULL AUTO_INCREMENT PRIMARY KEY ,
  `reply`           VARCHAR(10000)  NOT NULL ,
  `user_id`         INT(20)         NOT NULL ,
  `bottle_id`       INT(20)         NOT NULL ,
  FOREIGN KEY(`user_id`) REFERENCES `user`(`user_id`) ,
  FOREIGN KEY(`bottle_id`) REFERENCES `bottle`(`bottle_id`)

)ENGINE=InnoDB DEFAULT CHARSET=utf8;
-- 新建activity表,activity_id是自增主键,user_id是外键.
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
  `content`     VARCHAR(10000)  NOT NULL ,
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

CREATE TABLE `user_profile_pic`
(
  `pic_id`    INT(20)       NOT NULL AUTO_INCREMENT PRIMARY KEY ,
  `user_id`   INT(20)       NOT NULL UNIQUE ,
  `pic_path`  VARCHAR(255)  NOT NULL,
  FOREIGN KEY(`user_id`) REFERENCES `user`(`user_id`) 
)ENGINE=InnoDB DEFAULT CHARSET=utf8; 

-- trigger
create trigger `inc_post_num_in_group` after insert on `post` for each row
  update `group` set `post_num`=`post_num` + 1 where `group`.`group_id`=new.`group_id`;

-- create trigger `dec_post_num_in_group` before delete on `post` for each row
--   update `group` set `post_num`=`post_num` - 1 where `group`.`group_id`=old.`group_id`;

create trigger `inc_comment_num_in_post` after insert on `comment` for each row
  update `post` set `comment_num`=`comment_num` + 1 where `post`.`post_id`=new.`post_id`;

-- create trigger `dec_comment_num_in_post` after delete on `comment` for each row
--   update `post` set `comment_num`=`comment_num` - 1 where `post`.`post_id`=old.`post_id`;

create trigger `inc_likes_num_in_post` after insert on `user_like_post` for each row
  update `post` set `likes_num`=`likes_num` + 1 where `post`.`post_id`=new.`post_id`;

-- create trigger `dec_likes_num_in_post` after delete on `user_like_post` for each row
--   update `post` set `likes_num`=`likes_num` - 1 where `post`.`post_id`=old.`post_id`;

create trigger `inc_likes_num_in_comment` after insert on `user_like_comment` for each row
  update `comment` set `likes_num`=`likes_num` + 1 where `comment`.`comment_id`=new.`comment_id`;

-- create trigger `dec_likes_num_in_comment` after delete on `user_like_comment` for each row
--   update `comment` set `likes_num`=`likes_num` - 1 where `comment`.`comment_id`=old.`comment_id`;

create trigger `delete_post_in_group_before_delete_group` before delete on `group` for each row
  delete from `post` where `group_id`=old.`group_id`;

create trigger `delete_group_tag_before_delete_group` before delete on `group` for each row
  delete from `group_tag` where `group_id`=old.`group_id`;

create trigger `delete_comment_in_post_before_delete_post` before delete on `post` for each row
  delete from `comment` where `post_id`=old.`post_id`;

create trigger `delete_user_like_post_before_delete_post` before delete on `post` for each row
  delete from `user_like_post` where `post_id`=old.`post_id`;

create trigger `delete_user_like_comment_before_delete_comment` before delete on `comment` for each row
  delete from `user_like_comment` where `comment_id`=old.`comment_id`;


-- porcedure 
delimiter $$
create procedure `checkAndAddTagProc` (in `tagName` VARCHAR(255))
begin
  if (not exists (select * from `tag` where `tag_name`=`tagName`)) then
    insert into `tag` (tag_name) values (`tagName`);
  end if;
end$$
delimiter ;

-- init data
INSERT INTO `user` 
(name, password, head_portrait, contact, gender, age, address)
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

INSERT INTO `bottle`
(content, user_id)
VALUES
('this is user_id=1 send bottle 1', '1'),
('this is user_id=2 send bottle 2', '2'),
('this is user_id=3 send bottle 3', '3');

INSERT INTO `bottle_reply`
(reply, user_id, bottle_id)
VALUES
('this is reply from user2 to bottle1', '2', '1'),
('this is reply from user3 to bottle2', '3', '2'),
('this is reply from user1 to bottle3', '1', '3');

INSERT INTO `group`
(post_num, group_name, group_desc, user_id)
VALUES
(0, 'group1', 'this is group1', 1),
(0, 'group2', 'this is group2', 2),
(0, 'group3', 'this is group3', 1);

INSERT INTO `post`
(name, content, post_time, comment_num, likes_num, user_id, group_id)
VALUES
('post1', 'this is post1', 'time1', 0, 0, 1, 1),
('post2', 'this is post2', 'time2', 0, 0, 2, 1),
('post3', 'this is post3', 'time3', 0, 0, 3, 2),
('post4', 'this is post4', 'time4', 0, 0, 1, 3);

INSERT INTO `comment`
(content, comment_time, likes_num, user_id, post_id)
VALUES
('this is comment1', 'time1', 0, 1, 1),
('this is comment2', 'time1', 0, 1, 2),
('this is comment1', 'time1', 0, 1, 3),
('this is comment1', 'time1', 0, 1, 4);

INSERT INTO `group_tag`
(group_id, tag_id)
VALUES
(1, 1),
(2, 2),
(3, 3);