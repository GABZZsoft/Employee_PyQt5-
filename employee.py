from PyQt5 import uic, QtWidgets
import sys

class Interface(QtWidgets.QMainWindow):
    def __init__(self):
        super(Interface,self).__init__()
        uic.loadUi('employeeGUI.ui',self)
        self.pushButton_add.clicked.connect(self.add)
        self.pushButton_edit.clicked.connect(self.edit)
        self.Employee()

    def Employee(self):
        self.emp = ["Garuba", "Malik", "Soladayo"]
        self.listWidget.addItems(self.emp)
        self.listWidget.setCurrentRow(0)

    def add(self):
        row = self.listWidget.currentRow()
        text, ok = QtWidgets.QInputDialog.getText(self, "Employe Dialog", "Enter Employee Name")

        if ok and text is not None:
            self.listWidget.insertItem(row, text)

    def edit(self):
        row = self.listWidget.currentRow()
        Item = self.listWidget.item(row)
        text,ok = QtWidgets.QInputDialog.getText(self, "Employee Dialog", "Edit Employee "+Item.text())
        if ok and text is not None:
            Item.setText(text)
            #self.listWidget.insertItem(row, text)

    def onclick_add(self):
        pass

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    e = Interface()
    e.show()
    sys.exit(app.exec_())
