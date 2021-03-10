import requests
import re
#获取图片列表
def getImagesList():
    #获取斗图网源代码
    html=requests.get('http://xyq.163.com/').text
    #data-webporiginal="https://xyq.res.netease.com/pc/gw/20170118103441/img/pop_img_95582ab.jpg"
    reg=r'data-webporiginal="(.*?)"'
    reg=re.findall(reg,re.S)
getImagesList()