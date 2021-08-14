lines = ['안녕하세요.\n', '파이썬\n', '코딩 도장입니다.\n']
with open('./unit27/hello.txt', 'w') as file:    # hello.txt 파일을 쓰기 모드(w)로 열기
    file.writelines(lines)

with open('./unit27/hello.txt', 'r') as file:    # hello.txt 파일을 읽기 모드(r)로 열기
    lines = file.readlines()  # 리스트로 파일 내 문장들을 가져온다.
    print(lines)

with open('./unit27/hello.txt', 'r') as file:
    line = None    # 변수 line을 None으로 초기화
    while line != '':
        line = file.readline()
        print(line.strip('\n'))    # 파일에서 읽어온 문자열에서 \n 삭제하여 출력

with open('./unit27/hello.txt', 'r') as file:    # hello.txt 파일을 읽기 모드(r)로 열기
    for line in file:    # for에 파일 객체를 지정하면 파일의 내용을 한 줄씩 읽어서 변수에 저장함
        print(line.strip('\n'))    # 파일에서 읽어온 문자열에서 \n 삭제하여 출력

with open('./unit27/hello.txt', 'r') as file:     # hello.txt 파일을 읽기 모드(r)로 열기
    a, b, c = file
    print({a, b, c})
