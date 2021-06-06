import vtk
import sys
from PyQt5 import QtCore, QtGui
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QFileDialog
from win import Ui_MainWindow
from PyQt5 import Qt
from vtk.util import numpy_support
import numpy as np

path='./data'
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

        ######################################Read Data##############################################
        reader = vtk.vtkDICOMImageReader()
        reader.SetDirectoryName(self.PathDicom)
        reader.Update()

        # Load dimensions using `GetDataExtent`
        _extent = reader.GetDataExtent()
        ConstPixelDims = [_extent[1]-_extent[0]+1, _extent[3]-_extent[2]+1, _extent[5]-_extent[4]+1]

        # Load spacing values
        ConstPixelSpacing = reader.GetPixelSpacing()

        # Get the 'vtkImageData' object from the reader
        imageData = reader.GetOutput()
        # Get the 'vtkPointData' object from the 'vtkImageData' object
        pointData = imageData.GetPointData()
        # Ensure that only one array exists within the 'vtkPointData' object
        assert (pointData.GetNumberOfArrays()==1)
        # Get the `vtkArray` (or whatever derived type) which is needed for the `numpy_support.vtk_to_numpy` function
        arrayData = pointData.GetArray(0)

        # Convert the `vtkArray` to a NumPy array
        ArrayDicom = numpy_support.vtk_to_numpy(arrayData)
        # Reshape the NumPy array to 3D using 'ConstPixelDims' as a 'shape'
        ArrayDicom = ArrayDicom.reshape(ConstPixelDims, order='F')
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
        self.iren.Start()
        self.iren.Initialize()
        self.show()

    def slider_SLOT(self,val):
        surfaceExtractor.SetValue(0, val)
        self.update()

    def update(self):
        self.iren.Update()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())