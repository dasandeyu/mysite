[参考文档地址](https://docs.djangoproject.com/zh-hans/3.1/intro/tutorial01/#)

# 常用命令
1. 创建项目
    - django-admin.py startproject mysite
2. 启动开发服务器
    - python manage.py runserver 8080
    - python manage.py runserver 0.0.0.0:8000
3. 创建一个应用
    - python manage.py startapp polls

# 配置mysql数据库
1. 安装mysqlclient客户端。
2. 修改setting文件中的DATABASES配置，在运行之前需要先创建数据库。本项目创建的数据库mysite。
3. django对模型进行检测，并且将修改部分存储为一次迁移
    - python manage.py makemigrations polls
4. 将迁移需要执行的命令打印到屏幕
    - python manage.py sqlmigrate polls 0001
5. 应用迁移
    - python manage.py migrate  
6. 创建超级管理员 
    - python manage.py createsuperuser
    > 当前超级管理员配置  
      username:lanxiang_sh  
      Email:lanxiang_sh@ushareit.com  
      password:0