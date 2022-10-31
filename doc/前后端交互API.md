## 前后端交互API

#### backend_binary_reply

```json
{
	"status" : "success",
	"status" : "fail"
}
```

### 用户信息管理模块

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
	"contact" : "xxx"
}
```

##### backend->frontend

backend_binary_reply



#### user_upload_portrait

##### frontend->backend

http://t.zoukankan.com/danhuai-p-15720760.html

##### backend->frontend

backend_binary_reply

#### user_modify_contact

##### frontend->backend

```jaon
{
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



#### get_user_acticvities

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





