from urllib import parse

# urljoin : base와 url를 결합하여 전체 URL를 생성
# geturl : 함수에 의해 분해된 URL 요소를 하나의 URL로 결합
# urlunparse : 튜플 parts로부터 URL를 구성함

iot_url = parse.urljoin('https://home.sch.ac.kr', 'iot')
print('IOT Homepade:', iot_url)

p_url = parse.urlparse(iot_url)
print('Parsed URL:', p_url)
print('Unparsed URL:', p_url.geturl())

url = parse.urlunparse(p_url)
print('Encoded:', url)