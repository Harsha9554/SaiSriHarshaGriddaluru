from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def find_prefix(word, words):
    words.remove(word)
    max_len = 0
    for w in words:
        n = min(len(word), len(w))
        cur = 0
        i, j = 0, 0
        while i < n and j < n:
            if w[i] == word[i]:
                i += 1
                j += 1
                cur += 1
            else:
                break
        max_len = max(max_len, cur)

    return word[:max_len+1]


def index(request):
    words = ['bonfire', 'cardio', 'case', 'character', 'bonsai']
    words = sorted(words)
    keywords = request.GET.getlist('keywords')

    response_data = []

    sp_keywords = keywords[0].split(',')
    print(sp_keywords)

    for word in sp_keywords:
        if word in words:
            prefix = find_prefix(word, words)
            print(prefix)
            response_data.append({
                "keyword": word,
                "status": "found",
                "prefix": prefix
            })
        else:
            response_data.append({
                "keyword": word,
                "status": "not_found",
                "prefix": "not_applicable"

            })

    return JsonResponse(response_data, safe=False)
