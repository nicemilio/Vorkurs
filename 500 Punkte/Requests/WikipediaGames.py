import wikipediaapi

def get_links(page):
    links = page.links
    return links

wiki_wiki = wikipediaapi.Wikipedia('Wikigame', 'de')
page_py = wiki_wiki.page('Frühstücksfleisch')

while True:
    links = get_links(page_py)
    link_list = list(links.keys())
    
    for i, link in enumerate(link_list, start=1):
        print(f"Nummer {i}: {link}")
    
    print("In welchen Link möchtest du navigieren?")
    selection = int(input()) - 1
     
    if 0 <= selection < len(link_list):
        selected_link = link_list[selection]
        print(f"Navigiere zu: {selected_link}")
        if (selected_link == "Python (Programmiersprache)"):
            print ("Herzlichen Glückwunsch, du hast die Python Seite erreicht")
            break
        page_py = wiki_wiki.page(selected_link)
    else:
        print("Ungültige Auswahl, bitte erneut versuchen.")
