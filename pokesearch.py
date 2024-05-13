#Open Source library found at https://github.com/python-pillow/Pillow
from PIL import Image as im

from random import randint
from time import sleep

# List of every pokemon if someone searches by name
pklist = ("Bulbasaur","Ivysaur","Venusaur","Charmander","Charmeleon","Charizard","Squirtle","Wartortle","Blastoise",
          "Caterpie","Metapod","Butterfree","Weedle","Kakuna","Beedrill","Pidgey","Pidgeotto","Pidgeot","Rattata",
          "Raticate","Spearow","Fearow","Ekans","Arbok","Pikachu","Raichu","Sandshrew","Sandslash",
          "Nidoran ","Nidorina","Nidoqueen","Nidoran ","Nidorino","Nidoking","Clefairy","Clefable",
          "Vulpix","Ninetales","Jigglypuff","Wigglytuff","Zubat","Golbat","Oddish","Gloom","Vileplume",
          "Paras","Parasect","Venonat","Venomoth","Diglett","Dugtrio","Meowth","Persian","Psyduck","Golduck",
          "Mankey","Primeape","Growlithe","Arcanine","Poliwag","Poliwhirl","Poliwrath","Abra","Kadabra","Alakazam",
          "Machop","Machoke","Machamp","Bellsprout","Weepinbell","Victreebel","Tentacool","Tentacruel",
          "Geodude","Graveler","Golem","Ponyta","Rapidash","Slowpoke","Slowbro","Magnemite","Magneton","Farfetch",
          "Doduo","Dodrio","Seel","Dewgong","Grimer","Muk","Shellder","Cloyster","Gastly","Haunter","Gengar","Onix",
          "Drowzee","Hypno","Krabby","Kingler","Voltorb","Electrode","Exeggcute","Exeggutor","Cubone","Marowak",
          "Hitmonlee","Hitmonchan","Lickitung","Koffing","Weezing","Rhyhorn","Rhydon","Chansey","Tangela","Kangaskhan",
          "Horsea","Seadra","Goldeen","Seaking","Staryu","Starmie","Mr","Scyther","Jynx","Electabuzz","Magmar","Pinsir",
          "Tauros","Magikarp","Gyarados","Lapras","Ditto","Eevee","Vaporeon","Jolteon","Flareon","Porygon",
          "Omanyte","Omastar","Kabuto","Kabutops","Aerodactyl","Snorlax","Articuno","Zapdos","Moltres",
          "Dratini","Dragonair","Dragonite","Mewtwo","Mew","Chikorita","Bayleef","Meganium",
          "Cyndaquil","Quilava","Typhlosion","Totodile","Croconaw","Feraligatr","Sentret","Furret","Hoothoot","Noctowl",
          "Ledyba","Ledian","Spinarak","Ariados","Crobat","Chinchou","Lanturn","Pichu","Cleffa","Igglybuff",
          "Togepi","Togetic","Natu","Xatu","Mareep","Flaaffy","Ampharos","Bellossom","Marill","Azumarill","Sudowoodo",
          "Politoed","Hoppip","Skiploom","Jumpluff","Aipom","Sunkern","Sunflora","Yanma","Wooper","Quagsire",
          "Espeon","Umbreon","Murkrow","Slowking","Misdreavus","Unown","Wobbuffet","Girafarig","Pineco","Forretress",
          "Dunsparce","Gligar","Steelix","Snubbull","Granbull","Qwilfish","Scizor","Shuckle","Heracross","Sneasel",
          "Teddiursa","Ursaring","Slugma","Magcargo","Swinub","Piloswine","Corsola","Remoraid","Octillery","Delibird",
          "Mantine","Skarmory","Houndour","Houndoom","Kingdra","Phanpy","Donphan","Porygon2","Stantler","Smeargle",
          "Tyrogue","Hitmontop","Smoochum","Elekid","Magby","Miltank","Blissey","Raikou","Entei","Suicune",
          "Larvitar","Pupitar","Tyranitar","Lugia","Ho-Oh","Celebi","Treecko","Grovyle","Sceptile",
          "Torchic","Combusken","Blaziken","Mudkip","Marshtomp","Swampert","Poochyena","Mightyena","Zigzagoon","Linoone",
          "Wurmple","Silcoon","Beautifly","Cascoon","Dustox","Lotad","Lombre","Ludicolo","Seedot","Nuzleaf","Shiftry",
          "Taillow","Swellow","Wingull","Pelipper","Ralts","Kirlia","Gardevoir","Surskit","Masquerain",
          "Shroomish","Breloom","Slakoth","Vigoroth","Slaking","Nincada","Ninjask","Shedinja",
          "Whismur","Loudred","Exploud","Makuhita","Hariyama","Azurill","Nosepass","Skitty","Delcatty","Sableye",
          "Mawile","Aron","Lairon","Aggron","Meditite","Medicham","Electrike","Manectric","Plusle","Minun",
          "Volbeat","Illumise","Roselia","Gulpin","Swalot","Carvanha","Sharpedo","Wailmer","Wailord","Numel","Camerupt",
          "Torkoal","Spoink","Grumpig","Spinda","Trapinch","Vibrava","Flygon","Cacnea","Cacturne","Swablu","Altaria",
          "Zangoose","Seviper","Lunatone","Solrock","Barboach","Whiscash","Corphish","Crawdaunt","Baltoy","Claydol",
          "Lileep","Cradily","Anorith","Armaldo","Feebas","Milotic","Castform","Kecleon","Shuppet","Banette",
          "Duskull","Dusclops","Tropius","Chimecho","Absol","Wynaut","Snorunt","Glalie","Spheal","Sealeo","Walrein",
          "Clamperl","Huntail","Gorebyss","Relicanth","Luvdisc","Bagon","Shelgon","Salamence","Beldum",
          "Metang","Metagross","Regirock","Regice","Registeel","Latias","Latios","Kyogre","Groudon","Rayquaza",
          "Jirachi","Deoxys")

