## 前后端交互API

#### backend_binary_reply

```json
{
	"status" : "success",
	"status" : "fail"
}
```

### 登录/注册页面

#### user_login

##### frontend->backend

```json
{
    "name": " xxx",
    "password": "xxx"
}
```

##### backend->frontend

```json
{
	"status": "success",
	"status": "not_found",
	"status": "password_wrong"
}
```

#### user_register

##### frontend->backend

```json
{
	"name" : "xxx",
	"password" : "xxx",
	"contact" : "xxx",
    "age" : "xxx",
    "major" : "xxx",
}
```

##### backend->frontend

```json
{
	"status": "success",
	"status": "name has an account registered. please log in.",
}
```

#### 



### 个人主页

#### user_upload_portrait

##### frontend->backend

http://t.zoukankan.com/danhuai-p-15720760.html

##### backend->frontend

backend_binary_reply

#### user_modify_contact

##### frontend->backend

```jaon
{
	"name" : "xxx"
	"contact" : "xxx"
}
```

##### backend->frontend

backend_binary_reply



#### get_user_friends

##### frontend->backend

```json
{
	"name" : "xxx",
}
```

##### backend->frontend

```json
{
	"friends" : ["name1", "name2", ... "namen"]
}
```



#### get_user_bottles_history

##### frontend->backend

```json
{
	"name" : "xxx",
}
```

##### backend->frontend

```json
{
	"mybottles" : ["context1", "context2", ... "contextn"],
    "myReplyBottles" : [{
        "context" : "xxx",
        "reply" : "xxx"
    },
    {
      "context" : "xxx",
      "reply" : "xxx"                 
    },        
                        ...
                       ]
}
```



#### get_user_activities

##### frontend->backend

```json
{
	"name" : "xxx",
}
```

##### backend->frontend

```json
{
	"join": ["name"],
	"follow" : ["name"],
	"create" : ["name"]
}
```



#### add_user_tag

##### frontend->backend





## 11.6

## Home

![image-20221106232732210](../../../../大作业一/后端提交/BUAA_DB/pictures/image-20221106232732210.png)

## 个人主页

![image-20221106232757578](../../../../大作业一/后端提交/BUAA_DB/pictures/image-20221106232757578.png)

（字段先以下面为主，感觉还是先设计好并建好数据库，然后前端才能知道请求什么，这样更合理）

**修改或获取个人页面信息**

```
url: '/api/changeUserInfo',
{
	"userName" : string
	"gender" : string
	"age" : string
	"birth" : string
	"dynamicTags" : list
}
```

```
url: '/api/getUserInfo',
{
	"userId"
	"userName" : string
	"gender" : string
	"age" : string
	"birth" : string
	"dynamicTags" : list
}
```

## 活动页面

![image-20221106232702339](../../../../大作业一/后端提交/BUAA_DB/pictures/image-20221106232702339.png)

```
url: '/api/createActivity',
{
	name: '',
    region: '',
    date1: '',
    date2: '',
    delivery: false,
    type: [],
    resource: '',
    desc: ''
}
```

```
url: '/api/getActivity',
{
     activities:   dict {
                name: '',
                region: '',
                date1: '',
                date2: '',
                delivery: false,
                type: [],
                resource: '',
                desc: ''
       		 }
}
```

