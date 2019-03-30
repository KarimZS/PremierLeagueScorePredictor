
import os
import numpy as np


def main():
	print("Hello World!")
	history = populateHistory()
	teamNames = getTeams(history)
	featureTemplate,templateIndex = createFeatureTemplate(teamNames)
	generateTrainTest(history,2016,0.6)

def generateTrainTest(history,endDate,percentTrain):
	dataLines = []
	trainLines = []
	testLines = []
	history.sort(key=lambda x:x.year)
	for match in history:
		if int(match.year.split("-")[0]) > endDate:
			break
		else:
			vectorHome = getFeatures(match.homeTeam,match.awayTeam,match.year,history,1)
			vectorAway = getFeatures(match.homeTeam,match.awayTeam,match.year,history,0)
			dataLines.append({vectorHome,match.homeGoals})
			dataLines.append({vectorAway,match.awayGoals})
	for i in range(len(history)):
		if i <len(history)*percentTrain:
			trainLines.append(dataLines[i])
		else:
			testLines.append(dataLines[i])
	print("size", len(trainLines))
	print("size2", len(testLines))
	printData(trainLines,"data/train.tsv")
	printData(testLines,"data/test.tsv")

def printData(dataLines,fileName):
	file = open(fileName,"w+")
	for input,output in dataLines:
		file.write("%s \t %s \n"%(input,output))
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

def createFeatureTemplate(teams):
	indexDict = {}
	count = 0
	for team in teams:
		for team2 in teams:
			indexDict[team+"#"+team2+"#"+"GF"+"#"+"last"+"home"]=count
			count=count+1
			indexDict[team+"#"+team2+"#"+"GF"+"#"+"last"+"away"]=count
			count=count+1
			indexDict[team+"#"+team2+"#"+"GFAvg"+"#"+"last"+"home"]=count
			count=count+1
			indexDict[team+"#"+team2+"#"+"GFAvg"+"#"+"last"+"away"]=count
			count=count+1
			indexDict[team+"#"+team2+"#"+"GF"+"#"+"last5"+"home"]=count
			count=count+1
			indexDict[team+"#"+team2+"#"+"GF"+"#"+"last5"+"away"]=count
			count=count+1
			indexDict[team+"#"+team2+"#"+"GFAvg"+"#"+"last5"+"home"]=count
			count=count+1
			indexDict[team+"#"+team2+"#"+"GFAvg"+"#"+"last5"+"away"]=count
			count=count+1
		indexDict[team + "#" + "GF" + "#" + "last1"] = count
		count = count + 1
		indexDict[team + "#" + "GF" + "#" + "last2"] = count
		count = count + 1
		indexDict[team + "#" + "GF" + "#" + "last3"] = count
		count = count + 1
		indexDict[team + "#" + "GF" + "#" + "last4"] = count
		count = count + 1
		indexDict[team + "#" + "GF" + "#" + "last5"] = count
		count = count + 1
		indexDict[team + "#" + "GA" + "#" + "last1"] = count
		count = count + 1
		indexDict[team + "#" + "GA" + "#" + "last2"] = count
		count = count + 1
		indexDict[team + "#" + "GA" + "#" + "last3"] = count
		count = count + 1
		indexDict[team + "#" + "GA" + "#" + "last4"] = count
		count = count + 1
		indexDict[team + "#" + "GA" + "#" + "last5"] = count
		count = count + 1
	print("count features",count)
	templateVector = np.zeros(count)
	return templateVector,indexDict


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