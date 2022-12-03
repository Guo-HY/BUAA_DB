# BUAA_DB2

## 运行项目

- 在mysql终端中使用source命令运行`src/backend/database.sql`脚本可以初始化数据库与表。
- 更改`src/buaa_db/settings.py`中的`DATABASE_KEY`为数据库root账户登录密码
- 在`src/`目录下使用`python manage.py runserver`命令运行后端服务
- 在`src/frontend`目录下运行`npm install`安装所需`node_modules`
- 在`src/frontend`目录下使用`npm run serve`运行前端服务