#用Python实现下载www.bluecore.com.cn的首页HTML
import requests
response = requests.get('http://www.bluecore.com.cn')
print(response.content.decode('utf-8'))
