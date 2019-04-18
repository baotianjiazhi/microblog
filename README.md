<h1>Hello！</h1>
<p>自己动手做一个Flask项目<p>
<h3>9-6</h3>
<p>大致实现了项目的主要功能,其中翻译和搜索的功能没有做</p>
<h3>使用</h3>
  <p>启动虚拟环境后，pip install -r requirements.txt</p>
  <p>配置文件按自己的需要进行修改，原教程数据库使用的是sqlite，我把配置改为了mysql，其中文本编辑器被我改成了ckeditor</p>

# 友情提示
配置文件中的一些内容需要做修改，比如
>SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:baobaobao123@127.0.0.1:3306/microblog"
需要修改为自己的数据库配置
