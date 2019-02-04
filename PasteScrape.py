import requests
from bs4 import BeautifulSoup
from languages import *

class PasteScrape:
    """Scrap pastes from Pastebin.

    Parameters:
    -----------
    url : str
        The url of the paste to be scraped.

    Attributes:
    -----------
    id : string
        The id of the paste.
    lang : string
        The language used to highlight the text in the paste.
    data : list
        The text in the paste (each element represent a line).

    Methods:
    --------
    print()
        Print the text of the paste on the screen.
    write()
        Write the text of the paste in a file.
    __get_id(url)
        Return the id of the paste given its url.
    """
    def __init__(self, url):

        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # get the id of the paste
        self.id = self.__get_id(url)

        # detect the syntax highlighting
        lang = soup.find_all(class_='buttonsm')
        self.lang = get_lang(lang[len(lang) - 1].text, self.id)

        # get the text
        self.data = soup.find_all(class_='de1')

    def print(self):
        """Print the data."""

        for line in self.data:
            print(line.text)

    def write(self):
        """Write the data on a file."""

        for line in self.data:
            self.lang.file.write(line.text + '\n')

    def __get_id(self, url):
        """Return the id of the paste.

        Parameters:
        -----------
        url : str
            The url of the paste to be scraped.
        """

        ind = 0
        for i in range(len(url)):
            if url[i] == '/':
                ind = i + 1
        return url[ind:]
