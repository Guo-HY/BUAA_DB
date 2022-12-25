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
--   -- `pic`               VARCHAR(255)  NOT NULL DEFAULT 'media/0.jpg',
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

CREATE TABLE `user_group_score`
(
  `user_id`     INT(20)   NOT NULL ,
  `group_id`  INT(20)     NOT NULL ,
  `score`     INT(20)     NOT NULL ,  
  FOREIGN KEY(`user_id`) REFERENCES `user`(`user_id`) ,
  FOREIGN KEY(`group_id`) REFERENCES `group`(`group_id`)
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

delimiter $$
create procedure `update_user_group_score` (in `userid` INT(20), in `groupid` INT(20), in `add_score` INT(20) )
begin
  if (not exists (select * from `user_group_score` where `user_id`=`userid` and `group_id`=`groupid`)) then
    insert into `user_group_score`(`user_id`,`group_id`,`score`) values (`userid`, `groupid`, `add_score`);
  else
    update `user_group_score` set `score`=`score` + `add_score` where `user_id`=`userid` and `group_id`=`groupid`;
  end if;

end$$
delimiter ;

delimiter $$
create trigger `update_score_after_user_add_post` after insert on `post` for each ROW
begin
  CALL `update_user_group_score`(new.user_id, new.group_id, 5);
end$$
delimiter ;

delimiter $$
create trigger `update_score_after_user_add_comment` after insert on `comment` for each ROW
begin
  select `group_id` into @groupid from `post` where `post`.`post_id`=new.post_id;
  CALL `update_user_group_score`(new.user_id, @groupid, 3);
end$$
delimiter ;

delimiter $$
create trigger `update_score_after_user_like_post` after insert on `user_like_post` for each ROW
begin
  select `group_id` into @groupid from `post` where `post`.`post_id`=new.post_id;
  CALL `update_user_group_score`(new.user_id, @groupid, 1);
end$$
delimiter ;

delimiter $$
create trigger `update_score_after_user_like_comment` after insert on `user_like_comment` for each ROW
begin
  select `group_id` into @groupid from `post` where `post`.`post_id`=(select post_id from comment where comment.comment_id=new.comment_id);
  CALL `update_user_group_score`(new.user_id, @groupid, 1);
end$$
delimiter ;

create trigger `delete_user_group_score_before_delete_group` before delete on `group` for each row
  delete from `user_group_score` where `group_id`=old.`group_id`;



-- build index

create index `user_name` on `user`(`name`);
create index `user_user_id` on `user`(`user_id`);
create index `group_group_id` on `group`(`group_id`);
create index `group_user_id` on `group`(`user_id`);
create index `post_id` on `post`(`post_id`);
create index `user_id` on `post`(`user_id`);
create index `group_id` on `post`(`group_id`);
create index `comment_user_id` on `comment`(`user_id`);
create index `comment_post_id` on `comment`(`post_id`);
create index `bottle_bottle_id` on `bottle`(`bottle_id`);
create index `bottle_user_id` on `bottle`(`user_id`);
create index `bottle_reply_user_id` on `bottle_reply`(`user_id`);
create index `bottle_reply_bottle_id` on `bottle_reply`(`bottle_id`);

-- -- init data
-- INSERT INTO `user` 
-- (name, password, head_portrait, contact, gender, age, address)
-- VALUES
-- ('ghy', '123ghy', '123', '456', 'm', 20, '789'),
-- ('zal', '123zal', '123', '456', 'f', 20, '789'),
-- ('zlb', '123zlb', '123', '456', 'm', 20, '789');

-- INSERT INTO `activity`
-- (name, summary, begin_time, end_time, location, activity_nature, user_id)
-- VALUES
-- ('act1', 'this is act1', '2022-11-14', '2022-11-15', 'voc', 'act', 1),
-- ('act2', 'this is act2', '2022-11-16', '2022-11-17', 'as', 'gcc', 2),
-- ('act3', 'this is act3', '2022-11-18', '2022-11-19', 'vasd', 'vdst', 3);

-- INSERT INTO `tag`
-- (tag_name)
-- VALUES
-- ('tag1'),('tag2'),('tag3');

-- INSERT INTO  `user_tag`
-- (user_id, tag_id)
-- VALUES
-- (1, 1),
-- (2, 2),
-- (3, 3);

-- INSERT INTO `bottle`
-- (content, user_id)
-- VALUES
-- ('this is user_id=1 send bottle 1', '1'),
-- ('this is user_id=2 send bottle 2', '2'),
-- ('this is user_id=3 send bottle 3', '3');

-- INSERT INTO `bottle_reply`
-- (reply, user_id, bottle_id)
-- VALUES
-- ('this is reply from user2 to bottle1', '2', '1'),
-- ('this is reply from user3 to bottle2', '3', '2'),
-- ('this is reply from user1 to bottle3', '1', '3');

-- INSERT INTO `group`
-- (post_num, group_name, group_desc, user_id)
-- VALUES
-- (0, 'group1', 'this is group1', 1),
-- (0, 'group2', 'this is group2', 2),
-- (0, 'group3', 'this is group3', 1);

-- INSERT INTO `post`
-- (name, content, post_time, comment_num, likes_num, user_id, group_id)
-- VALUES
-- ('post1', 'this is post1', 'time1', 0, 0, 1, 1),
-- ('post2', 'this is post2', 'time2', 0, 0, 2, 1),
-- ('post3', 'this is post3', 'time3', 0, 0, 3, 2),
-- ('post4', 'this is post4', 'time4', 0, 0, 1, 3);

-- INSERT INTO `comment`
-- (content, comment_time, likes_num, user_id, post_id)
-- VALUES
-- ('this is comment1', 'time1', 0, 1, 1),
-- ('this is comment2', 'time1', 0, 1, 2),
-- ('this is comment1', 'time1', 0, 1, 3),
-- ('this is comment1', 'time1', 0, 1, 4);

-- INSERT INTO `group_tag`
-- (group_id, tag_id)
-- VALUES
-- (1, 1),
-- (2, 2),
-- (3, 3);
  INSERT INTO `user` VALUES (1,'speed','123ghy','123','123456','男',21,'usa'),(2,'messi','123zal','123','123456','男',35,'buaa'),(3,'Neymar','123zlb','123','456','男',20,'789');
   INSERT INTO `group` VALUES (1,2,'旅游','这儿是旅游爱好者分享旅游快乐的地方！',1),(2,2,'原神','契约已成,食言者当受食盐之罚',1),(3,3,'足球','只要心脏在跳动就不会舍弃脚下滚动的足球！',1);
  INSERT INTO `post` VALUES (1,'2022 年卡塔尔世界杯半决赛法国 2:0 摩洛哥晋级决赛，如何评价本场比赛？','1，格列兹曼战神中的战神，如果不是他来回厮杀，法国能不能苟到第二个进球十分难说。\n\n2，法国拿下得颇为艰难，左路防守也被摩洛哥打得透透的，甚至一度到了摩洛哥想怎么打就怎么有的程度。起初以为是姆巴佩不回防导致那么大的压力，结果姆总回来了几次也就一根电桩。\n\n3，所以很显然，法国的左路防守是可以加以利用的。回到英法大战，其实英格兰的不少机会也都是从法国队左路来的。凯恩打飞的那个点球，也是左后卫特奥一次鲁莽的背后撞人送出去的。特奥今天的进球很精彩，但他亲哥受伤后法国就他一个正印左后卫。想想昨天梅西在这个位置怎么欺负格瓦迪奥尔的。所以特奥真正的考验实际在决赛。\n\n4，德尚针对这点的调整是有点意思的，他下了今天脚风稀碎的吉鲁，把姆巴佩移到中间，左边则是新上场的小图拉姆。从本场来说，这招效果不错，左路防守瞬间缓解，前场也在适应后有收获。不过这估计只能作为权宜之计，毕竟损失的是吉鲁这个大支点。\n\n5，摩洛哥多少有些可惜，上半场的反扑就有一个倒勾中柱，下半场更是数过法国球门而不入，就连补时阶段在门线上的球都要被挡出来。虽然他们已经创造了历史，但实际距离更新的历史并不遥远。\n\n6，法国队看似没有弱点的阵容其实已经被英格兰和摩洛哥打出了缺口。还是那句话——阿根廷很有机会！\n','2022-12-25 10:44:46',3,1,1,3),(2,'2022 年卡塔尔世界杯半决赛阿根廷 3:0 克罗地亚，时隔 8 年再进决赛，如何评价本场比赛？','本届世界杯，梅西第三次完成单场进球加助攻的表演。\n\n于是，他世界杯上的助攻总数达到八次，和马拉多纳并列第一；进球数十一粒，现役现役球员第一；上场纪录和马特乌斯一样，达到25场。\n\n本届世界杯，梅西第三次完成单场进球加助攻的表演。\n\n于是，他世界杯上的助攻总数达到八次，和马拉多纳并列第一；进球数十一粒，现役现役球员第一；上场纪录和马特乌斯一样，达到25场。\n\n如果有很年轻的球迷，没有看过巅峰期梅西的比赛，那这一记助攻，多少能让他们领略一些巅峰梅西的风采。\n\n为什么这么说呢？因为这球，本来并不是一个机会。而梅西靠自己的带球，推进，摆脱，过人以及最后一传，硬生生把一个平淡的回合转化成了进球。\n\n这是巅峰期梅西常做的事情。甚至疯起来的时候，他一个人就能把这事儿从头到尾做完。\n\n甚至，这个球的发起和策动，实在是太过突然，以至于当梅西推进到三十米区域的时候，克罗地亚依然还没有上包夹。\n\n这届比赛，在前场三十米区域对梅西实行一对一防守的，我印象中这几乎是第一次。\n\n结果，被梅西留下心理阴影的中后卫又多了一位。坦白说格瓦迪奥尔本届比赛的表现，以及个人整体的成长，已经足够出色了。但一对一防守梅西，即便是35岁的梅西，依然还是，太过艰难的任务。\n\n最后的结果，确实被梅西过得干干净净。并不是经典的高速推进中正面变向过人，而是半背身情况下的节奏变化，以及繁复细微的身位假动作。以及，最后切进去那一下，依然扎实的身体对抗。\n\n也许，这是梅西参加的五届世界杯，迄今为止，单个回合最惊人的表演？他也终于在世界杯上，留下了这样的回合。\n\n类似的，甚至比这个更为惊人的表现，他在联赛和欧冠联赛，已经有许许多多了。\n\n时隔八年，阿根廷再次进入决赛。而梅西，终于有机会，再一次冲击自己的终极大满贯。\n\n而且这一路的晋级，梅西固然是光芒万丈，定海神针，但队友提供的支持，无论是活力还是能力，对梅西而言都显得弥足珍贵。\n\n阿尔瓦雷斯从和梅西合照的孩子，成为了与他并肩作战，提供最多帮助的队友，实在是最好的传承故事。\n\n直到这一刻，我们才可以确认，世界杯开始前所说的阿根廷很团结，都希望能和梅西一起夺得冠军，并不是应付媒体的套话。\n\n-\n\n足球世界，总是代有才人出。\n\n莫德里奇，告别了世界杯（还有三四名）。\n\n即便最后离开的时候，他也依然还是平静的。本届比赛他已经完成了不可思议的成就，险些能带着克罗地亚连续两届晋级决赛。\n\n以他的年纪，依然能在场上完成几乎不出错的串联，组织，策动和防守。\n\n几乎前所未有。\n\n这一场，真是承载了足球世界里最美好的一部分内容。\n再见魔笛，加油梅西。\n\n','2022-12-25 10:52:49',1,0,2,3),(3,'王者荣耀和原神哪个会先倒下？','大概率原神先凉。\n其实已经有人讲过了，原神这游戏真正在玩的没多少人，你之所以觉得这游戏火，是因为你是这个圈子的，你的各种娱乐APP会自动给你推送相关内容。有多少人小号一大堆?有多少人通关了就弃坑了?有多少人玩了一两天停留在十几级就溜了?\n女508L\n的7C心P\n二料冠军，快\n关于作\n我经常进萌新世界，我曾经以为最需要帮助的就是10到30级的萌新，于是我经常申请进这些萌新的世界，但是没几个能进去，为什么? 因为这些人根本就没玩，这游戏里面最萌新的是35级往上的因为下面的根本就不玩\n因为有很多人通关了就走，所以原神这类的游戏会想方设法拉长你通关的时长，表现在游戏里就是你用的所有东西都需要升级突破，你用的角色要升级突破，你用的武器也要，你的天赋也要，你的圣遗物也要，你的神像也要，你的世界树也要，你的好感度也要，你的冒险等级也要。\n分\n为了保证每天都有人玩，原神还设置了每日任务，每日委托的奖励是原石重要的来源.\n而相比之下王者荣耀并没有这么做，严格意义上讲，王者荣耀硬性的养成目标只有铭文，其他什么也不要求。只要你对目前自己的段位已经满意了，你完全可以摆，全游戏所有的奖励均对你开放，高低段位无差。不想打排位就可以邀请好友一起娱乐局开黑。对于日活，王者的奖励几乎是可以放弃，可以说对玩家每日活跃基本无要求，只有一些特定的节日会有为期一周左右的活跃度奖赏，完事拿完奖励以后你该摆接着摆没人管你。但是原神不同，原神想要完整的游戏体验至少得55级，55级以下不能摆，首先大世界奖励不同，其次你不能随意进别人的世界。\n原神流水高是因为氮佬氮金力度大，而不是玩的人多，不能代表人气，众所周知原神的氮金上限是十分恐怖的，一个卡池想要拿满几个W就下去了，顶级氮佬每个卡池都捞一个满命满精，那个氰余程度不敢想，即使抽一个零命一精，一个648恐怕都不行。所以原神的流水是切切实实的物价高,氮佬不差钱。而王者荣耀又不一样，无论你多有钱，在一定时间内王者荣耀商品的总价格都是有限的，你氮不了多少，所以王者的流水是实实在在的人气。\n以上都可以总结为一句话: 王者荣耀没有弃坑成本\n你现在玩王者玩的累了，你可以果断卸载，什么时候想玩了再下载，因为你知道你根本不会损失任何东西。而原神你玩累了，你要不要卸载你还要掂量一下，因为很可能下次你喜欢的角色复刻了结果你没有石头，你每天把每日做了就石头充裕，所以原神的弃坑成本是比较高的。','2022-12-25 11:03:05',0,0,2,2),(4,'初玩游戏《原神》，有什么忠告？','1、非XP党请不要随便氪金，因为你大概率会后悔。七神必抽，辅助保值能力远强于主C。没钱不要碰武器池。2、不要买成品号，因为剧情和探索在游戏的占比也相当重要。这游戏不是只有深渊。3、前期队伍成型期间建议玩一拖三队，一个C位带三个辅助，辅助不用拉太高，50级不会暴毙就行，资源灌给站场主C。后期辅助资源拉起来后可以试一试国家队（四脱手C）等配队。4、冒险10级以后，注意武器升级的重要性；冒险25级以后，注意圣遗物升级的重要性；冒险35级以后，注意技能等级的重要性，同时注意收集高星主属性对应的圣遗物，套装不重要；冒险45级以后，刷出一套合格的C位用5星套装；冒险50级以后，注意辅助练度的重要性。5、如果不是极限挑战玩家，遇到打不过的BOSS不要强打，请找高等级玩家帮你宰。天遒谷三塔一旦接取在完成前不能联机，请保证练度足够打过战斗塔以及拥有捕风瓶或者口袋锚点后再接取任务。6、摆正心态，这游戏没有PVP，别老是比来比去，开心最重要。玩游不混圈，赛过活神仙。7、人不会因为玩了某游戏就高人一等，不要随便鄙视除了猴，魔怔人，拱火乐子人，天龙人等以外的正常玩家。你要的答案：1、主角不适合C，厨力党给配上一套C位配置之后也可以C，但是不建议这样做。目前主角比较适合辅助，无论是风主聚怪岩主盖桶还是雷主充能。2、达达乌帕谷剑冢任务能白嫖一个4星单手剑原胚，（或者是大剑？）冒险等级提升会送4星的试做斩岩，雪山解密出一个密室里有一把4星大剑雪葬的星银。锻造武器中目前只推荐稻妻的天目影打刀，璃月的试做古华，其他不考虑特殊用途下（如女仆适合配白影剑）不推荐。3、角色实际情况请找攻略，一般是抽到谁练谁。','2022-12-25 11:03:57',0,0,2,2),(5,'墨脱旅行指南','\n因墨脱山多，且属于亚热带气候，夏季多雨，容易诱发山洪的泥石流，所以一直以来进入墨脱都相当困难。墨脱是全国最后一个通公路的地方，没通公路之前，这边一年大概有半年的时间都处于封山状态，外界进不去，里面也出不来，从十一月份一直持续到次年五月份。现在的墨脱，有一条公路，从波密的扎木镇一直修到墨脱县城，叫扎墨公路。今年（2021）另一条从派镇到墨脱的公路也会通车。据说派墨公路通车以后，从拉萨到墨脱只需要一天的时间。\n\n你要想去墨脱，需要提前准备好边防证。墨脱和印度毗邻，位于边防地带。很早之前的时候去墨脱需要边防证，后来边防证制度取消了，去墨脱县城不用边防证（徒步仍需要）。不过从今年三月份开始，进县城也需要边防证了。\n\n你要想去墨脱，什么季节去最好呢？我是冬天去的，感觉那边的冬天比内地的春天还要好。我不建议夏季去，因为夏季是雨季，据我碰到的好几个人说，夏天每天都在下雨，很潮湿。有时还会因为泥石流断路。有一个朋友七月份去的墨脱，到了墨脱之后，哪里也去不了，每天都在旅馆呆着。雨多设备容易坏，有时候夏天还会断电断网。夏天去更让人觉得不舒服的一点是还要收费，类似于门票，210块。这个在网上有些争议。','2022-12-25 11:06:19',0,0,2,1),(6,'大理旅居旅行不完全指南','在大理待了大半年了，对大理多少有了了解。\n\n想当初决定来大理的时候，虽然做了不少攻略，对这边的印象还是很模糊，以为到了大理就到了大理古城，纠结好久要住古城还是海边，或者市区。以为大理四季如春，只有一床被子分分钟被大理的冬天教做人。\n\n现在对大理有一定的了解了，就想写一写，一方面当作来过的纪念，另一方面也希望能给想来大理的人一个参考。\n版权归作者所有，任何形式转载请联系作者。\n\n大理年温差小，日温差比较大，特别是冬天，可能会有十几二十度的温差。「四季如春，一天分四季，一雨变成冬」这民谚说得非常准确了，一天内早晚和中午是两个季节，室内和室外也是两个季节。\n\n大理的四季基本都体验过了，总的来说夏天更舒适一些，早晚不会太凉，中午再热一般也不会超过 30 度。而且夏季属于雨季，据我观察到的规律经常是连续下小半个月的雨，然后再连续晴天大半个月，如此循环。\n\n冬季就比较难熬，干旱、大风，会一直持续到次年春天。如果在室外也还好，室内体感温度肯定零下了，特别是晚上，一床春夏被是肯定过不去的（别问我怎么知道的\n\n大理交通很方便，从昆明动车过来 400+ 公里， 2 小时车程。大理机场通往北京、上海、广州、成都、重庆等各大城市的航班都有。','2022-12-25 11:07:06',0,0,2,1),(7,'2022 年卡塔尔世界杯 1/4 决赛摩洛哥爆冷 1:0 淘汰葡萄牙，如何评价本场比赛？','1970年墨西哥世界杯，摩洛哥队是首支挺进世界杯决赛圈的非洲球队；\n\n1986年墨西哥世界杯，摩洛哥与波兰、英格兰和葡萄牙同处F组，以一胜两平的战绩获得小组头名出线，是首支小组出线的非洲球队，在淘汰赛首轮遇到后来的亚军西德队，被马特乌斯在比赛第87分钟绝杀，遗憾出局。\n\n2022年卡塔尔世界杯，在没什么人看好的情况下，摩洛哥人用众志成城的防守、行云流水的反击、简练大气的球风连斩伊比利亚联盟，成为第一支进入四强的非洲球队。\n\n非洲之光，闪耀卡塔尔。\n\n作为北非门户的守护神，今天的布努送出了三次扑救，包括菲利克斯的劲射和C罗在补时阶段的准单刀，继续保证摩洛哥的大门没有被对手所打穿。\n\n上一场比赛，葡萄牙完美地变阵打崩了瑞士队。这场比赛，葡萄牙希望用相同的套路在比赛的初期取得优势。\n\n于是，我们可以看到，在比赛一开场，葡萄牙的锋线就在不停地压迫摩洛哥人的后防。\n\n但是，变阵的效果只能打出一次出其不意的效果，第二次就没有可能了。\n\n上场比赛作为奇兵首发的贡萨洛·拉莫斯完成迷失在了亚特拉斯雄狮的丛林之中——在69分钟被替换下场时，0射正、0过人、0次关键传球、0次传中、0次对抗成功。\n\n“五零战士”的表现是五盾军团的一个缩影：\n\n相较于老冤家西班牙，葡萄牙的进攻的侵略性确实更强。然而，过于迷信上一次比赛成功经验的他们却忘记了保护自己漏洞百出的后防线。\n\n摩洛哥，恰恰就是那头喜欢用两只角把人顶死的狮子。\n\n在比赛60分钟左右的时候，我记得有一个数据：\n\n摩洛哥获得了10次进攻机会，转化成了八次射门机会。\n\n比赛第42分钟，欧纳希在前场绞杀葡萄牙成功，在上半场多次入侵达洛特防区的摩洛哥由叶海亚·阿拉左路完成斜四十五度的传中，恩·内斯里从一种不可思议的方式原地冲天，抓住小科斯塔的场均一失误CD用头将球砸入网窝。\n\n意识到苗头不对的桑托斯在下半场一开始就换上了C罗和坎塞洛试图加强进攻。但是，这二人上场之后，葡萄牙的进攻空间变得更加的堵塞，防守的空挡倒是无限变大，若非摩洛哥火枪手们的单刀实在过于欢乐，葡萄牙可能早就失去了扳平的希望。\n\n而迟暮的C罗，终于抑制不住再也机会触碰大力神杯的悲伤，泪洒球场。\n\n这个一生要强的男人，只身挺起葡萄牙足球六千余个日夜，终于等来了葡萄牙足球人才的井喷。\n\n只是，他再也没有机会见证葡萄牙足球的花开之时。\n\n看到C罗的泪水，相信众多C罗和葡萄牙球迷也难以自已。\n\n这些泪水汇流成河，带走了属于他们的青春。\n\n悲伤有时，快乐有时。\n\n创造非洲大陆新历史的摩洛哥众将随着球迷的欢呼声，再一次将主教练雷格拉古伊抛向空中：\n\n而摩洛哥边锋布法尔则与母亲在球场中央起舞，肆意庆祝由他们所创造的非洲足球新纪元。\n\n这是多么令人动容的那一刻！\n\n诸神落幕固然令人神伤，\n\n新传奇的开启难道也不令人欢愉吗！\n\n如同昨天的克罗地亚一样，足球场上没有必胜或者必败。\n\n只要永不放弃，心中常怀坚持与梦想，永不停歇地认真面对每一秒的战斗。\n\n奇迹，就一定会出现\n\nFootball, Bloody Hell!\n','2022-12-25 11:16:44',0,0,3,3);
  INSERT INTO `comment` VALUES (1,'在沙特打败阿根廷之前，不知道足球场上是几个人……在潘帕斯雄鹰击溃克罗地亚的时候，我已经在深夜中为阿根廷和梅西热泪盈眶了……这就是足球的魅力吧！内心总是希望这样的球队获胜，当家球星充满魅力且人品上佳，球队整体团结昂扬但又出身弱小。梅西辗转腾挪，点球助攻，阿尔瓦雷斯面带微笑，独中两元，潘帕斯雄鹰！！！稳稳的赢下了这一场胜利，愿梅西获得金球奖和金靴奖，为自己的足球生涯画上完美的句号！！','2022-12-25 10:45:27',1,1,1),(2,'克罗地亚防守策略是防传球路线，切断中路，不给阿根廷通过横传拉扯阵型，利用中路空挡的机会，全场基本成功了。不过阿根廷还是利用反击打进了球，也存在运气成分。最后一个是个人能力爆表，不讲理生吃中卫送饼成功，35岁老头能看出来吗？','2022-12-25 10:51:34',0,2,1),(3,'老板就不多说了，阿尔瓦雷斯真是福将','2022-12-25 11:13:44',0,3,1),(4,'为啥克罗地亚一反常态？不再防守，开始追求控球和进攻了。','2022-12-25 11:14:41',0,3,2);
 
INSERT INTO `activity` VALUES (1,'AENEA CON“LAST DANCE”足球主题潮流展','AENEACON是由国内首个专注于Z世代的潮流艺术馆AENEA Gallery发起的系列沉浸式体验潮流展览。AENEACON首个展览 “初来乍到” 球鞋潮流珍藏展，展出了价值数百万的收藏级球鞋，吸引万名观众观看。\n这次，由AENEA Gallery主理人CMAI策划，AENEACON又将带给观众：数百件球星亲签落场球衣藏品（*落场球衣指：球星在对应比赛中穿着的球衣），成套高稀有度球星签字折射球星卡，同时展出数名潮流艺术家创作的球鞋主题艺术作品','2022-12-11T16:00:00.000Z','2022-12-27T16:00:00.000Z','会议室','线下',2),(2,'音乐剧《桑塔露琪亚》镜框版','全程剧情快速推进，令人目不暇接3名演员分饰13个角色多种曲风带你领略大洋彼岸的城市风情共感剧中人物的爱情、友谊、嫉妒与别离','2022-12-19T16:00:00.000Z','2022-12-24T16:00:00.000Z','咖啡厅','线下',2);
INSERT INTO `bottle` VALUES (1,'多少事，从来急；天地转，光阴迫。一万年太久，只争朝夕。',1),(2,'天若有情天亦老，人间正道是沧桑。',1),(3,'踏遍青山人未老，风景这边独好。',1),(4,'男儿立志出乡关，学不成名誓不还！',1),(5,'自信人生二百年，会当水击三千里。',1),(6,'饭可以一日不吃，觉可以一日不睡，书不可以一日不读。',1),(7,'星星之火，可以燎原。',1),(8,'人不犯我，我不犯人;人若犯我，我必犯人!',1),(9,' 与天斗其乐无穷!与地斗其乐无穷!与人斗其乐无穷!',1),(10,'直到遇到足球，我的人生彻底改变，我很记得我第一个足球的样子，在我心里，它就像一颗糖果。',2),(11,'我要说我想一生都留在巴塞罗那。他们要我留这里多久，我就会留多久。我亏欠巴塞罗那的比他们给我的机会更多，我的生命是他们改变的。',2),(12,'历史对我紧追不舍，但我速度更快。',2),(13,'为了实现梦想，你必须奋斗；你必须做出牺牲，必须为之努力。',2),(14,'雄狮不会在乎绵羊的意见。',2),(15,'巴塞罗那是我永远无悔的俱乐部。',2),(16,'要相信自己，相信自己的家人，相信努力必有回报。有人问我足球如何成功时，我的脑子里只有自己对着墙壁一次次踢球和接球的场景。',2),(17,'有人把我和乔丹、博尔特和阿里这样的运动员相比较，这太疯狂了。我不喜欢比较，我应该和其他什么人比较呢？',2),(18,'为球衣胸前的名字而战，人们会记住它背后的名字。',2);
  INSERT INTO `tag` VALUES (1,'原神'),(2,'足球'),(3,'旅行'),(4,''),(5,'户外'),(6,'放松身心'),(7,'游戏'),(8,'第九艺术'),(9,'二次元'),(10,'恋与提瓦特'),(11,'运动'),(12,'世界杯'),(13,'欧冠'),(14,'冠军');
INSERT INTO `user_profile_pic` VALUES (1,1,'media/1.jpg'),(2,2,'media/2.jpg'),(3,3,'media/3.jpg');
    INSERT INTO `user_tag` VALUES (1,1),(1,2),(2,2),(3,2),(1,3),(3,3),(2,12),(2,14);
   INSERT INTO `group_tag` VALUES (1,3),(1,4),(1,5),(1,6),(2,7),(2,8),(2,9),(2,10),(3,11),(3,12),(3,13);
   INSERT INTO `user_group_score` VALUES (1,3,10),(2,3,8),(2,2,10),(2,1,10),(3,3,11);
   INSERT INTO `user_like_comment` VALUES (1,1);
    INSERT INTO `user_like_post` VALUES (1,1);
 