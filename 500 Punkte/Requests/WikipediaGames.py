import wikipediaapi

def get_links(page):
    links = page.links
    return enumerate(sorted(links.keys()), start=1)

wiki_wiki = wikipediaapi.Wikipedia('Wikigame', 'de')ç

while (True):
    page_py = wiki_wiki.page('Frühstücksfleisch')
    links = get_links (page_py)
    for i, link in links:
        print (i)
        print (link)
    