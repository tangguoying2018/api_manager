### 项目介绍
----------

该项目本来是 gongwalker 使用PHP写的，原项目地址:  
https://github.com/gongwalker/ApiManager  

现在做为个人python练手项目，所以就把它改成python版本了，改得有点粗糙，有需要的小伙伴可以拿去耍耍~   
当然，如果有小伙伴能贡献代码，完善或加入更多功能那就更好了~   

与原项目相比：  
1. 数据库加了新字段  
2. api参数存储字段数据格式不同了  
3. 用户管理使用django默认  
4. 权限管理 - 需要登陆用户才能看到分类及接口相关内容  
5. 基本功能与原版一致    

### 部署简单说明
----------

项目部署工具：  
nginx + supervisor + gunicorn


1. 创建虚拟化环境  

```
virtualenv env
```
    
2. 安装必要的信赖包

```
yum install libffi-devel mysql-devel
env/bin/pip install -r requirements.txt
```

3. 配置supervisor

安装supervisor(centos7)

```
yum install supervisor 
```

4. 修改 supervisord.conf 文件

修改或增加以下内容：

```
[include]
files = /etc/supervisor/conf.d/*.conf /path/to/api_manager/config/*.ini
```

5. 配置数据库

配置文件：settings.py

```
DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # }
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "api_manager",          #数据库
        "USER": "api_manager_user",     #数据库帐号
        "PASSWORD": "api_manager_PASS_123",  #数据库密码
    }
}
```

6. 初始化数据库

```
env/bin/python manage.py makemigrations app 
env/bin/python manage.py migrate
```

7. 创建用户

```
env/bin/python manage.py createsuperuser
```

### 静态文件简单说明
----------

配置：  
STATIC_ROOT = os.path.join(BASE_DIR, 'collec_static/')  

运行以下命令:  

``` python
python manage.py collectstatic 
```

注：这条命令会把所有静态文件复制到 collec_static/ 目录下面，当debug=False时，这个静态文件目录才生效，当debug=True时，会使用以下静态文件配置： STATICFILES_DIRS

### 开发时使用指定的开发环境变量
----------

``` python
python manage.py runserver --settings=api_manager.settings_dev
```

### 最后 - 相关截图

![image](https://raw.githubusercontent.com/tangguoying2018/api_manager/master/screenshots/1.png)
![image](https://raw.githubusercontent.com/tangguoying2018/api_manager/master/screenshots/2.png)
![image](https://raw.githubusercontent.com/tangguoying2018/api_manager/master/screenshots/3.png)
![image](https://raw.githubusercontent.com/tangguoying2018/api_manager/master/screenshots/4.png)
![image](https://raw.githubusercontent.com/tangguoying2018/api_manager/master/screenshots/5.png)
