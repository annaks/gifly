import urllib2
import ujson as json

API_KEY=''
API_URL='https://api-ssl.bitly.com'

HIGH_VALUE_API = '/v3/highvalue?access_token='+ API_KEY +'&limit='
LINK_INFO_API = '/v3/link/info?access_token='+ ACCESS_TOKEN +'&link='


limit = 10
url = API_URL + HIGH_VALUE_API + str(limit)
request = urllib2.urlopen(url)
data = json.loads(request.read())

return_urls = data['values']
