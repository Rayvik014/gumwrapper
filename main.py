import PyQt5.QtWidgets as pq


def main():
    app = pq.QApplication([])
    window = pq.QWidget()
    menu_layout = pq.QHBoxLayout()
    menu_layout.addWidget(pq.QPushButton('Refresh all'))
    menu_layout.addWidget(pq.QPushButton('Clear all'))
    menu_layout.addWidget(pq.QPushButton('Print'))
    menu_layout.addWidget(pq.QPushButton('Save as jpg'))
    window.setLayout(menu_layout)
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()