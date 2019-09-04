import sqlite3

class Backend:
    def __init__(self):
        c=sqlite3.connect("./db/database.db")
        c.row_factory=self.Dict
        self.conn=c
        self.curr=c.cursor()
    def Dict(self,cursor,row):
        d={}
        for idx,col in enumerate(cursor.description):
            d[col[0]]=row[idx]
        return d
    def newTeam(self):
        self.curr.execute("SELECT MATCHES FROM MATCHTABLE")
        v=self.curr.fetchone()
        self.curr.execute("SELECT DISTINCT PLAYER,ctg,scored FROM "+v['Matches'])
        players=self.curr.fetchall()
        return players
    def fetchMatches(self):
        self.curr.execute("SELECT * FROM MATCHTABLE")
        matches=[]
        matchtable=self.curr.fetchall()
        for i in matchtable:
            matches.append(i['Matches'])
        return matches
    def fetchScores(self,matchName,teamName):
 #       self.curr.execute("SELECT MATCHES FROM MATCHTABLE")
#        matches=self.curr.fetchall()
        self.curr.execute("SELECT * FROM "+str(matchName)+" WHERE PLAYER IN(SELECT PLAYER FROM "+str(teamName)+" )")
        return self.curr.fetchall()
    def getData(self,teamName):
        self.curr.execute("SELECT MATCHES FROM MATCHTABLE")
        v=self.curr.fetchone()
        self.curr.execute("SELECT DISTINCT PLAYER,ctg,scored FROM "+str(v['Matches'])+" WHERE PLAYER IN(SELECT PLAYER FROM "+str(teamName)+" )")
        d={}
        
        d['SELECTED_PLAYERS']=self.curr.fetchall()
        self.curr.execute("SELECT DISTINCT PLAYER,ctg FROM "+str(v['Matches'])+" WHERE PLAYER NOT IN(SELECT PLAYER FROM "+str(teamName)+" )")
        d['PLAYERS']=self.curr.fetchall()
        return d
    def fetchTeams(self):
        self.curr.execute("SELECT * FROM TEAMTABLE")
        tt=self.curr.fetchall()
        teams=[]
        for i in tt:
            teams.append(i['Team'])
        return teams
    def fetchPlayers(self,team):
        self.curr.execute("SELECT PLAYER FROM "+str(team))
        players=self.curr.fetchall()
        Players=[]
        for i in players:
            Players.append(i['PLAYER'])
        return Players
    def close(self):
        self.conn.close()
    def saveTeam(self,name,players):
        try:
            self.curr.execute("CREATE TABLE "+str(name)+" ( IDX INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, PLAYER TEXT);")
            self.curr.executemany("INSERT INTO "+str(name)+" (PLAYER) VALUES(?)",self.format(players))
            self.curr.execute("INSERT INTO TEAMTABLE (Team) VALUES(?)",self.format(str(name)))
            self.conn.commit()
            return 0
        except:
            return 1
    def format(self,data):
        if type(data)==type([]):
            Data=[]
            for i in data:
                Data.append((i,))
            return Data
        elif type(data)==type(''):
            return (data,)
