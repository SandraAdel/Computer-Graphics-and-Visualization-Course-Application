import vtk
import sys
from PyQt5 import QtCore, QtGui
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QFileDialog
from win import Ui_MainWindow
from PyQt5 import Qt
from vtk.util import numpy_support

path='./data'
dataDir = 'headsq/quarter'
surfaceExtractor = vtk.vtkContourFilter()

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.PathDicom =''
        self.pushButton.clicked.connect(self.openDICOM)
        self.slider.valueChanged.connect(self.slider_SLOT)
    
    def openDICOM(self):
        fname=QFileDialog.getExistingDirectory(self, 'Open folder',path)
        self.PathDicom = fname
        print(fname)
        self.OpenVTK()

    def OpenVTK(self):

        self.vtkWidget = QVTKRenderWindowInteractor(self.frame)
        self.vl = Qt.QVBoxLayout() 
        self.vl.addWidget(self.vtkWidget)

        self.ren = vtk.vtkRenderer()
        self.vtkWidget.GetRenderWindow().AddRenderer(self.ren)
        self.iren = self.vtkWidget.GetRenderWindow().GetInteractor()


        # v16 = vtk.vtkVolume16Reader()
        # v16.SetDataDimensions(64, 64)
        # v16.SetDataByteOrderToLittleEndian()
        # v16.SetFilePrefix(dataDir)
        # v16.SetImageRange(1, 93)
        # v16.SetDataSpacing(3.2, 3.2, 1.5)
        ######################################Read Data##############################################
        reader = vtk.vtkDICOMImageReader()
        reader.SetDataByteOrderToLittleEndian()
        reader.SetDirectoryName(self.PathDicom)
        reader.Update()

        #########################################################################################

        # surfaceExtractor.SetInputConnection(v16.GetOutputPort())
        surfaceExtractor.SetInputConnection(reader.GetOutputPort())
        surfaceExtractor.SetValue(0, 500)
        surfaceNormals = vtk.vtkPolyDataNormals()
        surfaceNormals.SetInputConnection(surfaceExtractor.GetOutputPort())
        surfaceNormals.SetFeatureAngle(60.0)
        surfaceMapper = vtk.vtkPolyDataMapper()
        surfaceMapper.SetInputConnection(surfaceNormals.GetOutputPort())
        surfaceMapper.ScalarVisibilityOff()
        surface = vtk.vtkActor()
        surface.SetMapper(surfaceMapper)
 
        aCamera = vtk.vtkCamera()
        aCamera.SetViewUp(0, 0, -1)
        aCamera.SetPosition(0, 1, 0)
        aCamera.SetFocalPoint(0, 0, 0)
        aCamera.ComputeViewPlaneNormal()
        
        self.ren.AddActor(surface)
        self.ren.SetActiveCamera(aCamera)
        self.ren.ResetCamera()
        self.ren.SetBackground(0, 0, 0)
        self.ren.ResetCameraClippingRange()

        self.frame.setLayout(self.vl)
        self.vtkWidget.Initialize()
        self.vtkWidget.GetRenderWindow().Render()
        self.vtkWidget.Start()
        self.vtkWidget.show()

    def slider_SLOT(self,val):
        surfaceExtractor.SetValue(0, val)
        self.vtkWidget.update()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())