# Original sources Copyright (c) 2006 by Tim Sutton
#
# ported to Python by Martin Dobias
#
# licensed under the terms of GNU GPL 2

from PyQt4 import QtCore, QtGui
from mainwindow_ui import Ui_MainWindow
from qgis.core import *
from qgis.gui import *
import sys
import os
import urllib2
from xml.dom.minidom import parse, parseString
import pdb
qgis_prefix = os.getenv( "QGISHOME" )

class PointLayer:
    def __init__(self, name, fields):
        self.name = name
        self.layer = QgsVectorLayer("Point?crs=epsg:4326", name, "memory")
        self.provider = self.layer.dataProvider()
        self.fields = fields
        self.AddFields(fields)
        self.layer.updateFieldMap()
        self.layer.setDisplayField(name)
        self.provider.createSpatialIndex()
        QgsMapLayerRegistry.instance().addMapLayer(self.layer)   
        # result = QObject.connect(self.pinLayer, SIGNAL("layerDeleted()"), self.layer_deleted)        
    def AddFields(self,fields):
        attributes = list()
        for s in fields:
            attributes.append(QgsField(s,QtCore.QVariant.String))
        self.provider.addAttributes(attributes)  

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

        # required by Qt4 to initialize the UI
        self.setupUi(self)

        # create map canvas
        self.canvas = QgsMapCanvas()
        self.canvas.setCanvasColor(QtGui.QColor(255,255,255))
        self.canvas.enableAntiAliasing(True)
        self.canvas.show()

        # lay our widgets out in the main window
        self.layout = QtGui.QVBoxLayout(self.frameMap)
        self.layout.addWidget(self.canvas)

        # create the actions behaviours
        self.connect(self.mpActionAddLayer, QtCore.SIGNAL("triggered()"), self.addLayer)
        self.connect(self.mpActionZoomIn, QtCore.SIGNAL("triggered()"), self.zoomIn)
        self.connect(self.mpActionZoomOut, QtCore.SIGNAL("triggered()"), self.zoomOut)
        self.connect(self.mpActionPan, QtCore.SIGNAL("triggered()"), self.pan)

        # create a little toolbar
        self.toolbar = self.addToolBar("File");
        self.toolbar.addAction(self.mpActionAddLayer);
        self.toolbar.addAction(self.mpActionZoomIn);
        self.toolbar.addAction(self.mpActionZoomOut);
        self.toolbar.addAction(self.mpActionPan);

        # create the map tools
        self.toolPan = QgsMapToolPan(self.canvas)
        self.toolPan.setAction(self.mpActionPan)
        self.toolZoomIn = QgsMapToolZoom(self.canvas, False) # false = in
        self.toolZoomIn.setAction(self.mpActionZoomIn)
        self.toolZoomOut = QgsMapToolZoom(self.canvas, True) # true = out
        self.toolZoomOut.setAction(self.mpActionZoomOut)


    def zoomIn(self):
        self.canvas.setMapTool(self.toolZoomIn)

    def zoomOut(self):
        self.canvas.setMapTool(self.toolZoomOut)

    def pan(self):
        self.canvas.setMapTool(self.toolPan)

    def addLayer(self):
        """add a (hardcoded) layer and zoom to its extent"""

        layerPath = "../data/GSHHS_i_L2.shp"
        layerName = "test"
        layerProvider = "ogr"

        # create layer
        layer = QgsVectorLayer(layerPath, layerName, layerProvider)
        print layer.isValid()
        if not layer.isValid():
          return
        # add layer to the registry
        QgsMapLayerRegistry.instance().addMapLayer(layer);
        # set extent to the extent of our layer
        self.canvas.setExtent(layer.extent())
        # set the map canvas layer set
        cl = QgsMapCanvasLayer(layer)
        # create layer1
        layerPath = "../data/GSHHS_i_L1.shp"
        layerName = "test1"
        layerProvider = "ogr"        
        layer1 = QgsVectorLayer(layerPath, layerName, layerProvider)
        if not layer.isValid():
          return
        # add layer to the registry
        QgsMapLayerRegistry.instance().addMapLayer(layer1);
        # set extent to the extent of our layer
        self.canvas.setExtent(layer1.extent())
        # set the map canvas layer set
        cl2 = QgsMapCanvasLayer(layer1)        
        
        self.boat_layer = PointLayer("Boats", ['id', 'x','y'])
        cl1 = QgsMapCanvasLayer(self.boat_layer.layer)
        layers = [cl,cl1,cl2]
        # layers = [cl1]
        self.canvas.setLayerSet(layers)
          
        self.FillInBoatLayer()
	def LoadLayerFromFile (self,path)
		pass
    def FillInBoatLayer(self):
        # if not self.have_boat_layer:
            # return
        f = urllib2.urlopen('http://gae.yb.tl/Flash/nb2012/LatestPositions/?rnd=31073')
        dom = parse(f)
        features = list()
        count = 0
        for team in dom.getElementsByTagName('team'):
            print team.toxml()
            # fc = int(self.boat_layer.provider.featureCount())
            id = team.attributes['id'].value
            pos =  team.getElementsByTagName('pos')[0]
            lat =  pos.attributes["o"].value
            lon =  pos.attributes["a"].value
            # print fc, id, lat, lon
            # QtGui.QMessageBox.information(self,"LatLon", "lat: %s  lon: %s"%(lat,lon)) 
            point = QgsPoint(float(lat),float(lon)) 
            feature = QgsFeature()
            feature.setGeometry(QgsGeometry.fromPoint(point))
            feature.setAttributeMap( { 0 : QtCore.QVariant(str(id)),
                                       1 : QtCore.QVariant(str(lat)),
                                       2 : QtCore.QVariant(str(lon)) })
            # print feature.setAttributeMap
            features.append(feature)
        self.boat_layer.provider.addFeatures(features)
        self.boat_layer.layer.updateExtents()
        self.boat_layer.layer.setCacheImage(None)
        self.canvas.refresh()
        # count += 1
        # if count >10:
            # break

def main(app):
    # initialize qgis libraries
    QgsApplication.setPrefixPath(qgis_prefix, True)
    QgsApplication.initQgis()
    # create main window
    wnd = MainWindow()
    wnd.show()
    # run!
    retval = app.exec_()
    # exit
    QgsApplication.exitQgis()
    sys.exit(retval)
if __name__ == "__main__":
# create Qt application
    app = QtGui.QApplication(sys.argv)
    main(app)

