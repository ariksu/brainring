import settings_ui
from PyQt5 import QtWidgets


class Settings(QtWidgets.QWidget, settings_ui.Ui_Settings):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.checklist = [self.CB1, self.CB2, self.CB3, self.CB4, self.CB5, self.CB6, self.CB7, self.CB8, self.CB9,
                          self.CB10, self.CB11, self.CB11, self.CB12, self.CB13, self.CB14, self.CB15, self.CB16]
        self.btnlist = [self.Btn1, self.Btn2, self.Btn3, self.Btn4, self.Btn5, self.Btn6, self.Btn7, self.Btn8,
                        self.Btn9, self.Btn10, self.Btn11, self.Btn12, self.Btn13, self.Btn14, self.Btn15, self.Btn16]
        self.CBlist = [self.CBButton1, self.CBButton2, self.CBButton3, self.CBButton4, self.CBButton5,
                       self.CBButton6, self.CBButton7, self.CBButton8, self.CBButton9, self.CBButton10, self.CBButton11,
                       self.CBButton12, self.CBButton13, self.CBButton14, self.CBButton15, self.CBButton16]
        self.initUi()

    def initUi(self):

        for CB in self.checklist:
            CB.stateChanged.connect(self.CommandActivated)
        for CB in self.CBlist:
            CB.setCurrentText("Кнопка %i" % (self.CBlist.index(CB) + 1))

    def CommandActivated(self):
        """
        activates
        :return:
        """
        CB = self.sender()
        i = self.checklist.index(CB)
        if CB.isChecked():
            self.btnlist[i].setEnabled(True)
            self.CBlist[i].setEnabled(True)
        else:
            self.btnlist[i].setEnabled(False)
            self.CBlist[i].setEnabled(False)

