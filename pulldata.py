import requests
import json 

API_KEY = "C45399540985DC199A1C374C8EF89F6F"

url = "https://api.steampowered.com/IStoreService/GetAppList/v1/"

params = {
    "key": API_KEY,
    "max_results": 50000,
    "last_appid": 0
}

response = requests.get(url, params=params)
response.raise_for_status()

IDdata = response.json()

print(IDdata)

with open("steamIDdata.json", "w", encoding="utf-8") as file:
    json.dump(IDdata, file)
    
appid = 431960

url = f"https://store.steampowered.com/api/appdetails?appids={appid}&cc=us"

data = requests.get(url).json()
with open("steamMetadata.json", "w", encoding="utf-8") as file:
    json.dump(data, file)
game = data[str(appid)]["data"]

print(game["name"])
print(game["publishers"])
print(game["genres"])
print(game["platforms"])
print(game["categories"])
print(game["release_date"]["date"])
price_overview = game.get("price_overview")
if price_overview:
    print(game["price_overview"]["final"])
else:
    print("Price: Free")
