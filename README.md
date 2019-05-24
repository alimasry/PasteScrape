# PasteScrape
PasteScrape is a tool to scrape pastes from Pastebin

# Prerequisites
- Need to have python3 installed
- Needed libraries:
- - [requests]( http://docs.python-requests.org/en/master/)
- - [bs4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

# Example code
- Example code to write what is in a paste on a file and print it on the screen
``` python
from PasteScrape import PasteScrape

def main():
    test = PasteScrape('https://pastebin.com/5Uu3aKqS')  #takes the link of the paste you want to scrap
    test.write()                                         # write the data on a file
    test.print()                                         # print the data on the screen
    paste = test.get()                                   # put the data in the string paste

main()

```
