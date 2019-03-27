
import os



def main():
	print("Hello World!")
	history = populateHistory()
	teamNames = getTeams(history)
	print(len(teamNames))
	generateTrainTest(history,2016,0.6)

def generateTrainTest(history,endDate,percentTrain):
	dataLines = []
	trainLines = []
	tesLines = []
	history.sort(key=lambda x:x.year)
	for match in history:
		print(match.year)
		if int(match.year.split("-")[0]) > endDate:
			return
		else:
			vectorHome = getFeatures(match.homeTeam,match.awayTeam,match.year,history,match.homeTeam)
			vectorAway = getFeatures(match.homeTeam,match.awayTeam,match.year,history,match.awayTeam)
			dataLines.append({vectorHome,match.homeGoals})
			dataLines.append({vectorAway,match.awayGoals})
	for i in len(history):
		if i <len(history)*percentTrain:
			trainLines.append(dataLines[i])
		else:
			tesLines.append(dataLines[i])
	printData(trainLines,"data/train.tsv")
	printData(tesLines,"data/train.tsv")

def printData(dataLines,fileName):
	file = open(fileName,"w")
	for line in dataLines:
		file.write(line[0],"\t",line[1])
	file.close()
def getTeams(history):
	set = []
	for match in history:
		if match.homeTeam not in set:
			set.append(match.homeTeam)
		if match.awayTeam not in set:
			set.append(match.awayTeam)
	return set

def populateHistory():
	folderName = "data"
	finalList = []
	for filename in os.listdir(folderName):
		if filename.endswith(".csv"):
			gameList = parseFile(os.path.join(folderName, filename))
			finalList = finalList + gameList
	return finalList

def parseFile(filename):
	gameList = []
	f = open(filename, "r")
	f.readline()
	for line in f:
		lineSplit = line.split(",")
		#Date,HomeTeam,AwayTeam,FTHG,FTAG,FTR,HTHG,HTAG,HTR,Referee,HS,AS,HST,AST,HF,AF,HC,AC,HY,AY,HR,AR
		game = Game(lineSplit[0],lineSplit[1],lineSplit[2],lineSplit[3],lineSplit[4])
		gameList.append(game)
	return gameList

def getFeatures(team1,team2,year,history,predictionTeam):

	dictionary = {}

	#home team based vector

	return 0

class Game():
	homeTeam = None
	awayTeam = None
	homeGoals = None
	awayGoals = None
	year = None

	def __init__(self,year,home,away,hgoals,agoals):
		self.homeTeam = home
		self.homeGoals = hgoals
		self.awayTeam = away
		self.awayGoals = agoals
		self.year = year
		return


if __name__ == "__main__":
	main()