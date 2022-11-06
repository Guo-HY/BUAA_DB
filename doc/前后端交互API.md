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





