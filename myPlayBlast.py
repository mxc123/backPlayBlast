
#!usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@author:MCC
@file: myPlayBlast
@time: 2018/11/22 19:04
"""
import os
import maya.cmds as cmds

def getFrameRange():
    startTime = cmds.playbackOptions(q = True,min = True)
    endTime = cmds.playbackOptions(q = True,max = True)
    return [int(startTime),int(endTime)]



def RunExport(path, publishPath=''):
    cmds.file(path, o=1, f=1)
    # cmds.loadPlugin("animImportExport")
    #
    videosPath = os.path.dirname(path)
    videosName = os.path.basename(path).split(".")[0]
    # name = os.path.basename(path).split(".")[0]
    # geoList = getObject()
    # nurbsCurvesList=selectNurbsCurve()
    # print "+++++++++++++++",geoList
    # bakeAnimation(nurbsCurvesList,frameRange[0],frameRange[1])
    # cmds.select(geoList[0])
    # fileDirs = abcPath+"/%s" % name
    # exportAnmiCurve("%s.anim"%fileDirs)
    movPath = "%s/%s.mov"%(videosPath,videosName)
    cmds.playblast(filename=movPath, format="qt", sequenceTime=0,\
                   clearCache=1, \
                   viewer=0, \
                   showOrnaments=1, \
                   fp=4, \
                   fo=1,\
                   percent=100, \
                   compression="Video", \
                   quality=100, widthHeight=[1080, 720])




