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

# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except(KeyError, Choice.DoesNotExist):
#         return render(request, 'polls/detail.html', {'question': question, 'error_message': "you didn't select a choice."})
#
#     else:
#         selected_choice.votes += 1
#         selected_choice.save()
#         return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
#
# def results(request, question_id):
#         question = get_object_or_404(Question, pk=question_id)
#         return render(request, 'polls/results.html', {'question': question})