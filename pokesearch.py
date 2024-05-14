
from PIL import Image as im

from random import randint
from sys import argv
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

crop = {
        "1":   (11, 29), "2":   (10, 29), "3":   (8,  31), "4":   (10, 29), "5":   (8,  31), "6":   (8,  31),
        "7":   (11, 29), "8":   (9,  30), "9":   (9,  31), "10":  (11, 28), "11":  (10, 29), "12":  (8,  30),
        "13":  (11, 28), "14":  (10, 29), "15":  (8,  31), "16":  (11, 29), "17":  (10, 30), "18":  (9,  30),
        "19":  (9,  31), "20":  (9,  31), "21":  (12, 29), "22":  (9,  31), "23":  (9,  31), "24":  (8,  31),
        "25":  (9,  30), "26":  (9,  31), "27":  (10, 28), "28":  (8,  31), "29":  (10, 30), "30":  (9,  31),
        "31":  (8,  31), "32":  (9,  30), "33":  (9,  31), "34":  (8,  31), "35":  (10, 30), "36":  (8,  31),
        "37":  (10, 29), "38":  (8,  31), "39":  (10, 29), "40":  (8,  31), "41":  (10, 29), "42":  (8,  31),
        "43":  (12, 28), "44":  (9,  30), "45":  (8,  30), "46":  (9,  30), "47":  (9,  30), "48":  (9,  30),
        "49":  (8,  31), "50":  (13, 26), "51":  (10, 29), "52":  (10, 28), "53":  (9,  30), "54":  (10, 30),
        "55":  (9,  31), "56":  (11, 29), "57":  (10, 30), "58":  (9,  30), "59":  (8,  31), "60":  (13, 27),
        "61":  (11, 28), "62":  (9,  28), "63":  (10, 29), "64":  (8,  30), "65":  (8,  31), "66":  (9,  30),
        "67":  (8,  31), "68":  (8,  31), "69":  (11, 28), "70":  (9,  30), "71":  (9,  31), "72":  (9,  30),
        "73":  (8,  31), "74":  (13, 26), "75":  (8,  31), "76":  (9,  31), "77":  (8,  31), "78":  (8,  31),
        "79":  (11, 29), "80":  (9,  31), "81":  (13, 28), "82":  (9,  31), "83":  (9,  30), "84":  (10, 29),
        "85":  (9,  31), "86":  (9,  31), "87":  (8,  31), "88":  (11, 28), "89":  (9,  31), "90":  (11, 28),
        "91":  (8,  31), "92":  (9,  30), "93":  (9,  30), "94":  (8,  31), "95":  (7,  31), "96":  (9,  30),
        "97":  (7,  31), "98":  (11, 28), "99":  (9,  30), "100": (12, 27), "101": (11, 28), "102": (11, 29),
        "103": (9,  30), "104": (11, 29), "105": (10, 29), "106": (10, 29), "107": (10, 29), "108": (11, 29),
        "109": (10, 31), "110": (8,  30), "111": (13, 30), "112": (10, 30), "113": (10, 29), "114": (10, 29),
        "115": (10, 30), "116": (11, 29), "117": (9,  30), "118": (11, 29), "119": (10, 29), "120": (11, 29),
        "121": (11, 30), "122": (10, 29), "123": (11, 30), "124": (11, 30), "125": (10, 30), "126": (10, 30),
        "127": (9,  30), "128": (9,  29), "129": (9,  31), "130": (9,  30), "131": (11, 30), "132": (13, 27),
        "133": (13, 31), "134": (9,  29), "135": (11, 29), "136": (11, 29), "137": (12, 30), "138": (12, 29),
        "139": (9,  29), "140": (14, 27), "141": (10, 30), "142": (9,  28), "143": (8,  30), "144": (9,  28),
        "145": (9,  28), "146": (10, 28), "147": (12, 28), "148": (10, 29), "149": (9,  30), "150": (9,  30),
        "151": (10, 30), "152": (10, 30), "153": (8,  31), "154": (8,  31), "155": (10, 29), "156": (11, 29),
        "157": (8,  31), "158": (10, 29), "159": (9,  31), "160": (9,  31), "161": (10, 29), "162": (9,  30),
        "163": (10, 30), "164": (9,  31), "165": (10, 29), "166": (9,  29), "167": (13, 27), "168": (9,  31),
        "169": (10, 28), "170": (11, 29), "171": (9,  30), "172": (10, 29), "173": (12, 28), "174": (11, 28),
        "175": (10, 29), "176": (9,  31), "177": (10, 30), "178": (9,  31), "179": (10, 30), "180": (9,  30),
        "181": (9,  31), "182": (9,  30), "183": (10, 29), "184": (9,  30), "185": (9,  31), "186": (9,  31),
        "187": (9,  30), "188": (11, 29), "189": (8,  31), "190": (11, 30), "191": (10, 30), "192": (9,  31),
        "193": (11, 28), "194": (10, 29), "195": (9,  30), "196": (9,  30), "197": (9,  30), "198": (9,  30),
        "199": (8,  31), "200": (9,  29),
        "201-0":  (8,  30), "201-1":  (8,  31), "201-2":  (8,  30), "201-3":  (10, 29),
        "201-4":  (10, 30), "201-5":  (9,  31), "201-6":  (9,  30), "201-7":  (9,  28),
        "201-8":  (8,  30), "201-9":  (11, 30), "201-10": (8,  30), "201-11": (9,  30),
        "201-12": (10, 28), "201-13": (13, 29), "201-14": (9,  28), "201-15": (11, 28),
        "201-16": (12, 28), "201-17": (12, 29), "201-18": (7,  31), "201-19": (10, 30),
        "201-20": (11, 28), "201-21": (11, 30), "201-22": (11, 29), "201-23": (11, 29),
        "201-24": (9,  30), "201-25": (10, 30), "201-26": (8,  30), "201-27": (9,  29),
        "202": (9,  31), "203": (8,  31), "204": (7,  28),
        "205": (10, 29), "206": (11, 31), "207": (8,  31), "208": (9,  31), "209": (10, 30), "210": (8,  31),
        "211": (10, 29), "212": (8,  31), "213": (9,  30), "214": (8,  31), "215": (10, 30), "216": (9,  30),
        "217": (8,  30), "218": (10, 30), "219": (8,  30), "220": (13, 28), "221": (9,  30), "222": (9,  31),
        "223": (11, 29), "224": (9,  29), "225": (8,  31), "226": (8,  30), "227": (8,  31), "228": (10, 30),
        "229": (8,  30), "230": (8,  30), "231": (11, 30), "232": (8,  31), "233": (10, 28), "234": (8,  31),
        "235": (9,  31), "236": (9,  31), "237": (9,  31), "238": (7,  30), "239": (8,  30), "240": (10, 30),
        "241": (8,  31), "242": (8,  31), "243": (8,  31), "244": (8,  31), "245": (8,  31), "246": (9,  30),
        "247": (10, 30), "248": (8,  31), "249": (8,  31), "250": (7,  31), "251": (10, 30), "252": (9,  30),
        "253": (9,  31), "254": (8,  31), "255": (10, 30), "256": (8,  31), "257": (8,  31), "258": (11, 29),
        "259": (9,  30), "260": (8,  31), "261": (12, 30), "262": (9,  31), "263": (13, 30), "264": (11, 31),
        "265": (11, 28), "266": (12, 30), "267": (9,  31), "268": (11, 30), "269": (9,  29), "270": (12, 28),
        "271": (9,  30), "272": (8,  31), "273": (11, 29), "274": (9,  31), "275": (8,  31), "276": (12, 27),
        "277": (10, 29), "278": (12, 27), "279": (10, 30), "280": (10, 30), "281": (9,  31), "282": (8,  31),
        "283": (10, 29), "284": (9,  31), "285": (12, 28), "286": (8,  31), "287": (13, 26), "288": (9,  31),
        "289": (10, 31), "290": (12, 27), "291": (10, 30), "292": (10, 30), "293": (11, 28), "294": (9,  31),
        "295": (8,  31), "296": (10, 30), "297": (9,  31), "298": (10, 28), "299": (11, 29), "300": (9,  30),
        "301": (10, 31), "302": (9,  30), "303": (10, 31), "304": (13, 26), "305": (11, 29), "306": (8,  31),
        "307": (9,  31), "308": (8,  31), "309": (11, 28), "310": (9,  30), "311": (11, 27), "312": (11, 27),
        "313": (9,  30), "314": (9,  30), "315": (9,  31), "316": (11, 28), "317": (12, 29), "318": (10, 30),
        "319": (9,  29), "320": (12, 29), "321": (9,  31), "322": (11, 29), "323": (8,  30), "324": (12, 30),
        "325": (9,  30), "326": (11, 29), "327": (9,  31), "328": (13, 31), "329": (10, 28), "330": (8,  30),
        "331": (10, 29), "332": (8,  31), "333": (11, 26), "334": (9,  30), "335": (9,  30), "336": (9,  29),
        "337": (10, 29), "338": (10, 29), "339": (11, 29), "340": (8,  31), "341": (11, 29), "342": (9,  31),
        "343": (10, 29), "344": (9,  30), "345": (9,  30), "346": (8,  31), "347": (9,  30), "348": (7,  30),
        "349": (10, 28), "350": (8,  31),
        "351-0": (10, 28), "351-1": (6,  28), "351-2": (6,  30), "351-3": (7,  28),
        "352": (10, 30), "353": (10,29), "354": (10,29),
        "355": (10, 29), "356": (8,  31), "357": (8,  31), "358": (9,  30), "359": (8,  31), "360": (9,  29),
        "361": (10, 29), "362": (9,  30), "363": (11, 28), "364": (12, 31), "365": (9,  31), "366": (11, 29),
        "367": (8,  31), "368": (9,  30), "369": (9,  31), "370": (11, 29), "371": (10, 29), "372": (9,  31),
        "373": (8,  31), "374": (9,  30), "375": (9,  31), "376": (8,  31), "377": (9,  31), "378": (8,  30),
        "379": (8,  30), "380": (11, 29), "381": (11, 29), "382": (8,  31), "383": (8,  31), "384": (8,  31),
        "385": (10, 30),
        "386-0": (9, 31), "386-1": (8, 31), "386-2": (8, 31), "386-3": (9, 31)
        }

