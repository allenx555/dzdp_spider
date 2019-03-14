# dzdp_spider

## 使用/测试
### 环境安装
1. 安装python3，pip
2. 建议使用虚拟环境安装必要库，在目录下执行 `pip install -r requirements.txt`
3. 建议使用 mysql 数据库，若本地暂无安装，可以将`./config.py`中`app.config.from_pyfile('config.py')`一行删去，若已安装，进入`./instance/config.py`将账户及密码改为本地 mysql 账户密码

### 运行
1. 进入`./dzdp_spider/spider/spider.py`，在第 88 行将`r''`中的内容改为本地大众点评 cookie
2. 爬虫入口为 `./run.py`
