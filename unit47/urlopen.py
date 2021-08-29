from time import time
from urllib.request import Request, urlopen
# 에러 해결: https://multifrontgarden.tistory.com/219
import ssl

context = ssl._create_unverified_context()


urls = ['https://www.google.co.kr/search?q=' + i
        for i in ['apple', 'pear', 'grape', 'pineapple', 'orange', 'strawberry']]

begin = time()
result = []
for url in urls:
    # UA가 없으면 403 에러 발생
    request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urlopen(request, context=context)
    page = response.read()
    result.append(len(page))

print(result)
end = time()
print('실행 시간: {0:.3f}초'.format(end - begin))
