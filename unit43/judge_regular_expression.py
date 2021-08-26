import re

url = input()
r = re.compile('^https?:\/\/[-\w]+(\.[-\w]+)+(\/[-.?=\w]+)+$')
if r.match(url):
    print('True')
else:
    print('False')
