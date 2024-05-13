import sys

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
            pixel = sprite.getpixel((x,y))
            if pixel[3] == 0:
                # Display nothing if the pixel is trasperant
                print(f'\033[0m'+"  ", end="")
            else:
                # Print two spaces with the background color of the current pixel
                sleep(0.001+0.0001*randint(1,10))
                print(f'\033[48;2;{pixel[0]};{pixel[1]};{pixel[2]}m'+f'\033[38;2;{pixel[0]};{pixel[1]};{pixel[2]}m'+"  "+f'\033[0m', end="", flush=True)
        print(f'\033[0m')

def pksearch(query, alt = None):
    global pklist
    global unownlst
    global castformlst
    global deoxyslst
    # See if the user is searching by ID
    if query.isnumeric():
        # Make sure the user isn't searching for a pokemon with more than 1 sprite associated with it
        if int(query) <= 386 and int(query) >= 1 and not query in ("201", "351", "386"):
            return spritePrint(query)
        elif int(query) == 201:
            if alt == None:
                return spritePrint(query+"-"+str(randint(0, 27)))
            elif alt in unownlst:
                return spritePrint(query+"-"+str(unownlst.index(alt)))
        elif int(query) == 351:
            if alt == None:
                return spritePrint(query+"-"+str(randint(0, 3)))
            elif alt.title() in castformlst:
                return spritePrint(query+"-"+str(castformlst.index(alt)))
            elif alt in (0, 1, 2, 3):
                return spritePritn(query+"-"+alt)
        elif int(query) == 386:
            if alt == None:
                return spritePrint(query+"-"+str(randint(0,3)))
            elif alt.title() in deoxyslst:
                return spritePrint(query+"-"+str(deoxyslst.index(alt)))
            elif alt in (0, 1, 2, 3):
                return spritePrint(query+"-"+alt)
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
    elif query.title() == "Unown":
        if alt == None:
            return pksearch("201")
        elif alt in unownlst:
            return spritePrint("201-"+str(unownlst.index(alt.upper())))
    elif query.title() == "Castform":
        if alt == None:
            return pksearch("351")
        elif alt in castformlst:
            return spritePrint("351-"+str(castformlst.index(alt.title())))
        else:
            return pksearch("Lol Error")
    elif query.title() == "Deoxys":
         if alt == None:
            return pksearch("386")
         elif alt in deoxyslst:
            return spritePrint("386-"+str(deoxyslst.index(alt.title())))
    elif query in pklist:
        return spritePrint(str(pklist.index(query.title())+1))

match len(sys.argv):
    case 3:
        if sys.argv[1].title() in ("201", "351", "386", "Unown", "Castform", "Deoxys"):
            pksearch(sys.argv[1], sys.argv[2])
    case 2:
        pksearch(sys.argv[1])
    case 1:
        pksearch("random")
