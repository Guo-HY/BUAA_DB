## 前后端交互API

- 前端保存userId作为用户标识。

## Home

![image-20221106232732210](assets/image-20221106232732210.png)

## 个人主页

![image-20221106231951650](assets/image-20221106231951650.png)

（字段先以下面为主，感觉还是先设计好并建好数据库，然后前端才能知道请求什么，这样更合理）

**修改或获取个人页面信息**

```json
url: '/api/changeUserInfo',
front->back
{
    "userId" : int,
	"userName" : string,
	"gender" : string,
	"age" : int,
	"birth" : string,
    "contact" : string,
    "address" : string
}
back->end
{
    "status" : string # success 或者 fail  可以忽略
}
```



```
url: '/api/userAddTag',
front->back
{
	"userId" : string
	"tagName" : string
}
back->front
{
	"status": string	# 可以忽略
}
```

```
url: '/api/getUserInfo',
front->end
{
	"userId" : int
}
end->front
{	
	"userName" : string
	"gender" : string
	"age" : string
	"birth" : string
	"contact" : string
	"dynamicTags" : list[string]
}
```

## 活动页面

![image-20221106232702339](assets/image-20221106232702339.png)

```
url: '/api/createActivity',
front->end
{
	"userId" : int
	"name" : string,
    "region" : string,
    "beginDate" : sting,
    "endDate" : string,
    "desc" : string,
    "activityNature" : string,
}
end->front
{
	"status" : string # 可以忽略
}
```

```
url: '/api/getActivity',
front->end
{
	
}
end->front
{
     activities:  list[ dict {
                name: string,
                region: string,
                beginDate: sting,
                endDate: string,
                desc: string,
                activitieNature: string,
       		 } ]
}
```

## 漂流瓶

```
url: '/api/receivedDriftBottleContent'
front->end
{
	"userId" : string
}
end->front
{
	"receivedDriftBottleContent" : string
}
```



## 登录页面

```
url: 'api/userLogin'
front->end
{
	"name" : string
	"password" : string
}
back->front
{
	"status": "success",
	"status": "not_found",
	"status": "password_wrong"
	"userId" : int
}
```



## 注册页面

```
url: 'api/userRegister'
front->end
{
	"name" : string,
	"password" : string,
	"contact" : string,	
    "age" : string,		
    "gender" : string,	
    "age" : string,		
    "address" : sting	
}
end->front
{
	"status" : "unknown_fail",	# 未知错误
	"status" : "name has an account registered. please log in."		# 已注册
	"status" : "success"		
}
```



## 社区页面

```
url: 'api/getHotGroupPic'
front-end
{
	"userId" : string
}
end->front
{
	"groups" : [
		{
			"groupId" : string, 
			"pic" : string,	# 先不实现
			"name" : string
		},
		
	]
}
```

```
url: 'api/getHotGroupIntro'
front->end
{
	"userId" : string
}
end->front
{
	"groups" : [
		{
			"groupId" : string, 
			"name" : string, 
			"desc" : string,
			"tags" : [ "xxx", "xxx"]
		},
	]
}
```

```
url: 'api/userAddGroup'
front->end
{
	"userId" : string
	"group_name" : string,
	"group_description" : string,
}
end->front
{
	"status" : "success"
}
```



## 圈子页面

```
url: 'api/getGroupInfo'
front->end
{
	"groupId" : string
}
end->front
{
	"group_name" : string,
	"group_description" : string,
	"post_num" : string,
	"create_user_name" : string,
	"tags" : [ "xxx", "xxx"],
	"posts" : [
		{
			"post_id" : string,
			"post_name" : string,
			"context" : string,
            "post_time" : string,
            "comment_num" : string,
            "likes_num" : string,
            "create_user_name" : string
		}
		
	]
}
```

```
url: 'api/userCreatePost'
front->end
{
	"userId" : string,
	"post_name" : string,
	"context" : string,
	"post_time" : sting
}
end->front
{
	"status" : "success"
}
```

```
url: 'api/userAddTagToGroup'
front->end
{
	"userId" : string,
	"groupId": string,
	"tagName" : string
}
end->front
{
	"status" : "success"
}
```





