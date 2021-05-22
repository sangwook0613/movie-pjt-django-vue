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



### front

> npm i + .env.local 에 아래꺼 추가

```bash
VUE_APP_SERVER_URL=http://127.0.0.1:8000
```



### Commit 규칙

1. 첫 문자는 대문자 and 동사 (Update, Create, Delete...)
2. 두 번째는 front 인지 back 인지 (front, back)
3. 추가한 기능 + (수정한 파일)

```bash
$ git commit -m "Update back signup view.py"

$ git commit -m "Update front movie_detail Detail.Vue"
```



### Git branch

```bash
# 확인
$ git branch

# 생성
$ git branch <branch name>

# 이동
$ git switch <branch name>

# 삭제
$ git branch -D <branch name>

# 병합
$ git merge <branch name>
$ git log --oneline --graph
$ git branch -d <branch name> 삭제해준다
```



#### 작업 순서

1. 생성
2. 이동
3. 작업 (이동한 branch에서 작업)
4. git push (작업한 branch에서 push)
   - $ git push origin `<branch name>`
5. 원격 저장소에서 merge(pull request)
6. 충돌 없으면 merge 하고, 충돌 있으면 상의
7. 로컬 + 원격에서  branch 삭제





#### 0519

- **movies model 작성**
- **URL 정리**
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





#### 0520

- 현재 모델 상황
- Director + Actor = Person 으로 교체

![image-20210520181056564](README.assets/image-20210520181056564.png)



- server/url 수정 완료
- 전체 영화, 단일 영화 시리얼라이즈+view 완료
- serializers 추천 알고리즘, Profile 제외하고 완료

#### 0521

- serializers profile, 검색
- profile 페이지 초안 완료





## 고민해야 할 사항

### 0520

#### back

1. review 작성 시 영화를 DB에 있는 것만 작성을 할 수 있게 하려고 하는데 선택지가 너무 많아진다
   - 해결할 방법 필요 or 검색
2. Keyword 번역문제 아직 해결 안됨
3. user_profile_image => 사진으로 하면 저장할 방법 필요 => 캐릭터같은거 선택지를 준다.
4. movie에 연결된 like와 hate 각각 처리했는데, like가 눌리면 hate가 취소되고 반대로도 되야함
   - front랑 back 에서 모두 처리해야 할듯

### 0521

#### back

1. keyword로 검색 기능 구현해야함

3. 키워드 관련 전처리 필요
   - 키워드를 비율로 보고 정리할지? 혹은 일정 count 수가 안되면 바로 삭제할지?
   - 만약 키워드가 하나도 없는 영화가 있다면 어떻게 보여줄지?

#### front

