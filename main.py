from bs4 import BeautifulSoup
import requests

query = input("Search for :")
param = {"q": query}
res = requests.get("https://www.bing.com/search", params=param)

soup = BeautifulSoup(res.text, "html.parser")

result = soup.find("ol", {"id": "b_results"})
links = result.findAll("li", {"class": "b_algo"})

for link in links:
    link_text = link.find("a").text
    link_href = link.find("a").attrs["href"]

    if link_text and link_href:
        print(link_text)
        print(link_href)
        try:
            print("Summery :", link.find("a").parent.parent.find("p").text)
        except AttributeError:
            print("Summery :", "No parent")



        children = link.find("h2")
        print("Next sibling :", children.next_siblink)
