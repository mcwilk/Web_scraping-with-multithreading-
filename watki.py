import os
import threading
import time
import requests
from bs4 import BeautifulSoup


def path_function(default_path):
    """
        Function asks user for file's path and checks if it is correct.
        If not - it asks again. If user did not type any path it takes a
        default one.
    """

    user_path = input("Please type file's path or push Enter: ")
    is_correct = os.path.exists(user_path)

    if len(user_path) == 0:
        file_path = default_path
    elif is_correct:
        file_path = user_path
    else:
        while not is_correct:
            user_path = input("Please type VALID path or push Enter: ")
            
            if len(user_path) != 0:
                is_correct = os.path.exists(user_path)

                if is_correct:
                    file_path = user_path
                    break
            else:
                file_path = default_path
                break

    return file_path


def file_reader(file_path):
    """
        Function reads file and generates list of urls.
    """

    with open(file_path, 'r') as f:
        urls = []

        for line in f:
            urls.append(line.strip())
    
    return urls


def download(url, pages_content):
    """
        Function downloads content from url addresses.
    """

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    pages_content.append(soup)

    return pages_content


class threadURL(threading.Thread):
    """
        Class for threads.
    """

    def __init__(self, url, pages_content):
        threading.Thread.__init__(self)
        self.url = url
        self.pages_content = pages_content

    def run(self):
        pages_content = download(self.url, self.pages_content)


def main():
    """
        Function executes all functions (main program).
    """

    DEFAULT_PATH = 'adresy_url.txt'
    pages_content = []

    file_path = path_function(DEFAULT_PATH)
    urls = file_reader(file_path)

    for url in urls:
        threadURL(url, pages_content).start()
    
    time.sleep(3)
    
    return pages_content


if __name__ == '__main__':
    main()
