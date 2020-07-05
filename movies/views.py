from django.shortcuts import render, get_object_or_404
from movies.models import Movie, Information
from django.http import HttpResponseRedirect
from django.urls import reverse

def main(request):
    latest_movie_list = Movie.objects.all().order_by('-pub_date')[:5]
    context = {'latest_movie_list': latest_movie_list}
    print(latest_movie_list)
    return render(request, 'movies/main.html', context)


def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})

def movie_list(request):
    qs = movie.objects.all()

    q = request.GET.get('q', '') # GET request의 인자중에 q 값이 있으면 가져오고, 없으면 빈 문자열 넣기
    if q: # q가 있으면
        qs = qs.filter(title__icontains=q) # 제목에 q가 포함되어 있는 레코드만 필터링

    return render(request, 'movies/movie_list.html', {
        'movie_list' : qs,
        'q' : q,
    })