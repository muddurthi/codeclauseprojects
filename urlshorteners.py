#pip install pyshorteners
#pip install pyperclip
import pyshorteners
url=input("Enter the url:")
def urlshortener(url):
    u=pyshorteners.Shortener()
    print(u.tinyurl.short(url))
urlshortener(url)