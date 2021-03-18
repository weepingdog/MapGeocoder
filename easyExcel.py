# -*- coding: utf-8 -*-
from win32com.client import Dispatch
import win32com.client

#copy from somewhere by zhx
# 功能：windows环境下的excel操作
# 1. 读写excel操作需要pywin32
#    pywin32：[https://github.com/mhammond/pywin32/releases/tag/b227]
# 2. 需要使用excel文件的完整路径
# 3. 只支持97-2000文件（后缀.xls）
# 4. 下标均从1开始

class easyExcel:
    """A utility to make it easier to get at Excel.    Remembering  
      to save the data is your problem, as is    error handling.  
      Operates on one workbook at a time."""
    def __init__(self,filename = None):
        self.xlApp = win32com.client.Dispatch("Excel.Application")
        if filename:
            self.filename = filename
            self.xlBook = self.xlApp.Workbooks.Open(filename)
        else:
            self.xlBook = self.xlApp.Workbooks.Add()
            self.filename = ""
    def save(self,newfilename = None):
        if newfilename:
            self.filename = newfilename
            self.xlBook.SaveAs(newfilename)
        else:
            self.xlBook.Save()
    def close(self):
        self.xlBook.Close(SaveChanges = 0)
        del self.xlApp
    def getCell(self,sheet,row,col):
        "Get value of one cell"
        sht = self.xlBook.Worksheets(sheet)
        return sht.Cells(row,col).Value
    def setCell(self,sheet,row,col,value):
        "Set value of one cell"
        sht = self.xlBook.Worksheets(sheet)
        sht.Cells(row,col).Value = value        
    def getRange(self,sheet,row1,col1,row2,col2):
        "----"
        sht = self.xlBook.Worksheets(sheet)
        return sht.Range(sht.Cells(row1,col1),sht.Cells(row2,col2)).Value
    def addPicture(self,sheet,pictureName,left,top,width,height):
        "x"
        sht = self.xlBook.Worksheets(sheet)
        sht.Shapes.AddPicture(pictureName,1,1,left,top,width,height)
    def cpSheet(self):
        "copy sheet"
        shts = self.xlBook.WorkSheets
        shts(1).Copy(None,shts(1))
