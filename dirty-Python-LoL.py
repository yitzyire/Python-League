import json
import urllib2
import requests

#Fill in these
summonername= "name"
apikey = "API-Key"
region = "euw"

player1 =""
player2 =""
player3 =""
player4 =""
player5 =""
player6 =""
player7 =""
player8 =""
player9 =""
player10 =""
player11 =""

def summonercall(summonername,apikey,region):
	url = ("https://"+region+".api.pvp.net/api/lol/"+region+"/v1.4/summoner/by-name/"+summonername+"?api_key="+apikey)
	response = requests.get(url)
	return response.json()

def idcall(ID, apikey, region):
	url = ("https://"+region+".api.pvp.net/api/lol/"+region+"/v1.3/stats/by-summoner/"+ID+"/summary?season=SEASON2017&api_key="+apikey)
	response = requests.get(url)
	return response.json()

def matchstats(ID, apikey, region):
	url = ("https://"+region+".api.pvp.net/observer-mode/rest/consumer/getSpectatorGameInfo/EUW1/"+ID+"?api_key="+apikey)
	response = requests.get(url)
	return response.json()

def summonerstats(player1, player2, player3, player4, player5, player6, player7, player8, player9, player10,player11, apikey, region):
	url = ("https://"+region+".api.pvp.net/api/lol/"+region+"/v1.3/game/by-summoner/"+ID+"/recent?api_key="+apikey)
	response = requests.get(url)
	return response.json()

def playerIDtoNames (player1, player2, player3, player4, player5, player6, player7, player8, player9, player10,player11, apikey, region):
	url = ("https://"+region+".api.pvp.net/api/lol/"+region+"/v1.4/summoner/"+player1+","+player2+","+player3+","+player4+","+player5+","+player6+","+player7+","+player8+","+player9+","+player10+","+player11+"/name?api_key="+apikey)	
	response = requests.get(url)
	return response.json()

def summonerRank(player1, player2, player3, player4, player5, player6, player7, player8, player9, player10,player11, apikey, region):
	url = ("https://"+region+".api.pvp.net/api/lol/"+region+"/v2.2/summoner/"+player1+","+player2+","+player3+","+player4+","+player5+","+player6+","+player7+","+player8+","+player9+","+player10+","+player11+"?api_key="+apikey)
	response = requests.get(url)
	return response.json()

firstresponse=summonercall(summonername,apikey,region)
ID = firstresponse[summonername.lower()] ['id']
ID=str(ID)
player1 = ID

secondresponse = idcall(ID,apikey,region.lower())
thirdresponse = matchstats(ID,apikey,region.lower())

try:
	player2 = thirdresponse ["participants"][0]["summonerId"]
	player2=str(player2)
	player3 = thirdresponse ["participants"][1]["summonerId"]
	player3=str(player3)
	player4 = thirdresponse ["participants"][2]["summonerId"]
	player4=str(player4)
	player5 = thirdresponse ["participants"][3]["summonerId"]
	player5=str(player5)
	player6 = thirdresponse ["participants"][4]["summonerId"]
	player6=str(player6)
	player7 = thirdresponse ["participants"][5]["summonerId"]
	player7=str(player7)
	player8 = thirdresponse ["participants"][6]["summonerId"]
	player8=str(player8)
	player9 = thirdresponse ["participants"][7]["summonerId"]
	player9=str(player9)
	player10 = thirdresponse ["participants"][8]["summonerId"]
	player10=str(player10)
	player11 = thirdresponse ["participants"][9]["summonerId"]
	player11=str(player11)

	playerConvert = playerIDtoNames(player1, player2, player3, player4, player5, player6, player7, player8, player9, player10, player11, apikey, region.lower())
	fourthresponse = summonerRank(player1, player2, player3, player4, player5, player6, player7, player8, player9, player10, player11, apikey, region.lower())

	player1rank = fourthresponse[player1]["highestRank"]
	player1rank=str(player1rank)
	player2rank = fourthresponse[player2]["highestRank"]
	player2rank==str(player2rank)
	player3rank = fourthresponse[player3]["highestRank"]
	player3rank==str(player3rank)
	player4rank = fourthresponse[player4]["highestRank"]
	player4rank==str(player4rank)
	player5rank = fourthresponse[player5]["highestRank"]
	player5rank==str(player5rank)
	player6rank = fourthresponse[player6]["highestRank"]
	player6rank==str(player6rank)
	player7rank = fourthresponse[player7]["highestRank"]
	player7rank==str(player7rank)
	player8rank = fourthresponse[player8]["highestRank"]
	player8rank==str(player8rank)
	player9rank = fourthresponse[player9]["highestRank"]
	player9rank==str(player9rank)
	player10rank = fourthresponse[player10]["highestRank"]
	player10rank==str(player10rank)
	player11rank = fourthresponse[player11]["highestRank"]
	player11rank==str(player11rank)
	playerlist = [player1, player2, player3, player4, player5, player6, player7, player8,player9, player10, player11]
	playerrank = [player1rank,player2rank,player3rank,player4rank,player5rank,player6rank,player7rank,player8rank,player9rank,player10rank,player11rank]
	playercount = 1
	for x, y in map(None, playerlist, playerrank):
		print playerConvert[x] + " , " + y
except:

	print "Error, Player not online or API limit reached"
	print "debug:", player1, player2, player3, player4, player5, player6, player7, player8, player9, player10, player11
