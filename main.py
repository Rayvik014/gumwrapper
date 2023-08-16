import os
from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import (
    QMainWindow,
    QApplication,
    QWidget,
)
from PySide6.QtGui import (
    QAction,
    QIcon,
)

class Wrapperwindow(QWidget):
    def __init__(self):
        super().__init__()

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.bar = self.addToolBar("Menu")
        self.bar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.refresh_action = QAction(self, text="Refresh All")
        self.refresh_action.setIcon(QIcon(f"{os.path.abspath(os.getcwd())}/icons/icons8-refresh-40.png"))
        self.refresh_action.triggered.connect(self.refresh_clicked)
        self.bar.addAction(self.refresh_action)

        self.clear_action = QAction(self, text="Clear All")
        self.clear_action.setIcon(QIcon(f"{os.path.abspath(os.getcwd())}/icons/icons8-erase-40.png"))
        self.clear_action.triggered.connect(self.clear_clicked)
        self.bar.addAction(self.clear_action)

        self.print_action = QAction(self, text="Print All")
        self.print_action.setIcon(QIcon(f"{os.path.abspath(os.getcwd())}/icons/icons8-print-40.png"))
        self.print_action.triggered.connect(self.print_clicked)
        self.bar.addAction(self.print_action)

        self.save_action = QAction(self, text="Save as JPG")
        self.save_action.setIcon(QIcon(f"{os.path.abspath(os.getcwd())}/icons/icons8-save-40.png"))
        self.save_action.triggered.connect(self.save_clicked)
        self.bar.addAction(self.save_action)

    @Slot()
    def refresh_clicked(self):
        pass

    @Slot()
    def clear_clicked(self):
        pass

    @Slot()
    def print_clicked(self):
        pass

    @Slot()
    def save_clicked(self):
        pass


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()