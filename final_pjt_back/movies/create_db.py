import requests
from bs4 import BeautifulSoup
from pprint import pprint
from decouple import config

from .models import Genre, Movie, Keyword, Person

### 사용할 API 정리
NAVER_PAPAGO_DETECT_URL = 'https://openapi.naver.com/v1/papago/detectLangs'
NAVER_PAPAGO_TRANSLATE_URL = 'https://openapi.naver.com/v1/papago/n2mt'
MOVIE_API_KEY = config('MOVIE_API_KEY')
X_Naver_Client_Id = config('X_Naver_Client_Id')
X_Naver_Client_Secret = config('X_Naver_Client_Secret')
headers = {'X-Naver-Client-Id': X_Naver_Client_Id, 'X-Naver-Client-Secret': X_Naver_Client_Secret,
            'Content-Type': 'application/x-www-form-urlencoded','charset':'utf-8'}
MOVIE_POPULAR_URL = f'https://api.themoviedb.org/3/movie/popular?api_key={MOVIE_API_KEY}&language=ko-KR&region=KR'
MOVIE_TOP_RATED_URL = f'https://api.themoviedb.org/3/movie/top_rated?api_key={MOVIE_API_KEY}&language=ko-KR&region=KR'
GENRE_URL = f'https://api.themoviedb.org/3/genre/movie/list?api_key={MOVIE_API_KEY}&language=ko-KR'
MOVIE_API_URL = [MOVIE_POPULAR_URL, MOVIE_TOP_RATED_URL]


