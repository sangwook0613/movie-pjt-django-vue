import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')
django.setup()

from movies.models import Genre, Movie, Keyword, Person
import csv

movie_data = open('write.csv','w', newline='')
writer = csv.writer(movie_data)
 
# 컬럼명 생성
column_names = ['id']
for genre in Genre.objects.all():
    column_names.append(f'g_{genre.id}')

for keyword in Keyword.objects.all():
    column_names.append(f'k_{keyword.id}')
print(len(column_names))

writer.writerow(column_names)

cnt = 0
for movie in Movie.objects.all():
    row_data = []
    row_data.append(movie.pk)
    for genre in Genre.objects.all():
        row_data.append(int(genre in Genre.objects.filter(movie__id=movie.pk)))

    for keyword in Keyword.objects.all():
        row_data.append(int(keyword in Keyword.objects.filter(movie_keywords__id=movie.pk)))

    writer.writerow(row_data)
    cnt += 1
    if cnt % 50 == 0:
        print(cnt)
    # print(row_data, len(row_data))

movie_data.close()

# cnt = 0
# for genre in Genre.objects.all():
#     if cnt > 10:
#         break
#     print(genre.pk, genre.name)
#     cnt += 1
# # row데이터 추가
# for i in range(5):
#     temp_row = []
#     for j in range(len(column_names)):
#         temp_row.append(j)
#     writer.writerow(temp_row)


# response['Content-Disposition'] = 'attachment; filename="movie_data.csv"'
# return response
    


# cut_num = 10
# cnt = 0
# for keyword in Keyword.objects.all():
#     if keyword.keyword_count < cut_num:
#         cnt += 1
#         keyword.delete()
#     if cnt % 100 == 0:
#         print(cnt)

# print(cnt)