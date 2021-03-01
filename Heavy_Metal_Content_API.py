from urllib import request, parse

url = 'http://data.ulsan.go.kr/rest/ulsanhmetal/getUlsanhmetalList'
queryParams = '?' + parse.urlencode({ parse.quote_plus('ServiceKey') : '서비스키', parse.quote_plus('pageNo') : '1', parse.quote_plus('numOfRows') : '10',
                                     parse.quote_plus('entId') : '1', parse.quote_plus('mDate') : '2017-01' })

requests = request.Request(url + queryParams)
requests.get_method = lambda: 'GET'
response_body = request.urlopen(requests).read()
#print (response_body)
print(response_body.decode('utf-8'))