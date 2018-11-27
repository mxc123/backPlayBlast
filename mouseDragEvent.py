#!usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@author:MCC
@file: mouseDragEvent
@time: 2018/11/22 19:05
"""
import sys
import os
import subprocess
sys.path.append(r'C:\cgteamwork\bin\lib\pyside')
from PySide import QtGui
def _getFilePath(urls):
    if '///' in urls.toString():
        filePath = urls.toString().split('///')[-1]
        return filePath
    elif '///' not in urls.toString():
        filePath = urls.toString()[1:]
        return filePath

class My_ListWidget(QtGui.QListWidget):
    def __init__(self,parent = None):
        super(My_ListWidget,self).__init__(parent)
        self._parent = parent
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        self.information=[]
        data = event.mimeData()
        urls = data.urls()
        if (urls and urls[0].scheme() == 'file'):
            event.acceptProposedAction()

    def dragMoveEvent(self,event):
        data = event.mimeData()
        urls = data.urls()
        if (urls and urls[0].scheme() == 'file'):
            event.acceptProposedAction()

    def dropEvent(self, event):
        data = event.mimeData()
        urls = data.urls()
        if (urls and urls[0].scheme() == 'file'):
            urls[0].setScheme("")
            for uu in urls:
                uu=_getFilePath(uu)
                self.information.append(uu)
        for ii in self.information:
            items = QtGui.QListWidgetItem(ii)
            self._parent.listWidget.addItem(items)




