"""

Written by Avinash S. Soor
Git: Avinasho
08-August-2018

The following code should read in a user-defined URL, open it and display each
URL, the page title and finally all the links on that webpage.

"""
import requests
from bs4 import BeautifulSoup, SoupStrainer
import httplib2
import pandas as pd

class webCrawler:
    def __init__(self):
        print('##################################')
        print('Please enter URL (without HTTP://)')
        self.url = input()
        self.url = 'https://' + self.url
        print('##################################')
        print('Finding map for:', self.url)
        print('##################################')
        self.depth = 1
        self.main_list = []
        self.tol = 10
        self.full_list = []
        self.url_length = len(self.url)

    def get_list_of_links(self, url):
        current_list = []
        code = requests.get((url))
        plain = code.text
        soup = BeautifulSoup(plain, 'html.parser')
        for link in soup.find_all('a'):
            current_list.append(link.get('href'))
            if link.get('href') in self.full_list:
                continue
            else:
                self.full_list.append(self.url + link.get('href'))
        return soup, current_list

    def check_url(self, url):
        if url[0:self.url_length] == self.url:
            return True
        else:
            return False

    def main(self):
        while self.depth <= self.tol:
            if self.depth == 1:
                soup, self.main_list = self.get_list_of_links(self.url)
                print('##################################')
                print('Depth:', self.depth)
                print('Title of Page:', soup.title)
                print('List of links on this Page:')
                for index in range(len(self.main_list)):
                    print(self.main_list[index])
                self.tol = len(self.main_list)
                print('##################################')
                # print(' ')
                # print('press enter to continue.')
                # input()
                print(' ')

            elif self.depth > 1:
                for index in range(len(self.main_list)):
                    print(self.main_list[index])
                    # url = self.url + self.main_list[index]
                    try:
                        url = self.main_list[index]
                        cont = self.check_url(url)
                        if cont == True:
                            soup, self.curr_list = self.get_list_of_links(url)
                        else:
                            continue
                    except:
                        url = self.url + self.main_list[index]
                        cont = self.check_url(url)
                        if cont == True:
                            soup, self.curr_list = self.get_list_of_links(url)
                        else:
                            continue
                    print('##################################')
                    print('Depth:', self.depth)
                    print('Title of Page:', soup.title)
                    print('List of links on this Page:')
                    for index in range(len(self.curr_list)):
                        print(self.curr_list[index])
                    print('##################################')
                    # print(' ')
                    # print('press enter to continue.')
                    # input()
                    print(' ')

            self.depth += 1

webCrawler().main()
