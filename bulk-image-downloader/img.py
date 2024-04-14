import os
import requests
from bs4 import BeautifulSoup
import wget

url = 'https://www.cs.mun.ca/~harold/'
download_folder = 'downloads'

# Create downloads folder if doesn't exist
if not os.path.exists(download_folder):
    os.makedirs(download_folder)

# Send get request, parse with bs4, and get all images
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
imgs = soup.find_all('img')
print('Images Found:')
for img in imgs:
    print(img, end=',\n')

for img in imgs:
    img_url = os.path.join(url, img['src'])
    file_name = img['src'].split('/')[-1]
    wget.download(img_url, out=os.path.join(download_folder, file_name))