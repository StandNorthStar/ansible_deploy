# 安装须知:
必须先在节点安装 libselinux-python ，不然无法传输文件
* 本安装包仅仅限于新建安装,不支持升级.如果升级会删除数据库.
  - 如果要升级,请注释创建数据库脚本语句中drop database XX 信息.
* inventory/hosts 添加机器请填写IP,不要使用主机名.
  - openfalcon-agent下会获取里面的IP,只要保证此组下是IP.

