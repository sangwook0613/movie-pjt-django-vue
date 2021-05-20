# DB 정리

## BASE API = TMDB API

### 1. Movie 테이블

#### API

- movies - Get Popular `/movie/popular`
- movies - Get Top Rated `/movie/top_rated`

query string

- api_key
- language = ko-KR
- page - 최대 페이지까지
- region - 아무것도 없는 default인 경우와 `KR` 로 설정한 경우 2가지

#### 컬럼명

draw.io 참고

#### 기타

- page를 고려하지 않았을 때 총 4개의 API를 부른다! (popular 에서 region 2가지, top_rated 에서 region 2가지)

- 각 api 를 불러왔을 때 중복되는 영화는 제외처리

- 키워드와 배우는 몇명까지 보여줄지 고민 필요

  

### 2. Genre 테이블

#### API

- genres - Get Detail `/genre/movie/list`

query string

- api_key
- language = ko-KR

#### 컬럼명

ID / 장르명

#### 기타

- 참고 주소 = https://api.themoviedb.org/3/genre/movie/list?api_key=2f6e2467882449898b073c342aa59532&language=ko-KR
- 위 주소에서 나오는 값만 저장하면 됨



### 3. Keyword 테이블

#### API

- keywords - Get Detail `/keyword/{keyword_id}`
- movies - Get Keywords `/movie/{movie_id}/keywords`
- 파파고 번역 API

query string

- api_key
- 각각 keyword_id 와 movie_id 는 필수

#### 컬럼명

ID / 한글명 / 영어명 / count

#### 기타

- 구성하는 방식

  1. keywords의 Get Detail API에 1부터 100만? 정도까지 수를 하나씩 넣어보면서, 정상적인 결과를 반환하면 해당, id 와 영어명을 keyword 테이블에 넣어준다.

  2. movie의 Get Keywords 를 통해 각 영화 id 가 갖고 있는 keyword_id 확인하여, keyword 테이블의 count 를 세준다.

     이 때, 만약 keyword 테이블에 없는 keyword가 있다면 추가해준다.

  3. 위 과정이 다 끝난 후, 파파고 번역 API를 활용하여 keyword 테이블에 한글명을 추가해준다.



### 4. Actor, Director 테이블

#### API

- people - Get Detail `/person/{person_id}`
- movies - Get Credits `/movie/{movie_id}/credits`
- 파파고 언어감지 API

query string

- api_key
- 각각 person_id 와 movie_id 는 필수
- language도 ko-KR로 추가하자

#### 컬럼명

ID / 한글명 / 영어명 / image / 성별(여자 - 1, 남자 - 2)

#### 기타

- 구성하는 방식 (Actor, Director 모두 같으며, 설명은 actor 로 진행)

  1. people 의 Get Detail API에 1부터 100만? 정도까지 수를 하나씩 넣어보면서, 정상적인 결과를 반환하면 해당, id 와 영어이름, 한글이름, image 주소, 성별을 people 테이블에 넣어준다.

     이 때, 한글이름을 찾기 위해서, 파파고 언어감지 API를 통해 `also_known_as` 의 value 에서 한글명을 찾아낸다.

     - 영어 이름은 `name` 이라는 key 값의 value이다.

  2. movie의 Get Credits 를 통해 각 영화 id 가 갖고 있는 person_id 확인하여, movie 테이블에 배우들의 id를 채워준다.

     단, 이 때, actor 테이블에 있는 배우들만 추가해야한다! 그렇기에 만약 actor 테이블에 없는 actor가 있다면 따로 저장 후, actor 테이블에 보충해야한다.

     

- Director 참고 예시 (봉준호 감독)

   "job": "Director" => "id": 21684,https://api.themoviedb.org/3/movie/496243/credits?api_key=2f6e2467882449898b073c342aa59532&language=ko-KR