# Most images come from https://github.com/pret/pokeemerald,
# The attack and defence forms of Deoxys came from https://github.com/pret/pokefirered,
# The varients of Castform came from https://github.com/rh-hideout/pokeemerald-expansion.
# All images are copyright of Nintendo/Creatures Inc./GAME FREAK Inc.

# Opens an image and prints it as ascii character backgrounds
def spritePrint(pkid):
    sprite = (im.open(str(__file__)[:-13]+'icons/icon-'+pkid+'.png')).convert('RGBA')
    pkrange = crop[pkid]
    # Loop over each pixel in a nested loop over each row of 32 pixels
    for y in range(pkrange[0], pkrange[1] + 1):
        for x in range(32):
            pixel = sprite.getpixel((x,y))
            if pixel[3] == 0:
                # Display nothing if the pixel is trasperant
                print(f'\x1b[0m'+"  ", end="")
            else:
                # Print two spaces with the background color of the current pixel
                sleep(0.001+0.0001*randint(1,10))
                print(f'\x1b[48;2;{pixel[0]};{pixel[1]};{pixel[2]}m'+f'\x1b[38;2;{pixel[0]};{pixel[1]};{pixel[2]}m'+"  "+f'\x1b[0m', end="", flush=True)
        print(f'\x1b[0m')

