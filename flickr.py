import datetime
import requests
import random
import os
import urllib
from os.path import expanduser
import xml.etree.ElementTree as ET


def get_interesting_image_id(furl):
    response = requests.get(furl, stream=True)

    if response.status_code != 200:
        # This means something went wrong.
        print("Error Code:", response.status_code)

    return response.content


def get_flickr_wallpaper_url(froot, fphotos):
    photo_url = []

    for photo in froot.findall('./photos/photo'):
        farm_id = photo.get('farm')
        server_id = photo.get('server')
        photo_id = photo.get('id')
        secret = photo.get('secret')
        title = photo.get('title').replace(" ", "_")  # replace spaces from image name...
        size = 'h'  # high res images

        flickr_photo_url = "https://farm" + farm_id + ".staticflickr.com/" + server_id + "/" + photo_id + "_" + secret + "_" + size + ".jpg"  # static image url
        photo_url.append(flickr_photo_url)
        fphotos[flickr_photo_url] = title  # stores image url and image title

    return random.choice(photo_url)


def download_image_set_wallpaper(flickr_wallpaper_url, image_name):
    urllib.urlretrieve(flickr_wallpaper_url, image_name)

    linux_mint_cmd = "gsettings set org.cinnamon.desktop.background picture-uri file:///" + image_name  # Works only on Gnome 3.XX Linux Mint 17.XX Cinnamon
    linux_mint_cmd = linux_mint_cmd.decode("utf-8")
    print linux_mint_cmd
    os.system(linux_mint_cmd)


date = datetime.date.today() - datetime.timedelta(days=2)  # Flickr interseting API Works only if two days before...!?
print(str(date))


api_key = "YOUR_API_KEY"  # Insert your API key here....

number = "5"

# flickr_api_test = "https://api.flickr.com/services/rest/?method=flickr.test.echo&name=value&api_key="
flickr_api = "https://api.flickr.com/services/rest/?method=flickr.interestingness.getList&date=" + str(
        date) + "&per_page=" + number + "&api_key="

url = flickr_api + api_key
# url = "https://api.github.com/events"
# print(url)

xml_data = get_interesting_image_id(url)  # data responded in XML

# xml = ET.parse("sample.xml")      if parsing from file
# root = xml.getroot()

root = ET.fromstring(xml_data)  # need to parse the response body, not the response object
photos = {'photo_url': 'photo_title'}
flickr_wallpaper_url = get_flickr_wallpaper_url(root, photos)

home = expanduser("~")
flickr_download_dir = home + "/Pictures/Flickr"  # Flickr Image Download directory

if not os.path.exists(flickr_download_dir):  # Make directory if not exist
    os.makedirs(flickr_download_dir)

image_name = flickr_download_dir + "/" + photos[flickr_wallpaper_url] + "-" + str(
        date) + ".jpg"  # Absolute path of the .jpg image

today_image_set = False

for img in os.listdir(flickr_download_dir):
    if img.endswith(".jpg") and img.find(str(date)) != -1:  # download only if today's image is not present
        today_image_set = False
    else:
        today_image_set = True


if not today_image_set:
    download_image_set_wallpaper(flickr_wallpaper_url, image_name)
else:
    print "Today's image already set...!"
