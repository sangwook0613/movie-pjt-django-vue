# final pjt

> 초기세팅: final_pjt_back에 .env 파일 만들어서 다음과 같이 사용

```bash
# install 필요
$ pip install python-decouple
# .env
MOVIE_API_KEY={TMDB_KEY}
X_Naver_Client_Id={X_Naver_Client_Id}
X_Naver_Client_Secret={X_Naver_Client_Secret}
```

```python
# movies/views.py
from decouple import config
MOVIE_API_KEY = config('MOVIE_API_KEY')
X_Naver_Client_Id = config('X_Naver_Client_Id')
X_Naver_Client_Secret = config('X_Naver_Client_Secret')
```



```bash
$ python manage.py migrate
$ python manage.py createsuperuser
```



### Commit 규칙

1. 첫 문자는 대문자 and 동사 (Update, Create, Delete...)
2. 두 번째는 front 인지 back 인지 (front, back)
3. 추가한 기능 + (수정한 파일)

```bash
$ git commit -m "Update back signup view.py"

$ git commit -m "Update front movie_detail Detail.Vue"
```











#### 0519

- **movies model 작성**
- **URL 정리** = POSTMAN 파일로 올림 (final_pjt.postman_collection.json)
- account 수업때 했던 코드 옮겨놈
- drf, drf-jwt, cors 설치해놈 -> freeze완료

```python
# top_rated 영화
MOVIE_URL = f'https://api.themoviedb.org/3/movie/top_rated?api_key={token}&language=ko-KR&page={page}'

# popular region = KR
f'https://api.themoviedb.org/3/movie/popular?api_key={token}&language=ko-KR&page={pagee}&region=KR'

# 전체 장르
GENRE_URL = f'https://api.themoviedb.org/3/genre/movie/list?api_key={token}&language=ko-KR'

# 영화의 CREDIT 목록 (PEOPLE)
MOVIE_CREDIT_URL = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={token}&language=ko-KR'

# 배우 DETAIL
ACTOR_DETAIL_URL = f'https://api.themoviedb.org/3/person/{actor_id}?api_key={token}&language=ko-KR'

# 감독 DETAIL
DIRECTOR_DETAIL_URL = f'https://api.themoviedb.org/3/person/{director_id}?api_key={token}&language=ko-KR'

# 영화 KEYWORD
MOVIE_KEYWORD_URL = f'https://api.themoviedb.org/3/movie/{movie_id}/keywords?api_key={token}'
```



- 현재 모델 상황

![image-20210520020642874](README.assets/image-20210520020642874.png)



- 할 일
  1. token 숨기기(.env 사용?)
  2. 영화 POPULAR, NATION 등 지정했을 때 중복 잘 들어가는지 확인하기
  3. url으로 실행하는 법 말고 다른 방법 있는지?
