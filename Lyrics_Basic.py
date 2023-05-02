# bs4로 부터 BeautifulSoup을 불러온다. 외부모듈을 통한 함수. 대문자, 철자 유의

from bs4 import BeautifulSoup

# requests는 요청하는것. import를 통해 함수를 사용한다.

import requests

# 요청. 값을 불러올때나 존재하는지 확인하는 get을 사용하여 키를넣어줌 URL

resp = requests.get("https://lyricstranslate.com/en/Muse-Time-Running-Out-lyrics.html")


# soup 라는 별칭으로 BeautifulSoup을 통해 html의 마크업 구분으로 해당 사이트의 텍스트를 불러온다.
soup = BeautifulSoup(resp.text, 'html.parser')

# mydivs라는 별칭으로 위의 별칭에서 div, class키의 ltf direction-ltr 값을 가져온다. 해당 값은 개발자모드에서 위치를 통해 확인한다.

mydivs = soup.find('div',{'class':'ltf direction-ltr'})

#lyric라는 별칭으로 위의 별칭에서 div 의 부분을 전부 찾아준다.

lyric = mydivs.find_all('div')

#sentence라는 별칭으로 lyric 안에서 텍스트를 반복print한다.

for sentence in lyric:


    print(sentence.text)

