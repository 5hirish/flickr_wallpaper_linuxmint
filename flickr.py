
import datetime
import requests
import random
import os
import urllib
from os.path import expanduser
import xml.etree.ElementTree as ET

date = datetime.date.today() - datetime.timedelta(days=2)               # Flickr interseting API Works only if two days before...!?
print(str(date))

api_key = "YOUR-API-KEY"                # Insert your API key here......
number = "5"

flickr_api_test = "https://api.flickr.com/services/rest/?method=flickr.test.echo&name=value&api_key="

flickr_api = "https://api.flickr.com/services/rest/?method=flickr.interestingness.getList&date="+str(date)+"&per_page="+number+"&api_key="

url = flickr_api+api_key
# url = "https://api.github.com/events"
# print(url)

response = requests.get(url, stream=True)

if response.status_code != 200:
    # This means something went wrong.
    print("Error Code:", response.status_code)

xml_data = response.content             # data responded in XML

# xml = ET.parse("sample.xml")      if parsing from file
# root = xml.getroot()

root = ET.fromstring(xml_data)          # need to parse the response body, not the response object
photo_url = []
photos = {'photo_url': 'photo_title'}

for photo in root.findall('./photos/photo'):
    farm_id = photo.get('farm')
    server_id = photo.get('server')
    photo_id = photo.get('id')
    secret = photo.get('secret')
    title = photo.get('title').replace(" ", "_")        # replace spaces from image name...
    size = 'h'                                          # high res images

    flickr_photo_url = "https://farm"+farm_id+".staticflickr.com/"+server_id+"/"+photo_id+"_"+secret+"_"+size+".jpg"        # static image url
    photo_url.append(flickr_photo_url)
    photos[flickr_photo_url] = title            # stores image url and image title

flickr_wallpaper_url = random.choice(photo_url)

home = expanduser("~")
flickr_download_dir = home+"/Pictures/Flickr"               # Flickr Image Download directory

if not os.path.exists(flickr_download_dir):                 # Make directory if not exist
    os.makedirs(flickr_download_dir)

image_name = flickr_download_dir+"/"+photos[flickr_wallpaper_url]+"-"+str(date)+".jpg"      # Absolute path of the .jpg image

urllib.urlretrieve(flickr_wallpaper_url, image_name)

linux_mint_cmd = "gsettings set org.cinnamon.desktop.background picture-uri file:///"+image_name        # Works only on Gnome 3.XX Linux Mint 17.XX Cinnamon
print linux_mint_cmd
os.system(linux_mint_cmd)