def pksearch(query, alt = None):
    # See if the user is searching by ID
    if query.isnumeric():
        # Make sure the user isn't searching for a pokemon with more than 1 sprite associated with it
        if int(query) in range(1, 386 + 1) and not query in ("201", "351", "386"):
            return spritePrint(query)
        elif int(query) == 201:
            if alt == None:
                return spritePrint(query+"-"+str(randint(0, 27)))
            elif alt in unownlst:
                return spritePrint(query+"-"+str(unownlst.index(alt)))
        elif int(query) in (351, 386):
            if alt == None:
                return spritePrint(query+"-"+str(randint(0, 3)))
            elif alt.title() in castformlst:
                return spritePrint(query+"-"+str(castformlst.index(alt)))
            elif alt.title() in deoxyslst:
                return spritePrint(query+"-"+str(deoxyslst.index(alt)))
            elif alt in ('0', '1', '2', '3'):
                return spritePrint(query+"-"+alt)
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
    elif query.title() == "Deoxys":
         if alt == None:
            return pksearch("386")
         elif alt in deoxyslst:
            return spritePrint("386-"+str(deoxyslst.index(alt.title())))
    elif query in pklist:
        return spritePrint(str(pklist.index(query.title())+1))

if __name__ == "__main__":
    match len(argv):
        case 3:
            if argv[1].title() in ("201", "351", "386", "Unown", "Castform", "Deoxys"):
                pksearch(argv[1].title(), argv[2].title())
        case 2:
            if argv[1] == "--help":
                print("pokesearch.py [PKMN] [VARIENT]")
                print("  PKMN    can either be a species name or pokedex number")
                print("  VARIENT Only use to diplay a specific Unown, Castform, or Deoxys")
            else:
                pksearch(argv[1].title())
        case 1:
            pksearch("random")
