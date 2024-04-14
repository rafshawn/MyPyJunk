import os
import requests
from bs4 import BeautifulSoup
import wget
from urllib.parse import urljoin

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
    img_url = urljoin(url, img['src'])
    file_name = img['src'].split('/')[-1]
    try:
        wget.download(img_url, out=os.path.join(download_folder, file_name))
    except Exception as e:      # Ignores exceptions (HTTPSerrors, etc.) and moves on to next download
        print(f"Error downloading {img_url}: {e}")
