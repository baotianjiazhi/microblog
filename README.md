# Hello！
自己动手做一个Flask项目
### 9-6
大致实现了项目的主要功能,其中翻译和搜索的功能没有做

### 使用

  ### 配置python环境

  启动虚拟环境后，pip install -r requirements.txt

  ### 配置文件修改

  在配置文件`config.py`中修改配置文件

  > 将 SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:baobaobao123@127.0.0.1:3306/microblog" 替换为自己的数据库配置信息：基本格式为user:password@host:port/database_name

  email配置内容看自己的需要修改，当时在做的过程中如果直接使用国内一些邮箱会被认定为发送垃圾邮件，如果有合适的解决办法，我会在后面进行修改

  配置文件按自己的需要进行修改，原教程数据库使用的是sqlite，我把配置改为了mysql，其中文本编辑器被我改成了ckeditor

  ### 数据库迁移

  博客使用的是sqlalchemy+pymysql配置数据库，所以在使用之前需要自己手动迁移，启动虚拟环境之后输入

  ```flask db init```
  初始化数据库

  ```flask db migrate```
  生成迁移文件

  ```flask db upgrade```
  数据库迁移，数据库在迁移完成后，运行`microblog.py`即可在`127.0.0.1:5000`查看