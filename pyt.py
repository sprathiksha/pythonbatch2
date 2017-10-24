Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> d="ab=c;def=ghi"
>>> vp=dict(item.split("=") for item in d.split(";"))
>>> vp
{'ab': 'c', 'def': 'ghi'}
>>> 
