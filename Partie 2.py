from PySide2.QtWidgets import *

class LabeledTextField(QWidget) :
    def __init__(self,text):
        QWidget.__init__(self)
        self.setWindowTitle("Affichage")
        layout = QHBoxLayout()
        label = QLabel(text)
        textbis = QTextEdit()
        textbis.setMaximumHeight(800)

        layout.addWidget(label)
        layout.addWidget(textbis)

class ConfigurationDialog(QDialog) :
    def __init__(self,text):
        QWidget.__init__(self)
        label1 = LabeledTextField("IP address")
        label2 = LabeledTextField("User")
        label3 = LabeledTextField("Password")
        layout = QHBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)

        self.setLayout(layout)



if __name__ == "__main__":
   app = QApplication([])
   win = ConfigurationDialog()
   app.exec_()

