from PyQt4 import QtCore, QtGui
from backend import Backend
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        self.BE=Backend()
        self.points=0
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(600, 400)
        Dialog.setMinimumSize(QtCore.QSize(600, 400))
        Dialog.setMaximumSize(QtCore.QSize(600, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/logo/Logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.gridLayout_3 = QtGui.QGridLayout(Dialog)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_3.addWidget(self.label_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.comboBox = QtGui.QComboBox(Dialog)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.horizontalLayout_3.addWidget(self.comboBox)
        self.comboBox_2 = QtGui.QComboBox(Dialog)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.horizontalLayout_3.addWidget(self.comboBox_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.scrollArea = QtGui.QScrollArea(Dialog)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 281, 209))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.listView = QtGui.QListView(self.scrollAreaWidgetContents)
        self.listView.setObjectName(_fromUtf8("listView"))
        self.gridLayout.addWidget(self.listView, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout.addWidget(self.label_4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.scrollArea_2 = QtGui.QScrollArea(Dialog)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName(_fromUtf8("scrollArea_2"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 281, 207))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.listView_2 = QtGui.QListView(self.scrollAreaWidgetContents_2)
        self.listView_2.setObjectName(_fromUtf8("listView_2"))
        self.gridLayout_2.addWidget(self.listView_2, 0, 0, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout.addWidget(self.scrollArea_2)
        self.Teams,self.Matches=[],[]
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_6.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout_4.addWidget(self.pushButton)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.gridLayout_3.addLayout(self.verticalLayout_6, 0, 0, 1, 1)
        self.fillcomboBoxes()
        self.retranslateUi(Dialog)
        self.comboBox.activated.connect(self.selectTeam)
        self.comboBox_2.activated.connect(self.selectMatch)
        self.pushButton.setEnabled(False)
        self.pushButton.clicked.connect(self.renderScores)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def renderScores(self):
        model=QtGui.QStandardItemModel()
        totalPoints=0
        for i in self.Scores:
            points=0
            if i['ctg']=='BAT':
                if int(i['scored'])>=2:
                    points+=1
                if int(int(i['scored'])/50)>=1:
                    points+=5
                if int(int(i['scored'])/100)>=1:
                    points+=10
                if 80>=(int(i['scored'])/int(i['faced']))<=100:
                    points+=2
                if (int(i['runs'])/int(i['faced']))>100:
                    points+=4
                if int(i['fours'])>=1:
                    points+=1
                if int(i['sixes'])>=1:
                    points+=2
            elif i['ctg']=='BWL':
                points+=10*int(i['wickets'])
                points+=5*(int(i['wickets'])//3)
                if i['wickets']>=5:
                    points+=10
                if 3.5>int(i['faced'])/int(i['scored'])<=4.5:
                    points+=4
                if 2>=int(i['faced'])/int(i['scored'])<=3.5:
                    points+=7
                if int(i['faced'])/int(i['scored'])<2:
                    points+=10
                points+=10*(i['ro']+i['catches']+i['stumping'])
            totalPoints+=points
            model.appendRow(QtGui.QStandardItem(str(points)))
            self.listView_2.setModel(model)
            self.label_4.setText(str(totalPoints))
                
            
    def selectTeam(self):
        self.selectedTeam=self.comboBox.currentText()
        self.Players=self.BE.fetchPlayers(self.selectedTeam)
        PlayerViewModel=QtGui.QStandardItemModel()
        for i in self.Players:
            item=QtGui.QStandardItem(i)
            PlayerViewModel.appendRow(item)
        self.listView.setModel(PlayerViewModel)
    def selectMatch(self):
        selectedMatch=self.comboBox_2.currentText()
        self.Scores=self.BE.fetchScores(selectedMatch,self.selectedTeam)
        self.pushButton.setEnabled(True)
    def fillcomboBoxes(self):
    	self.Teams=self.BE.fetchTeams()
    	self.comboBox.addItems(self.Teams)
    	self.Matches=self.BE.fetchMatches()
    	self.comboBox_2.addItems(self.Matches)
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Evalute", None))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Evaluate the Performance of your Fantasy Team</span></p></body></html>", None))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Players</span></p></body></html>", None))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-weight:600;\">Points</span></p></body></html>", None))
        self.label_4.setText(_translate("Dialog", "##", None))
        self.pushButton.setText(_translate("Dialog", "Calculate Score", None))

import Resources_rc
class LaunchEval(QtGui.QDialog,Ui_Dialog):
    def __init__(self,parent=None):
        QtGui.QDialog.__init__(self,parent)
        self.setupUi(self)
    def getPoints(self):
        return self.points


