import requests
import json
import time
import re

API_KEY = "C45399540985DC199A1C374C8EF89F6F"

# 1. Get Steam App IDs

url = "https://api.steampowered.com/IStoreService/GetAppList/v1/"

params = {
    "key": API_KEY,
    "max_results": 1000,
    "last_appid": 0
}

response = requests.get(url, params=params)
response.raise_for_status()

IDdata = response.json()

# Save the raw App List
with open("steamIDdata.json", "w", encoding="utf-8") as file:
    json.dump(IDdata, file, indent=4)

print("App list downloaded.")


# 2. Get the actual game data

apps = IDdata.get("response", {}).get("apps", [])

games = []

print(f"Found {len(apps)} apps.")


for index, app in enumerate(apps):

    appid = app.get("appid")

    if not appid:
        continue

    print(f"{index + 1}/{len(apps)} - AppID: {appid}")

    # Steam store API
    url = f"https://store.steampowered.com/api/appdetails"

    params = {
        "appids": appid,
        "cc": "us",
        "l": "english"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()

        data = response.json()

        # The response is keyed by the AppID
        app_data = data.get(str(appid))

        if not app_data:
            print("  No data returned.")
            continue

        # Steam sometimes returns success=false
        if not app_data.get("success"):
            print("  Steam returned success=false.")
            continue

        game = app_data.get("data", {})

        # Only keep actual games

        if game.get("type") != "game":
            print(f"  Skipping: {game.get('type')}")
            continue

        # Platforms

        platforms = [
            platform
            for platform, supported
            in game.get("platforms", {}).items()
            if supported
        ]

        # Genres

        genres = [
            genre.get("description")
            for genre in game.get("genres", [])
        ]

        # Categories

        categories = [
            category.get("description")
            for category in game.get("categories", [])
        ]

        # Release date

        release_date = game.get("release_date", {}).get("date")

        release_year = None

        if release_date:
            match = re.search(r"\b(19|20)\d{2}\b", release_date)

            if match:
                release_year = int(match.group())
                
        # Price

        price_overview = game.get("price_overview")

        if price_overview:
            price = price_overview.get("final_formatted")
        elif game.get("is_free"):
            price = "Free"
        else:
            price = None

        # Create our own clean JSON object

        game_data = {
            "appid": appid,
            "name": game.get("name"),

            "platforms": platforms,
            
            "genres": genres,

            "release_year": release_year,

            "price": price,

            "singleplayer": "Single-player" in categories,
            "multiplayer": "Multi-player" in categories,

            "categories": categories,

            "publisher": game.get("publishers", []),
            "developer": game.get("developers", [])
        }

        games.append(game_data)

        print(f"  {game.get('name')}")

    except requests.RequestException as error:
        print(f"  Request failed: {error}")

    except Exception as error:
        print(f"  Error: {error}")

    # Don't send requests too quickly
    time.sleep(1)


# 3. Save all game data

with open("steamMetadata.json", "w", encoding="utf-8") as file:
    json.dump(games, file, indent=4, ensure_ascii=False)

print()
print(f"Finished! Saved {len(games)} games to steamMetadata.json")
