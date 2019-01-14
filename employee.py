from PyQt5 import uic, QtWidgets
import sys

class Interface(QtWidgets.QMainWindow):
    def __init__(self):
        super(Interface,self).__init__()
        uic.loadUi('employeeGUI.ui',self)
        self.pushButton_add.clicked.connect(self.add)
        self.pushButton_edit.clicked.connect(self.edit)
        self.pushButton_remove.clicked.connect(self.remove)
        self.pushButton_up.clicked.connect(self.up)
        self.pushButton_down.clicked.connect(self.down)
        self.pushButton_sort.clicked.connect(self.sort)
        self.pushButton_close.clicked.connect(self.close)

        self.Employee()

    def sort(self):
        self.listWidget.sort()

    def close(self):
        quit()

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

    def remove(self):
        row = self.listWidget.currentRow()
        item = self.listWidget.item(row)
        if item is None:
            return
        reply = QtWidgets.QMessageBox.question(self,"Remove Employee","Do you want to remove employee "+item.text(),QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            item = self.listWidget.takeItem(row)
            del item

    def up(self):
        row = self.listWidget.currentRow()

        if row >= 1:
            item = self.listWidget.takeItem(row)
            self.listWidget.insertItem(row -1, item)
            self.listWidget.setCurrentItem(item)

    def down(self):
        row = self.listWidget.currentRow()
        #self.listWidget.


        if row < self.listWidget.count()-1:
            item = self.listWidget.takeItem(row)
            self.listWidget.insertItem(row +1, item)
            self.listWidget.setCurrentItem(item)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    e = Interface()
    e.show()
    sys.exit(app.exec_())
