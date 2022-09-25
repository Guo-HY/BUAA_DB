- 使用json进行前后端交互。

## 数据库概念模式设计

### 实体E-R图

![学生实体E-R图.drawio](https://raw.githubusercontent.com/Guo-HY/picture_git/master/img/%E5%AD%A6%E7%94%9F%E5%AE%9E%E4%BD%93E-R%E5%9B%BE.drawio.svg)

![课程实体E-R图.drawio](https://raw.githubusercontent.com/Guo-HY/picture_git/master/img/%E8%AF%BE%E7%A8%8B%E5%AE%9E%E4%BD%93E-R%E5%9B%BE.drawio.svg)

### 联系E-R图

![联系E-R图](https://raw.githubusercontent.com/Guo-HY/picture_git/master/img/%E8%81%94%E7%B3%BBE-R%E5%9B%BE.svg)

## 逻辑模式设计

### 数据库关系模式

关系模式形式化表示为$R(U,D,DOM,F)$,$U$为组成该关系的属性名，$D$为U中属性所来自的域，$DOM$为属性与域的映射，$F$为属性间的依赖关系集合。约定$N$表示正整数，$FLOAT$表示浮点数，$L$为任意字符组成的字符串，$T$表示时间，$B$表示布尔值，主码以下划线标识，$*$代表一个实体中所有属性。

#### 实体

- 学生：$student<\{\underline{学号}，密码，用户名，年级，班级\}，D,DOM,F>$,其中$D=\{L,N\}$,$DOM=\{DOM(用户名)=L,DOM(学号)=N,DOM(密码)=N,DOM(年级)=N,DOM(班级)=N\}$,$F=\{学号 \rightarrow *\}$

- 课程：$course<\{\underline{课程ID}，课程名，课程介绍，课程容量，已选人数\},D,DOM,F>$,其中$D=\{N,L\}$,$DOM=\{DOM(课程ID)=N,DOM(课程名)=L,DOM(课程介绍)=L\}$，$F=\{课程ID\rightarrow *\}$

#### 联系

- 学生选择课程$student\_course<\{\underline{学生ID},\underline{课程ID}\},D,DOM,F>$

### 关系模式等级的判定与规范化

略



## 数据库基本表定义

### 实体表

#### 学生表 students

| 字段名称         | 数据类型 | 字段大小 | 必填字段 | 主键 | 外键 | 说明     |
| ---------------- | -------- | -------- | -------- | ---- | ---- | -------- |
| student_id       | int      | 20       | 是       | 是   | 否   | 学号     |
| student_password | varchar  | 255      | 是       | 否   | 否   | 登录密码 |
| student_username | varchar  | 255      | 是       | 否   | 否   | 用户名   |
| student_grade    | int      | 20       | 是       | 否   | 否   | 年级     |
| student_class    | int      | 20       | 是       | 否   | 否   | 班级     |

#### 课程表 courses

| 字段名称        | 数据类型 | 字段大小 | 必填字段 | 主键 | 外键 | 说明     |
| --------------- | -------- | -------- | -------- | ---- | ---- | -------- |
| course_id       | int      | 20       | 是       | 是   | 否   | 课程ID   |
| course_name     | varchar  | 255      | 是       | 否   | 否   | 课程名   |
| course_intro    | varchar  | 10000    | 是       | 否   | 否   | 课程评价 |
| course_capacity | int      | 20       | 是       | 否   | 否   | 课程容量 |
| course_elected  | int      | 20       | 是       | 否   | 否   | 已选人数 |

### 联系表

#### 学生选择课程 

| 字段名称   | 数据类型 | 字段大小 | 必填字段 | 主键 | 外键 | 说明   |
| ---------- | -------- | -------- | -------- | ---- | ---- | ------ |
| student_id | int      | 20       | 是       | 是   | 是   | 学号   |
| course_id  | int      | 20       | 是       | 是   | 是   | 课程id |

 	



## API

### studentRegister

frontend->backend

| key              | value | 说明 |
| ---------------- | ----- | ---- |
| student_id       | int   |      |
| student_password | char  |      |
| student_username | char  |      |
| student_grade    | int   |      |
| student_class    | int   |      |

backend->frontend

| key    | value   | 说明   |
| ------ | ------- | ------ |
| status | success | 字符串 |
|        | fail    |        |

### studentLogin

frontend->backend

| key              | value | 说明 |
| ---------------- | ----- | ---- |
| student_id       | int   |      |
| student_password | char  |      |

backend->frontend

| key    | value                  | 说明 |
| ------ | ---------------------- | ---- |
| status | success                |      |
|        | student_id_not_found   |      |
|        | student_password_wrong |      |

### studentCurriculum

frontend->backend

| key        | value |      |
| ---------- | ----- | ---- |
| student_id | int   |      |

backend->frontend

![932c91b05f62abda92ad48971ca0dc0](https://raw.githubusercontent.com/Guo-HY/picture_git/master/img/932c91b05f62abda92ad48971ca0dc0.png)

### studentCourseSelection

frontend->backend

| key        | value |      |
| ---------- | ----- | ---- |
| student_id | int   |      |
| course_id  | int   |      |

backend->frontend

| key    | value   |      |
| ------ | ------- | ---- |
| status | success |      |
|        | fail    |      |

### studentCoursePost

frontend->backend

| key        | value |      |
| ---------- | ----- | ---- |
| student_id | int   |      |

backend->frontend

![932c91b05f62abda92ad48971ca0dc0](https://raw.githubusercontent.com/Guo-HY/picture_git/master/img/932c91b05f62abda92ad48971ca0dc0.png)

### studentCourseWithdraw

frontend->backend

| key        | value |      |
| ---------- | ----- | ---- |
| student_id | int   |      |
| course_id  | int   |      |

backend->frontend

| key    | value   |      |
| ------ | ------- | ---- |
| status | success |      |
|        | fail    |      |