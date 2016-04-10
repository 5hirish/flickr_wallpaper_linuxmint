
import datetime
import requests
import random
import xml.etree.ElementTree as ET

date = datetime.date.today() - datetime.timedelta(days=2)
print(str(date))

api_key = "YOUR_API_KEY"
number = "5"

flickr_api_test = "https://api.flickr.com/services/rest/?method=flickr.test.echo&name=value&api_key="

flickr_api = "https://api.flickr.com/services/rest/?method=flickr.interestingness.getList&date="+str(date)+"&per_page="+number+"&api_key="

url = flickr_api+api_key
# url = "https://api.github.com/events"
print(url)

response = requests.get(url, stream=True)

if response.status_code != 200:
    # This means something went wrong.
    print("Error Code:", response.status_code)

xml_data = response.content

# xml = ET.parse("sample.xml")      if parsing from file
# root = xml.getroot()

root = ET.fromstring(xml_data)          # need to parse the response body, not the response object
photo_url = []

for photo in root.findall('./photos/photo'):
    farm_id = photo.get('farm')
    server_id = photo.get('server')
    photo_id = photo.get('id')
    secret = photo.get('secret')
    title = photo.get('title')
    size = 'h'

    flickr_photo_url = "https://farm"+farm_id+".staticflickr.com/"+server_id+"/"+photo_id+"_"+secret+"_"+size+".jpg"
    photo_url.append(flickr_photo_url)

print(random.choice(photo_url))