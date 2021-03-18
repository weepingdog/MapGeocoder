# -*- coding: utf-8 -*-
import os

#import time
#import random
#time.sleep(random.randint(1,2))

from gcs2wgs84 import gcj02towgs84
from easyExcel import easyExcel
from MapGeocoder import MapGeocoder


ftxt = open("sc_baidu.txt","w")

fp = u"C:\\Users\\zhx\\Documents\\GitHub\\MapGeocoder\\四川省乡镇行政区划简册.xls"
print fp
xls = easyExcel(fp)

map_coder = MapGeocoder("baidu")
i = 2
t4 = xls.getCell("Sheet1",i,4)
while t4:
    t1 = xls.getCell("Sheet1",i,1)
    t2 = xls.getCell("Sheet1",i,2)
    t3 = xls.getCell("Sheet1",i,3)
    #t4 = xls.getCell("Sheet1",i,4)
    t5 = xls.getCell("Sheet1",i,5)
    t6 = xls.getCell("Sheet1",i,6)
    t7 = xls.getCell("Sheet1",i,7)
    if t1!=None:
        ds=t1.replace("\n","")
    if t2!=None:
        qx=t2.replace("\n","")    
    if t7 == u"驻地无变化":
        print i,ds,qx,t4
    else:
        address = ""
        if t7==None or t7=="":
            address = ds+qx+t4
        else:
            address = ds+qx+t4+t7
        map_coder.SetAddress(address)
        x,y,level = map_coder.GetResult()
        time.sleep(0.1*random.randint(1,2)) #停顿，以防被ban
        x2,y2 = gcj02towgs84(x,y)
        print i,ds,qx,t4,t7,x,y,level,x2,y2
        longtxt = u"{0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11}\n".format(i,ds,qx,t3,t4,int(t5),t7,x,y,level,x2,y2)
        try:
            ftxt.write(longtxt.encode("cp936"))
        except:
            longtxt = u"{0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11}\n".format(i,ds,qx,t3,"===",int(t5),t7,x,y,level,x2,y2)
            ftxt.write(longtxt.encode("cp936"))
    i+=1
    t4 = xls.getCell("Sheet1",i,4)  
xls.close()
ftxt.close()
