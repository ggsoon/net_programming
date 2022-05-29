from urllib import parse
url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_sly.hst&fbm=1&acr=1&ie=utf8&query=%ED%94%84%EB%A6%AC%EB%AF%B8%EC%96%B4%EB%A6%AC%EA%B7%B8'
parsed_url = parse.urlparse(url)
print(parsed_url)
print('scheme :', parsed_url.scheme)
print('netloc :', parsed_url.netloc)
print('path :', parsed_url.path)
print('params :', parsed_url.params)
print('query :', parsed_url.query)
print('fragment:', parsed_url.fragment)

parsed_url = parse.urlsplit(url)
print(parsed_url)
print('scheme :', parsed_url.scheme)
print('netloc :', parsed_url.netloc)
print('path :', parsed_url.path)
print('query :', parsed_url.query)
print('fragment:', parsed_url.fragment)