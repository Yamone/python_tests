# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
url = 'http://www.lumine.ne.jp/xml/cms_shop.xml?_=1559751604138'
try:
    # resp = 
    resp = requests.get(url)
    resp.encoding = 'utf-8' # Optional: requests infers this internally
    respData = resp.text
    html = BeautifulSoup(respData, "html.parser")
    for shopinfo in html.find_all('shopinfo'):
        print(f'id : {shopinfo.id.text}')
        print(f'date : {shopinfo.print_date.text}')
        d = shopinfo.shop_info.image.next.rstrip()
        print(f'image : http://www.lumine.ne.jp/pict/{d}')
        title = shopinfo.title.text
        print(f'title : {title}')
        print("")
  
    
except Exception as e:
    print(str(e))

print("press any to exist")
x = input("")