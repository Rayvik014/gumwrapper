import os
from PySide6.QtCore import Qt, Slot
from PySide6.QtWidgets import (
    QMainWindow,
    QApplication,
    QWidget,
    QGridLayout,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
)
from PySide6.QtGui import (
    QAction,
    QIcon
)


class WrapperWindow(QWidget):
    def __init__(self):
        super().__init__()
        grid = QGridLayout(self)
        ul_block = GumWrapperBlock()
        ur_block = GumWrapperBlock()
        dl_block = GumWrapperBlock()
        dr_block = GumWrapperBlock()
        grid.addLayout(ul_block, 0, 0)
        grid.addLayout(ur_block, 0, 1)
        grid.addLayout(dl_block, 1, 0)
        grid.addLayout(dr_block, 1, 1)



class GumWrapperBlock(QVBoxLayout):
    def __init__(self):
        super().__init__()
        refresh_button = QPushButton('Refresh')
        change_button = QPushButton('Change')
        edit_button = QPushButton('Edit')
        sublayout = QHBoxLayout()
        sublayout.addWidget(refresh_button)
        sublayout.addWidget(change_button)
        sublayout.addWidget(edit_button)
        self.addLayout(sublayout)
        self.addWidget(QLabel())



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

        self.setCentralWidget(WrapperWindow())

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