from time import time
from urllib.request import Request, urlopen
# 에러 해결: https://pythonq.com/so/python/857608
import functools
import asyncio
import ssl

context = ssl._create_unverified_context()

urls = ['https://www.google.co.kr/search?q=' + i
        for i in ['apple', 'pear', 'grape', 'pineapple', 'orange', 'strawberry']]


async def fetch(url):
    # UA가 없으면 403 에러 발생
    request = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    # run_in_executor 사용
    response = await loop.run_in_executor(None, functools.partial(urlopen, request, context=context))
    # run in executor 사용
    page = await loop.run_in_executor(None, response.read)
    return len(page)


async def main():
    futures = [asyncio.ensure_future(fetch(url)) for url in urls]
    # 태스크(퓨처) 객체를 리스트로 만듦
    result = await asyncio.gather(*futures)                # 결과를 한꺼번에 가져옴
    print(result)

begin = time()
loop = asyncio.get_event_loop()          # 이벤트 루프를 얻음
loop.run_until_complete(main())          # main이 끝날 때까지 기다림
loop.close()                             # 이벤트 루프를 닫음
end = time()
print('실행 시간: {0:.3f}초'.format(end - begin))
