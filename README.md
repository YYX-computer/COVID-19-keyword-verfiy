# COVID-19-keyword-verfiy

![covid19_img1](https://img-blog.csdnimg.cn/20200402222421113.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80Mjk1NDYxNQ==)
![covid19_img2](https://img-blog.csdnimg.cn/20200402222908373.png)

In the COVID-19,we got a difficultly problem:the Info-padenmic.

Run this code to verify a keyword that you want to know the truth.

This code will tell you the keywords truth.

Run this:
```
sudo pip install -r requests.txt
python keyword_verify.py
```

*Please add your trusted info-source:*

*change the code:'keyword_verify'*

*change:*
```
# -*- encoding:utf-8 -*-
import requests as r
import Tkinter as tk
urls = []   #change this line,add the trust url in 'urls'!
def get():
```