unownlst = ("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","!","?")
castformlst = ("Normal", "Rainy", "Snowy" , "Sunny")
deoxyslst = ("Normal", "Attack", "Defence", "Speed")

# Most images come from https://github.com/pret/pokeemerald,
# The attack and defence forms of Deoxys came from https://github.com/pret/pokefirered,
# The varients of Castform came from https://github.com/rh-hideout/pokeemerald-expansion.
# All images are copyright of Nintendo/Creatures Inc./GAME FREAK Inc.

# Opens an image and prints it as ascii character backgrounds
def spritePrint(pkid):
    sprite = (im.open(str(__file__)[:-13]+'icons\icon-'+pkid+'.png')).convert('RGBA')
    # Loop over each pixel in a nested loop over each row of 32 pixels
    for y in range(32):
        for x in range(32):
            # This function returns a list (r, g, b, a) of the red, green, blue, and alpha values of the pixel (x, y)
            pixel = sprite.getpixel((x,y))
            if pixel[3] == 0:
                # Display nothing if the pixel is trasperant
                print(f'\033[0m'+"  ", end="")
            else:
                # Print two spaces with the background color of the current pixel
                sleep(0.001+0.0001*randint(1,10))
                print(f'\033[48;2;{pixel[0]};{pixel[1]};{pixel[2]}m'+f'\033[38;2;{pixel[0]};{pixel[1]};{pixel[2]}m'+"  "+f'\033[0m', end="", flush=True)
        print(f'\033[0m')

def pksearch(query):
    global pklist
    global unownlst
    global castformlst
    global deoxyslst
    # See if the user is searching by ID
    if query.isnumeric():
        # Make sure the user isn't searching for a pokemon with more than 1 sprite associated with it
        if int(query) <= 386 and int(query) >= 1 and ("201", "351", "386").count(query) == 0:
            return spritePrint(query)
        elif int(query) == 201:
            # Print a random Unown
            return spritePrint(query+"-"+str(randint(0, 27)))
        elif int(query) == 351 or int(query) == 386:
            # Print a random Castform or Deoxys
            return spritePrint(query+"-"+str(randint(0, 3)))
        else:
            return pksearch("Lol Error")
    # Print a specific Unown
    elif query[0:4] == "201-" and list(str(l) for l in range(0, 28)).count(query[4:]) == 1:
        return spritePrint(query)
    elif query[0:4] == "201-" and unownlst.count((query[4].upper())) == 1 and len(query) == 5:
        return spritePrint("201-"+str(unownlst.index(query[5].upper())))
    # Print a specific Castform or Deoxys
    elif (query[0:4] == "351-" or query[0:4] == "386-") and list(str(l) for l in range(4)).count(query[4]) == 1 and len(query) == 5:
        return spritePrint(query)
    # Print a random Pokemon
    elif query.lower() == "random":
        return pksearch(str(randint(1, 386)))
    # Exceptions for Unown, Castform, or Deoyxs
    elif query.title()[0:5] == "Unown" and len(query) == 5 or len(query) == 7:
        if len(query) == 5:
            return pksearch("201")
        elif len(query) == 7 and unownlst.count(query[6].upper()) == 1 and query[5] == " " or query[5] == "-":
            return spritePrint("201-"+str(unownlst.index(query[6].upper())))
    elif query.title()[0:8] == "Castform":
        if len(query) == 8:
            return pksearch("351")
        elif castformlst.count(query[9:].title()) == 1 and query[8] == " " or query[8] == "-":
            return spritePrint("351-"+str(castformlst.index(query[9:].title())))
        else:
            return pksearch("Lol Error")
    elif query[0:6].title() == "Deoxys":
         if len(query) == 6:
            return pksearch("386")
         elif deoxyslst.count(query[7:].title()) == 1 and query[6] == " " or query[6] == "-":
            return spritePrint("386-"+str(deoxyslst.index(query[7:].title())))
    elif pklist.count(query) == 1:
        return spritePrint(str(pklist.index(query.title())+1))
    else:
        print("That is not a valid Pokemon, please enter the ID or name of a Pokemon from the first three generations.")
        return pksearch(str(input("Please enter a valid Pokemon name or ID ")))

# Instructions to user
print("This tool will display any Pokemon from the first three generations (the first 386 Pokemon)")
sleep(1)
print("You can search by ID number, by species name, or type 'random' for a suprise")
sleep(1)
pksearch(str(input("Pick your Pokemon: ")))
