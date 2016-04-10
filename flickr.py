
import datetime
from urllib2 import URLError
import requests

date = datetime.date.today() - datetime.timedelta(days=2)
print(str(date))

api_key = "YOUR_API_KEY"
number = "5"

flickr_api_test = "https://api.flickr.com/services/rest/?method=flickr.test.echo&name=value&api_key="

flickr_api = "https://api.flickr.com/services/rest/?method=flickr.interestingness.getList&date="+str(date)+"&per_page="+number+"&format=json&api_key="

# url = flickr_api+api_key
url = "https://api.github.com/events"
print(url)

response = requests.get(url)
json_data = response.json()
print(json_data)
