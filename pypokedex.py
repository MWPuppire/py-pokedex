#!/usr/bin/env python3
import json, requests

def extractdata():
    global mode

    pkdxfile = "https://raw.githubusercontent.com/MWPuppire/py-pokedex/master/data/pokedex.json"
    file = requests.get(pkdxfile)
    pokedex = file.json()
    data = {}

    for pokemon in pokedex:
            pokemondata = eval(json.dumps(pokedex[pokemon]))
            data.update({pokemon: pokemondata})
    return data
def list():
    data = extractdata()
    list = []
    for pokemon in sorted(data):
        pokemon = data[pokemon]
        list.append("No. " + str(pokemon["number"]) + ":   " + pokemon["name"] + "       " + " - ".join(pokemon["types"]))
    return list
def lookup(pkmn):
    data = extractdata()
    try:
        int(pkmn)
        searchby = "number"
    except ValueError:
        searchby = "name"
    for pokemon in data:
        if data[pokemon][searchby] == pkmn:
            pkmn = pokemon
    if not pkmn in data:
        return "Error: " + pkmn + " does not exist in the database"
    pokemon = data[pkmn]
    return "No. " + str(pokemon["number"]) + ":   " + pokemon["name"] + "       " + " - ".join([str(type) for type in pokemon["types"]]) + "\nStats: \nBST (Base Stat Total): " + str(int(pokemon["spdefense"]) + int(pokemon["defense"]) + int(pokemon["spattack"]) + int(pokemon["attack"]) + int(pokemon["hp"]) + int(pokemon["speed"])) + "\nHP: " + str(pokemon["hp"]) + "\nAttack: " + str(pokemon["attack"]) + "\nDefense: " + str(pokemon["defense"]) + "\nSp. Attack: " + str(pokemon["spattack"]) + "\nSp. Defense: " + str(pokemon["spdefense"]) + "\nSpeed: " + str(pokemon["speed"])
def listgen(gen):
    data = extractdata()
    list = []
    if gen == "1": genStart, genEnd = 1, 151
    elif gen == "2": genStart, genEnd = 152, 251
    elif gen == "3": genStart, genEnd = 252, 386
    elif gen == "4": genStart, genEnd = 387, 493
    elif gen == "5": genStart, genEnd = 494, 649
    elif gen == "6": genStart, genEnd = 650, 721
    for pokemon in sorted(data):
        pokemon = data[pokemon]
        if int(pokemon["number"]) >= genStart and int(pokemon["number"]) <= genEnd:
            list.append("No. " + str(pokemon["number"]) + ":   " + pokemon["name"] + "       " + " - ".join([str(type) for type in pokemon["types"]]))
    return list
def help():
    return "{0:=^40}".format("") + "\nOptions:\n-help Brings up this text\n-lookup Look up a specific Pokémon by name or number\n-list List all Pokémon\n-gen List all Pokémon in a certain generation\n" + "{0:=^40}".format("")