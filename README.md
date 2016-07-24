# Htai.me 本子采集器

自动采集htai.me(当时还不知道有E绅士这个东西，所以写了这个...)上的本子信息，并使用selenium控制chorme下载云盘分享文件,并完成重命名解压缩包密码。

## 实现思路
http://blog.nanguage.org/wordpress/2016/07/06/%E7%BB%85%E5%A3%AB%E6%9C%AC%E5%AD%90%E9%87%87%E9%9B%86%E5%99%A8/
## 食用方法
### 解决库依赖
```
pip3 install -r requirements.txt
```
### 修改配置
所有配置均位于configer.py中，一般来说只需要修改start_page 与 end_page两个变量，对应要下载htai.me上的起始与终止页号。main_page 对应起始页面，zip_passwd 对应解压密码。download_path 为本地保存地址。
### 运行
修改配置后运行main.py开始爬取。
```
python3 main.py
```
