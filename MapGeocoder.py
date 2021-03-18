# -*- coding: utf-8 -*-
import requests
import json

# created by zhx, Mar 11 2021

class MapGeocoder:
    def __init__(self,maptype):
        self.api = ""
        self.params = {"output":"json"}
        self.maptype = maptype
        if maptype == "amap":
            self.api = "https://restapi.amap.com/v3/geocode/geo"
            self.params["key"] = "b98a92e6fcecfc44562894742997d455" #请申请自己的key
        elif maptype == "baidu":
            self.api = "http://api.map.baidu.com/geocoding/v3/"
            self.params["ak"] = "V3UzWARbsZlwDgHPcIwj3ZZ6hADloQGw"  #请申请自己的key
            self.params["ret_coordtype"] = "gcj02ll"
        elif maptype == "qq":
            self.api = "https://apis.map.qq.com/ws/geocoder/v1/"
            self.params["key"] = "DJABZ-WU3ER-BMXWM-WRY5Z-PJ5DH-LKFNK"  #请申请自己的key
        else:
            print "bad maptype"
            
    def SetAddress(self,address):
        self.params["address"]=address

    def GetResult(self):
        r = requests.get(self.api,self.params)
        js = json.loads(r.text)
        if self.maptype == "amap":
            if js['status'] == '1':  #高德成功状态
                geocodes = js[u'geocodes']
                if len(geocodes)==1: #高德输出为多个结果，取第一个
                    xy = geocodes[0]['location']
                    xs,ys = xy.split(",")
                    x,y = float(xs),float(ys)
                    level = geocodes[0]['level']  #字符串                                   
                    return x,y,level                
        elif self.maptype == "baidu":
            if js['status'] == 0:   #百度成功状态
                result = js[u'result']
                xy = result['location']
                x= xy["lng"]
                y= xy["lat"]
                level = result['level']  #字符串
                #precise = result['precise']
                #confidence = result['confidence']
                #comprehension = result['comprehension']
                return x,y,level                
        elif self.maptype == "qq":
            if js['status'] == 0:   #QQ成功状态
                result = js[u'result']
                xy = result['location']
                x= xy["lng"]
                y= xy["lat"]
                level = result['level']  #数值 0-11                
                return x,y,level 
        else:
            print "bad maptype"
        return 200,200,""
    

if __name__ == "__main__":
    maptype ="amap"
    address = u"成都市青羊区光耀二路381号"
    map_coder = MapGeocoder(maptype)
    map_coder.SetAddress(address)
    x,y,level = map_coder.GetResult()
    print maptype,address,x,y,level
    
    '''
    addressList = [u"成都市青羊区光耀二路381号",u"成都市龙泉驿区鲸龙路451号"]
    maptypeList = ["amap","baidu","qq"]
    for maptype in maptypeList:
        print maptype
        map_coder = MapGeocoder(maptype)
        for address in addressList:
            map_coder.SetAddress(address)
            x,y,level = map_coder.GetResult()
            print "\t",maptype,address,x,y,level
    '''    
