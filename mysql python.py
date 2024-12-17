# importing the source code and mysql connector
import A_Tkinter_BasicCode
import mysql.connector
# importing the source code and mysql connector

# establishing connection to mysql server
db=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="golibuxi",
    database="scoreboard"
    )
# establishing connection to mysql server

mycon=db.cursor()

# please de-comment the following region before executing it a new computer, but re-comment it on following attempts

mycon.execute("CREATE DATABASE scoreboard")
mycon.execute("CREATE TABLE highscore(name VARCHAR(30), score smallint)")
mycon.execute("DESCRIBE highscore")
for x in mycon:
   print(x)

# please de-comment the following region before executing it a new computer, but re-comment it on following attempts

# entering the score and player name
mycon.execute("INSERT INTO highscore(name, score) VALUES(%s, %s)",(A_Tkinter_BasicCode.player_det))
db.commit()
# entering the score and player name

# extracting scoreboard
mycon.execute("SELECT * FROM highscore")
# extracting scoreboard

# displaying leaderboard on python console
print("! Player Name ! Score  !")
for x in mycon:
    print("!",x[0]," "*(10-len(x[0])),"!",
          x[1]," "*(5-len(str(x[1]))),"!")
# displaying leaderboard on python console
