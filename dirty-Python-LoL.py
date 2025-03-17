import json
import requests

# Fill in these
summonername = "name"
apikey = "API-Key"
region = "euw"

player1 = ""
player2 = ""
player3 = ""
player4 = ""
player5 = ""
player6 = ""
player7 = ""
player8 = ""
player9 = ""
player10 = ""
player11 = ""

def summonercall(summonername, apikey, region):
    url = f"https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summonername}?api_key={apikey}"
    response = requests.get(url)
    return response.json()

def idcall(ID, apikey, region):
    url = f"https://{region}.api.riotgames.com/lol/league/v4/entries/by-summoner/{ID}?api_key={apikey}"
    response = requests.get(url)
    return response.json()

def matchstats(ID, apikey, region):
    url = f"https://{region}.api.riotgames.com/lol/spectator/v4/active-games/by-summoner/{ID}?api_key={apikey}"
    response = requests.get(url)
    return response.json()

def playerIDtoNames(player_list, apikey, region):
    player_str = ",".join(player_list)
    url = f"https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-account/{player_str}?api_key={apikey}"
    response = requests.get(url)
    return response.json()

def summonerRank(player_list, apikey, region):
    player_str = ",".join(player_list)
    url = f"https://{region}.api.riotgames.com/lol/league/v4/entries/by-summoner/{player_str}?api_key={apikey}"
    response = requests.get(url)
    return response.json()

firstresponse = summonercall(summonername, apikey, region)
ID = firstresponse[summonername.lower()]['id']
ID = str(ID)
player1 = ID

secondresponse = idcall(ID, apikey, region.lower())
thirdresponse = matchstats(ID, apikey, region.lower())

try:
    player_list = [str(thirdresponse["participants"][i]["summonerId"]) for i in range(10)]
    playerConvert = playerIDtoNames(player_list, apikey, region.lower())
    fourthresponse = summonerRank(player_list, apikey, region.lower())

    player_ranks = {player_list[i]: str(fourthresponse[i]["tier"]) for i in range(10)}

    for i, player_id in enumerate(player_list):
        player_name = playerConvert.get(player_id, {}).get('name', 'Unknown')
        player_rank = player_ranks.get(player_id, 'Unranked')
        print(f"{player_name} , {player_rank}")

except requests.exceptions.RequestException as e:
    print("Error: API request failed")
    print("debug:", e)

except KeyError as e:
    print("Error: Key not found in response")
    print("debug:", e)

except Exception as e:
    print("Unexpected error:", e)
