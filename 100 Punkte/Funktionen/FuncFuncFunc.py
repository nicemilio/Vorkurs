gengar = {"name": "Gengar", "typ": "Geist"}
gengartwo = {"name": "Gengar", "typ": ["Geist", "Gift"]}

def welchen_typ_hat_mein_pokemon (pokemon: dict, type, multiple = False):
    #Takes a pokemon dict, the value which it wants to return and if there are multiple types
    if multiple:
        return pokemon ["name"], ", ".join (pokemon [type])
    if type in pokemon:
        return pokemon ["name"], pokemon [type]
    else:
        return "Not found"


print (welchen_typ_hat_mein_pokemon (gengar, "typ"))
print (welchen_typ_hat_mein_pokemon (gengartwo, "typ", True))