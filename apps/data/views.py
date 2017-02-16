
from django.shortcuts import render
from django.http import HttpResponse
from textblob import TextBlob as tb
from .tfidf import tfidf
from .models import Curriculum


def home(request):
    print ('hola mundo')
    curriculums = Curriculum.objects.all()

    bloblist = [tb(curriculum.algoritmo_texto) for curriculum in curriculums]
    for i, blob in enumerate(bloblist):
        print("Top words in document {}".format(i + 1))
        scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
        sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        for word, score in sorted_words[:3]:
            print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))

    return render(request, 'home.html', locals())


