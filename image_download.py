import random
import urllib.request
def download_web_image(url):
    name=random.randrange(1,256)
    f_name=str(name)+".jpg"
    urllib.request.urlretrieve(url,f_name)
print("Enter the image url")
url=input(("<<<<<><<<<"))
download_web_image(url)
def repeat(url):
    print("Enter another image url")
    url=input(("<<<<<><<<<"))
    download_web_image(url)
repeat(url)

