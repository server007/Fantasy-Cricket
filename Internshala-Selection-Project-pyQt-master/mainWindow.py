from PyQt4 import QtCore, QtGui
from backend import Backend
from save import SaveDialog
from evalWindow import LaunchEval
from open_Dialog import OpenDialog
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
def Notify(title,text,icon):
    msg=QtGui.QMessageBox()
    msg.setIcon(icon)
    #msg.setTitle(title)
    msg.setText(text)
    msg.setStandardButtons(QtGui.QMessageBox.Ok)
    msg.exec_()
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.BE=Backend()
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/logo/Logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout.addWidget(self.label_9)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.horizontalLayout_5.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_4.addWidget(self.label_7)
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.horizontalLayout_4.addWidget(self.label_8)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_2.addWidget(self.label_3)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_2.addWidget(self.label_4)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_3.addWidget(self.label_5)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.horizontalLayout_3.addWidget(self.label_6)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 2)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.horizontalLayout_6.addWidget(self.label_10)
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_6.addWidget(self.label_11)
        self.gridLayout_3.addLayout(self.horizontalLayout_6, 1, 0, 1, 1)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.label_12 = QtGui.QLabel(self.centralwidget)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.horizontalLayout_7.addWidget(self.label_12)
        self.label_13 = QtGui.QLabel(self.centralwidget)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.horizontalLayout_7.addWidget(self.label_13)
        self.gridLayout_3.addLayout(self.horizontalLayout_7, 1, 1, 1, 1)
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName(_fromUtf8("horizontalLayout_11"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout = QtGui.QGridLayout(self.frame)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.radioButton = QtGui.QRadioButton(self.frame)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.horizontalLayout_8.addWidget(self.radioButton)
        self.radioButton_2 = QtGui.QRadioButton(self.frame)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.horizontalLayout_8.addWidget(self.radioButton_2)
        self.radioButton_3 = QtGui.QRadioButton(self.frame)
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.horizontalLayout_8.addWidget(self.radioButton_3)
        self.radioButton_4 = QtGui.QRadioButton(self.frame)
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.radioButton.setChecked(True)
        self.horizontalLayout_8.addWidget(self.radioButton_4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.listView = QtGui.QListView(self.frame)
        self.listView.setObjectName(_fromUtf8("listView"))
        self.verticalLayout_2.addWidget(self.listView)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_11.addWidget(self.frame)
        self.label_16 = QtGui.QLabel(self.centralwidget)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.horizontalLayout_11.addWidget(self.label_16)
        self.frame_2 = QtGui.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName(_fromUtf8("horizontalLayout_10"))
        self.label_14 = QtGui.QLabel(self.frame_2)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.horizontalLayout_10.addWidget(self.label_14)
        self.label_15 = QtGui.QLabel(self.frame_2)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.horizontalLayout_10.addWidget(self.label_15)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        spacerItem = QtGui.QSpacerItem(18, 20, QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem)
        self.listView_2 = QtGui.QListView(self.frame_2)
        self.listView_2.setObjectName(_fromUtf8("listView_2"))
        self.horizontalLayout_9.addWidget(self.listView_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.horizontalLayout_11.addWidget(self.frame_2)
        self.gridLayout_3.addLayout(self.horizontalLayout_11, 2, 0, 1, 2)
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_10.raise_()
        self.totalPoints=1000
        self.frame.raise_()
        self.frame_2.raise_()
        self.label_16.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.formation=[]
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuManage_Teams = QtGui.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName(_fromUtf8("menuManage_Teams"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionNEW_TEam = QtGui.QAction(MainWindow)
        self.actionNEW_TEam.setObjectName(_fromUtf8("actionNEW_TEam"))
        self.actionOPEN_Team = QtGui.QAction(MainWindow)
        self.actionOPEN_Team.setObjectName(_fromUtf8("actionOPEN_Team"))
        self.actionSAVE_Team = QtGui.QAction(MainWindow)
        self.actionSAVE_Team.setObjectName(_fromUtf8("actionSAVE_Team"))
        self.actionEVALUATE_Team = QtGui.QAction(MainWindow)
        self.actionEVALUATE_Team.setObjectName(_fromUtf8("actionEVALUATE_Team"))
        self.menuManage_Teams.addAction(self.actionNEW_TEam)
        self.menuManage_Teams.addAction(self.actionOPEN_Team)
        self.menuManage_Teams.addAction(self.actionSAVE_Team)
        self.menuManage_Teams.addAction(self.actionEVALUATE_Team)
        self.menubar.addAction(self.menuManage_Teams.menuAction())
        self.selectedPlayers=[]
        self.pointList={}
        self.selectedPlayerModel=QtGui.QStandardItemModel()
        self.PlayerModel=QtGui.QStandardItemModel()
        self.listView_2.setModel(self.selectedPlayerModel)
        self.listView.setModel(self.PlayerModel)
        self.retranslateUi(MainWindow)
        self.radioButton.clicked.connect(self.BATClicked)
        self.radioButton_2.clicked.connect(self.BOWClicked)
        self.radioButton_3.clicked.connect(self.ARClicked)
        self.radioButton_4.clicked.connect(self.WKClicked)
        self.listView.doubleClicked.connect(self.selectPlayer)
        self.listView_2.doubleClicked.connect(self.removePlayer)
        self.actionNEW_TEam.activated.connect(self.newTeamActivated)
        self.actionOPEN_Team.activated.connect(self.openDialog)
        self.actionSAVE_Team.activated.connect(self.save)
        self.actionEVALUATE_Team.activated.connect(self.evaluate)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def openDialog(self):
        d=OpenDialog()
        d.exec_()
        tn=d.getTeamName()
        if not tn or len(tn)==0:
            return
        self.load(tn)
    def load(self,teamName):
        d={}
        data=self.BE.getData(teamName)
        d['PLAYERS']=data['PLAYERS']
        d['NAME']=teamName
        self.totalPoints=1000
        self.pointList={}
        for i in data['SELECTED_PLAYERS']:
            try:
                d[i['ctg']]+=1
            except KeyError:
                d[i['ctg']]=1
            self.pointList[i['player']]=i['scored']
            self.totalPoints-=int(i['scored'])
        self.label_11.setText(str(self.totalPoints))
        self.label_13.setText(str(1000-self.totalPoints))
        self.newTeamActivated(d)
        self.selectedPlayers=data['SELECTED_PLAYERS']
        self.selectedPlayerModel=QtGui.QStandardItemModel()
        for i in self.selectedPlayers:
            self.selectedPlayerModel.appendRow(QtGui.QStandardItem(str(i['player'])))
        self.listView_2.setModel(self.selectedPlayerModel)
            
    def evaluate(self):
        d=LaunchEval()
        d.exec_()
    def WKClicked(self):
        if 'WK' not in self.players:
            return
        self.PlayerModel=QtGui.QStandardItemModel()
        for i in self.players['WK']:
            item=QtGui.QStandardItem(i)
            self.PlayerModel.appendRow(item)
        self.listView.setModel(self.PlayerModel)
        self.cv='WK'
    def ARClicked(self):
        if 'AR' not in self.players:
            return
        self.PlayerModel=QtGui.QStandardItemModel()
        for i in self.players['AR']:
            item=QtGui.QStandardItem(i)
            self.PlayerModel.appendRow(item)
        self.listView.setModel(self.PlayerModel)
        self.cv='AR'
    def save(self):
        ht={'AR':False,'WK':False,'BAT':False,'BWL':False}
        if len(self.selectedPlayers)<11:
            return Notify("Warning","You need to have a team of atleast 11 players",QtGui.QMessageBox.Critical)
        for i in self.selectedPlayers:
            ht[i['ctg']]=True
        final=True
        for i in ht:
            final=final and ht[i]
        if not final:
            return Notify("Warning","You need to have atleast one player from each group",QtGui.QMessageBox.Critical)
        d=SaveDialog()
        d.exec_()
        text=d.getName()
        if len(text)==0:
            return
        pl=[]
        if text:
            for i in self.selectedPlayers:
                pl.append(i['player'])
            rc=self.BE.saveTeam(text,pl)
            if rc:
                Notify("Error","Error Saving!",QtGui.QMessageBox.Critical)
            else:
                Notify("Saved","Saved!",QtGui.QMessageBox.Information)
                self.label_15.setText(text)
    def BOWClicked(self):
        if 'BWL' not in self.players:
            return
        self.PlayerModel=QtGui.QStandardItemModel()
        for i in self.players['BWL']:
            item=QtGui.QStandardItem(i)
            self.PlayerModel.appendRow(item)
        self.listView.setModel(self.PlayerModel)
        self.cv='BOW'
    def BATClicked(self):
        self.PlayerModel=QtGui.QStandardItemModel()
        if 'BAT' not in self.players:
            return
        for i in self.players['BAT']:
            item=QtGui.QStandardItem(i)
            self.PlayerModel.appendRow(item)
        self.listView.setModel(self.PlayerModel)
        self.cv='BAT'
    def removePlayer(self,index):
        if len(self.selectedPlayers)>0:
            index=index.row()
            ctg=self.selectedPlayers[index]['ctg']
            for i in self.selectedPlayerModel.findItems(self.selectedPlayers[index]['player']):
                self.selectedPlayerModel.removeRow(i.row())
            if ctg=='AR':
                txt=int(self.label_6.text())
                self.label_6.setText(str(txt-1))
            if ctg=='WK':
                txt=int(self.label_8.text())
                self.label_8.setText(str(txt-1))
            if ctg=='BAT':
                txt=int(self.label_2.text())
                self.label_2.setText(str(txt-1))
            if ctg=='BWL':
                txt=int(self.label_4.text())
                self.label_4.setText(str(txt-1))
            player=self.selectedPlayers.pop(index)['player']
            self.players[ctg].append(player)
            self.totalPoints+=int(self.pointList[player])
            self.label_11.setText(str(self.totalPoints))
            self.label_13.setText(str(1000-self.totalPoints))
            eval("self."+self.cv+"Clicked()")
    def selectPlayer(self,index):
        index=index.row()
        ctg='BWL' if self.cv=='BOW' else self.cv
        c=0
        txt=self.players[ctg][index]
        for i in self.selectedPlayers:
            if i['ctg']==ctg:
                c+=1
        currentPlayer=''
        if ctg=='AR':
            self.label_6.setText(str(c+1))
            self.selectedPlayerModel.appendRow(QtGui.QStandardItem(txt))
            currentPlayer=self.players[ctg].pop(index)
            self.selectedPlayers.append({'player':currentPlayer,'ctg':ctg})
            self.totalPoints-=int(self.pointList[currentPlayer])
            self.label_11.setText(str(self.totalPoints))
            self.label_13.setText(str(1000-self.totalPoints))
            eval("self."+self.cv+"Clicked()")
            return
        elif ctg=='WK':
            if c<1:
                currentPlayer=self.players[ctg].pop(index)
                self.selectedPlayers.append({'player':currentPlayer,'ctg':ctg})
                self.totalPoints-=int(self.pointList[currentPlayer])
                self.label_11.setText(str(self.totalPoints))
                self.label_13.setText(str(1000-self.totalPoints))
                self.label_8.setText(str(c+1))
                self.selectedPlayerModel.appendRow(QtGui.QStandardItem(txt))
                eval("self."+self.cv+"Clicked()")
                return
        elif ctg=='BAT':
            currentPlayer=self.players[ctg].pop(index)
            self.selectedPlayers.append({'player':currentPlayer,'ctg':ctg})
            self.totalPoints-=int(self.pointList[currentPlayer])
            self.label_11.setText(str(self.totalPoints))
            self.label_13.setText(str(1000-self.totalPoints))
            self.label_2.setText(str(c+1))
            self.selectedPlayerModel.appendRow(QtGui.QStandardItem(txt))
            eval("self."+self.cv+"Clicked()")
            return
        elif ctg=='BWL':
            if c<3:
                currentPlayer=self.players[ctg].pop(index)
                self.selectedPlayers.append({'player':currentPlayer,'ctg':ctg})
                self.totalPoints-=int(self.pointList[currentPlayer])
                self.label_11.setText(str(self.totalPoints))
                self.label_13.setText(str(1000-self.totalPoints))
                self.label_4.setText(str(c+1))
                self.selectedPlayerModel.appendRow(QtGui.QStandardItem(txt))
                eval("self."+self.cv+"Clicked()")
                return
        
        Notify("Warning","You can't select more than "+self.translate(c)+" "+self.decode(ctg),QtGui.QMessageBox.Critical)                
    def translate(self,c):
	    if c==1:
	        return "one"
	    if c==2:
	        return "two"
	    if c==3:
	        return "three"
	    if c==4:
	        return "four"
    def decode(self,ctg):
	    if ctg=='AR':
	        return "All Rounders"
	    if ctg=='WK':
	        return "Wicket Keeper"
	    if ctg=="BWL":
	        return "Bowlers"
	    if ctg=="BAT":
	        return "Batsmen"
    def newTeamActivated(self,team=None):
        self.players={}
        if not team:
            players=self.BE.newTeam()
        else:
            self.players['BWL']=[]
            self.players['BAT']=[]
            self.players['WK']=[]
            self.players['AR']=[]
            players=team['PLAYERS']
        

        if not team:
            self.label_2.setText("0")
            self.label_4.setText("0")
            self.label_6.setText("0")
            self.label_8.setText("0")
            self.label_11.setText("1000")
            self.label_13.setText("0")
            self.label_15.setText("*Untitled")
        else:
            self.label_2.setText("0" if 'BAT' not in team.keys() else str(team['BAT']))
            self.label_4.setText("0" if 'BWL' not in team.keys() else str(team['BWL']))
            self.label_6.setText("0" if 'AR' not in team.keys() else str(team['AR']))
            self.label_8.setText("0" if 'WKT' not in team.keys() else str(team['WKT']))
            self.label_15.setText(team['NAME'])
        for p in players:
            item=QtGui.QStandardItem(p['player'])
            self.pointList[p['player']]=int(p['scored'])
            try:
                self.players[p['ctg']].append(p['player'])
            except:
                self.players[p['ctg']]=[p['player']]
        self.BATClicked()
        self.selectedPlayerModel=QtGui.QStandardItemModel()
        self.listView_2.setModel(self.selectedPlayerModel)
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Cricket", None))
        self.label_9.setText(_translate("MainWindow", "Your Selections", None))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Batsman (BAT)</span></p></body></html>", None))
        self.label_2.setText(_translate("MainWindow", "##", None))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Wicket-Keeper (WK)</span></p></body></html>", None))
        self.label_8.setText(_translate("MainWindow", "##", None))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Bowler (BOW)</span></p></body></html>", None))
        self.label_4.setText(_translate("MainWindow", "##", None))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Allrounders (AR)</span></p></body></html>", None))
        self.label_6.setText(_translate("MainWindow", "##", None))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Points Available</span></p></body></html>", None))
        self.label_11.setText(_translate("MainWindow", "####", None))
        self.label_12.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Points Used</span></p></body></html>", None))
        self.label_13.setText(_translate("MainWindow", "####", None))
        self.radioButton.setText(_translate("MainWindow", "BAT", None))
        self.radioButton_2.setText(_translate("MainWindow", "BOW", None))
        self.radioButton_3.setText(_translate("MainWindow", "AR", None))
        self.radioButton_4.setText(_translate("MainWindow", "WK", None))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:28pt;\">&gt;</span></p></body></html>", None))
        self.label_14.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Team Name</span></p></body></html>", None))
        self.label_15.setText(_translate("MainWindow", "Displayed Here", None))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams", None))
        self.actionNEW_TEam.setText(_translate("MainWindow", "NEW Team", None))
        self.actionNEW_TEam.setToolTip(_translate("MainWindow", "Create New Team", None))
        self.actionOPEN_Team.setText(_translate("MainWindow", "OPEN Team", None))
        self.actionOPEN_Team.setToolTip(_translate("MainWindow", "Open an Existing Team", None))
        self.actionSAVE_Team.setText(_translate("MainWindow", "SAVE Team", None))
        self.actionSAVE_Team.setToolTip(_translate("MainWindow", "Save your Team", None))
        self.actionEVALUATE_Team.setText(_translate("MainWindow", "EVALUATE Team", None))
        self.actionEVALUATE_Team.setToolTip(_translate("MainWindow", "Evaluate Team Performance", None))
import Resources_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

