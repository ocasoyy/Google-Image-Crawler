from __future__ import print_function

from bs4 import BeautifulSoup
import requests
import re
import urllib.request
import urllib
from urllib.request import urlopen
import os
import argparse
import sys
import json
import time
from selenium import webdriver



def get_soup(url,header):
    return BeautifulSoup(urlopen(urllib.request.Request(url, headers=header)),'html.parser')

path = "C:/Users/YY/Documents/Data/CCP/Crawled"

def main(args):
    keyword = str(input("검색어를 입력하세요: "))
    parser = argparse.ArgumentParser(description='Scrape Google images')
    parser.add_argument('-s', '--search', default=keyword, type=str, help='search term')
    parser.add_argument('-n', '--num_images', default=500, type=int, help='num images to save')
    parser.add_argument('-d', '--directory', default=path, type=str, help='save directory')
    args = parser.parse_args()

    query = args.search
    max_images = args.num_images
    save_directory = args.directory
    image_type="Action"
    query= query.split()
    query='+'.join(query)
    url="https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch"
    header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
    soup = get_soup(url, header)
    ActualImages=[]    # contains the link for Large original images, type of  image

    page_nums = 2
    driver = webdriver.Chrome('C:/Users/YY/Documents/Winter Project/chromedriver')
    driver.implicitly_wait(2)
    driver.get(url)

    for page_num in range(page_nums):
        if page_num == 0:
            for a in soup.find_all("div", {"class": "rg_meta"}, string=True):
                link = json.loads(a.text)["ou"]
                Type = json.loads(a.text)["ity"]
                ActualImages.append((link, Type))

            for i, (img, Type) in enumerate(ActualImages[0:len(ActualImages)]):
                try:
                    # req = urllib.request.Request(img, headers={'User-Agent' : header})
                    h = urllib.request.urlopen(img)
                    raw_img = h.read()
                    if len(Type) == 0:
                        f = open(os.path.join(save_directory, keyword + "_" + str(i) + ".jpg"), 'wb')
                        f.write(raw_img)
                        f.close()
                    else:
                        f = open(os.path.join(save_directory, keyword + "_" + str(i) + "." + Type), 'wb')
                        f.write(raw_img)
                        f.close()
                except Exception as e:
                    print("could not load: " + img)
                    print(e)

        else:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)


            driver.find_element_by_xpath('//*[@id="smb"]').click()

            soup = get_soup(url, header)
            ActualImages = []

            for a in soup.find_all("div", {"class": "rg_meta"}, string=True):
                link = json.loads(a.text)["ou"]
                Type = json.loads(a.text)["ity"]
                ActualImages.append((link, Type))

            for i, (img, Type) in enumerate(ActualImages[0:len(ActualImages)]):
                try:
                    # req = urllib.request.Request(img, headers={'User-Agent' : header})
                    h = urllib.request.urlopen(img)
                    raw_img = h.read()
                    if len(Type) == 0:
                        f = open(os.path.join(save_directory, keyword + "_" + str(page_num) + str(i) + ".jpg"), 'wb')
                        f.write(raw_img)
                        f.close()
                    else:
                        f = open(os.path.join(save_directory, keyword + "_" + str(page_num) + str(i) + "." + Type), 'wb')
                        f.write(raw_img)
                        f.close()
                except Exception as e:
                    print("could not load: " + img)
                    print(e)


if __name__ == '__main__':
    from sys import argv
    try:
        main(argv)
    except KeyboardInterrupt:
        pass
    sys.exit()