def createDB(request):
    for i in range(2):
        page = 1    
        while page <= 10: # 최대 500페이지이기에 500번 반복 진행
            MOVIE_URL = f'{MOVIE_API_URL[i]}&page={page}'
            # 전체 장르 테이블 만들때 사용
            request_movies = requests.get(MOVIE_URL).json()
            request_genres = requests.get(GENRE_URL).json()
            genres = request_genres.get('genres')
            movies = request_movies.get('results')
            for genre in genres:
                genre_id = genre.get('id')
                genre_name = genre.get('name')
                genre_data = Genre(id=genre_id, name=genre_name)
                genre_data.save()
            
            for movie in movies:
                movie_id = movie.get('id')
                movie_title = movie.get('title')
                movie_original_title = movie.get('original_title')
                movie_overview = movie.get('overview')
                movie_poster_path = movie.get('poster_path')
                movie_release_date = movie.get('release_date')
                movie_backdrop_path = movie.get('backdrop_path')
                movie_genres = movie.get('genre_ids')
                vote_average = movie.get('vote_average')
                vote_count = movie.get('vote_count')

                # 예외 처리
                ## 줄거리가 없는 경우 저장하지 않는다.
                if movie_overview == '':
                    break

                # DEATIL API 에서 추가 정보 받아오기
                MOVIE_DETAIL_URL = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={MOVIE_API_KEY}&language=ko-KR'
                movie_detail = requests.get(MOVIE_DETAIL_URL).json()
                movie_runtime = movie_detail.get('runtime')

                movie_data = Movie(title=movie_title, original_title=movie_original_title, overview=movie_overview,
                    poster_path=f'https://image.tmdb.org/t/p/original{movie_poster_path}', runtime=movie_runtime,
                    backdrop_path=f'https://image.tmdb.org/t/p/original{movie_backdrop_path}', release_date=movie_release_date,
                    vote_average=vote_average, vote_count=vote_count)

                # 영화 제목으로 중복 체크
                if not Movie.objects.filter(title=movie_title).exists():
                    movie_data.save()
                    # 해당 영화 장르 M:N 테이블에 추가
                    for g in movie_genres:
                        movie_data.genres.add(g)
                else:
                    continue

                # CREDIT에서 people 정보 받아오기
                MOVIE_CREDIT_URL = f'https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key={MOVIE_API_KEY}&language=ko-KR'
                movie_credit = requests.get(MOVIE_CREDIT_URL).json()
                cast = movie_credit.get('cast')
                crew = movie_credit.get('crew')
                cnt_actor = cnt_director = 0
                
                # 배우
                for people in cast:
                    if people.get('profile_path') and people.get('known_for_department') == 'Acting':
                        # 10개만 추출
                        if cnt_actor == 10:
                            continue
                        actor_id = people.get('id')
                        actor_gender = people.get('gender')
                        actor_name = people.get('name')
                        actor_eng_name = people.get('original_name')
                        actor_profile_path = people.get('profile_path')
                        # Actor id에 해당하는 actor detail로 요청
                        ACTOR_DETAIL_URL = f'https://api.themoviedb.org/3/person/{actor_id}?api_key={MOVIE_API_KEY}&language=ko-KR'
                        actor_detail = requests.get(ACTOR_DETAIL_URL).json()
                        names = actor_detail.get('also_known_as')
                        for name in names:
                            # PAPAGO 언어 감지 결과 한글이면
                            NAVER_LANGEAGE_URL = f'{NAVER_PAPAGO_DETECT_URL}?query={name}'
                            # 파파고 요청 : post + header 필요
                            test_result_language = requests.post(NAVER_LANGEAGE_URL,headers=headers).json()
                            if test_result_language.get('langCode') == 'ko':
                                # actor_name = 한글 이름으로 교체
                                actor_name = name
                                break

                        # Actor 테이블에 중복검사
                        if not Person.objects.filter(id=actor_id).exists():
                            # 테이블에 없는 배우면 추가
                            people_data = Person(id=actor_id, gender=actor_gender, name=actor_name, 
                                eng_name=actor_eng_name, profile_path=f'https://image.tmdb.org/t/p/original{actor_profile_path}',
                                job='Actor')
                            people_data.save()

                        # 해당 영화 배우들 M:N 테이블에 추가
                        movie_data.actors.add(actor_id)
                        cnt_actor += 1
                        
                # 감독
                for people in crew:
                    # 감독 = 1명
                    if cnt_director == 1:
                            break
                    if people.get('job') == 'Director':
                        director_id = people.get('id')
                        director_gender = people.get('gender')
                        director_name = people.get('name')
                        director_eng_name = people.get('original_name')
                        director_profile_path = people.get('profile_path')

                        DIRECTOR_DETAIL_URL = f'https://api.themoviedb.org/3/person/{director_id}?api_key={MOVIE_API_KEY}&language=ko-KR'
                        director_detail = requests.get(DIRECTOR_DETAIL_URL).json()
                        names = director_detail.get('also_known_as')
                        for name in names:
                            # PAPAGO 언어 감지 결과 한글이면
                            NAVER_LANGEAGE_URL = f'{NAVER_PAPAGO_DETECT_URL}?query={name}'
                            # 파파고 요청 : post + header 필요
                            test_result_language = requests.post(NAVER_LANGEAGE_URL,headers=headers).json()
                            if test_result_language.get('langCode') == 'ko':
                                # director_name = 한글 이름으로 교체
                                director_name = name
                                break

                        # Director 테이블에 중복검사
                        if not Person.objects.filter(id=director_id).exists():
                            # 테이블에 없는 감독이면 추가         
                            director_data = Person(id=director_id, gender=director_gender, name=director_name, 
                                eng_name=director_eng_name, profile_path=f'https://image.tmdb.org/t/p/original{director_profile_path}',
                                job='Director')
                            director_data.save()
                        
                        # 해당 영화 배우들 M:N 테이블에 추가
                        movie_data.directors.add(director_id)
                        cnt_director += 1
                
                MOVIE_KEYWORD_URL = f'https://api.themoviedb.org/3/movie/{movie_id}/keywords?api_key={MOVIE_API_KEY}'
                movie_keywords = requests.get(MOVIE_KEYWORD_URL).json()
                keywords = movie_keywords.get('keywords')
                for keyword in keywords:
                    keyword_id = keyword.get('id')
                    keyword_eng_name = keyword.get('name')
                    # 키워드 없으면 추가
                    if not Keyword.objects.filter(id=keyword_id).exists():
                        keyword_data = Keyword(id=keyword_id, keyword_eng_name=keyword_eng_name,)
                        keyword_data.save()

                        # 파파고 번역기
                    #     data = {
                    #         'text' : keyword_eng_name,
                    #         'source': 'en',
                    #         'target' : 'ko',
                    #     }
                    #     translate_result = requests.post(NAVER_PAPAGO_TRANSLATE_URL, headers=headers, data=data).json()
                    #     keyword_name = translate_result.get('message').get('result').get('translatedText')
                        
                    #     # 저장
                    #     keyword_data = Keyword(id=keyword_id, keyword_name=keyword_name, keyword_eng_name=keyword_eng_name,)
                    #     keyword_data.save()
                    else:
                        keyword_data = Keyword.objects.get(id=keyword_id)
                        keyword_data.keyword_count = keyword_data.keyword_count + 1
                        keyword_data.save()

                    # movie:keyword M:N 관계에 id 추가
                    movie_data.keywords.add(keyword_id)

            page += 1


    ### 키워드 전처리 작업 진행
    # cut_num = 10
    # for keyword in Keyword.objects.all():
    #     if keyword.keyword_count < cut_num:
    #         keyword.delete()
    