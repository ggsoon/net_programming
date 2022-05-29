from urllib import parse, request

query = {'temperature': '25', 'humidity': '60'}
encoded_query = parse.urlencode(query)
url = 'http://localhost:8080/'
get_url = url + '?' + encoded_query

#GET
rsp = request.urlopen(get_url)
print(rsp.read().decode())