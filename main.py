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
    QSizePolicy,
    QLineEdit,
)
from PySide6.QtGui import (
    QAction,
    QIcon,
    QPixmap,
)


class WrapperWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        grid = QGridLayout(self)
        ul_block = GumWrapperBlock('pics/empty_877_620.png')
        ur_block = GumWrapperBlock('pics/empty_877_620.png')
        dl_block = GumWrapperBlock('pics/empty_877_620.png')
        dr_block = GumWrapperBlock('pics/empty_877_620.png')
        grid.addLayout(ul_block, 0, 0)
        grid.addLayout(ur_block, 0, 1)
        grid.addLayout(dl_block, 1, 0)
        grid.addLayout(dr_block, 1, 1)





class GumWrapperBlock(QVBoxLayout):
    def __init__(self, image_path):
        super().__init__()
        refresh_button = QPushButton('Refresh')
        edit_button = QPushButton('Edit')
        sublayout = QHBoxLayout()
        sublayout.addWidget(refresh_button)
        sublayout.addWidget(edit_button)

        mark_label = QLabel("Mark: ")
        mark_label_lineedit = QLineEdit()
        model_label = QLabel("Model: ")
        model_label_lineedit = QLineEdit()
        year_label = QLabel("Year: ")
        year_label_lineedit = QLineEdit()
        sublayout.addWidget(mark_label)
        sublayout.addWidget(mark_label_lineedit)
        sublayout.addWidget(model_label)
        sublayout.addWidget(model_label_lineedit)
        sublayout.addWidget(year_label)
        sublayout.addWidget(year_label_lineedit)

        self.addLayout(sublayout)
        image_label = QLabel()
        image_label.setScaledContents(True)
        pixmap = QPixmap(image_path)
        pixmap.scaled(877,620,aspectMode=Qt.KeepAspectRatio)
        image_label.setPixmap(pixmap)
        image_label.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.addWidget(image_label)

        refresh_button.clicked.connect(self.refresh_clicked)
        edit_button.clicked.connect(self.edit_clicked)

    @Slot()
    def refresh_clicked(self):
        pass

    @Slot()
    def edit_clicked(self):
        pass

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.bar = self.addToolBar("Menu")
        self.bar.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)

        self.refresh_action = QAction(self, text="Refresh All")
        self.refresh_action.setIcon(QIcon(f"{os.path.abspath(os.getcwd())}/icons/icons8-refresh-40.png"))
        self.refresh_action.triggered.connect(self.refresh_all_clicked)
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

        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)

        self.setCentralWidget(WrapperWindow())


    @Slot()
    def refresh_all_clicked(self):
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
    window.resize(1315, 1000)
    window.setMinimumSize(100, 70)
    window.show()
    app.exec()