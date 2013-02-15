import urllib2
import ujson as json
import pprint

ACCESS_TOKEN=open('API_KEY.no').read()
API_URL='https://api-ssl.bitly.com'

HIGH_VALUE_API = '/v3/highvalue?access_token='+ ACCESS_TOKEN +'&limit='
LINK_INFO_API = '/v3/link/info?access_token='+ ACCESS_TOKEN +'&link='

#get high value links
limit = 10
url = API_URL + HIGH_VALUE_API + str(limit)
request = urllib2.urlopen(url)
data = json.loads(request.read())

return_urls = data['data']['values']

#create an empty list to hold the image links
image_links = []

#for each high value link, return the link info
for link in return_urls:
    url = API_URL + LINK_INFO_API + link
    request = urllib2.urlopen(url)
    data = json.loads(request.read())
    #check to see if link is an image, if so then we add it to image_links
    if data['data']['category'] == 'image':
        image_links.append(link)
