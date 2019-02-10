from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import requests
import os


def scrap_images(image_cnt=10):
    search = input("Search for :")

    dir_name = search.replace(" ", "_").lower()

    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)

    param = {"q": search}

    res = requests.get("https://www.bing.com/images/search", params=param)

    soup = BeautifulSoup(res.text, "html.parser")

    links = soup.findAll("a", {"class": "thumb"})

    for link in links:
        try:
            img_obj = requests.get(link.attrs["href"])
            print("getting :", link.attrs["href"])
            title = link.attrs["href"].split("/")[-1]
            img = Image.open(BytesIO(img_obj.content))
            img.save("./"+dir_name+"/"+title, img.format)
            if image_cnt < 0:
                break
            image_cnt -= 1
        except IOError:
            pass

    scrap_images()


if __name__ == "__main__":
    cnt = input("Enter the number Images to Download:")
    scrap_images(int(cnt))


