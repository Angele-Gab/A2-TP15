from PySide2.QtWidgets import *

class SQLClientWindow (QWidget) :
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("SQL Client")
        self.setMinimumSize(600,400)
        layout = QVBoxLayout()
        buttonsPanel = ButtonsPanel()
        layout.addWidget(buttonsPanel)

        notificationPanel = QTextEdit()
        layout.addWidget(notificationPanel)

        resultTable = QTableWidget(5,3)
        resultTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout.addWidget(resultTable)



        self.setLayout(layout)


class ButtonsPanel (QWidget) :
    def __init__(self):
        QWidget.__init__(self)
        layout = QHBoxLayout()
        bouton1 = QPushButton("Configure")
        bouton2 = QPushButton("Connect")
        bouton3 = QPushButton("Disconnect")
        layout.addWidget(bouton1)
        layout.addWidget(bouton2)
        layout.addWidget(bouton3)
        self.setLayout(layout)




if __name__ == "__main__":
   app = QApplication([])
   win = SQLClientWindow()
   win.show()
   app.exec_()
