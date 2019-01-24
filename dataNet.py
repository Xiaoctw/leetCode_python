# import requests
# r=requests.get("http://www.baidu.com")
# r.status_code
import requests
from bs4 import BeautifulSoup
r=requests.get("http://www.baidu.com")
print(r.status_code)#状态码
print(r.encoding)#编码
#print(r.text)#内容
