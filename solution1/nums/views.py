from urllib import response
from django.shortcuts import render
from django.http import JsonResponse
from .url_regex import check_valid_url
import requests

# Create your views here.


def index(request):
    # http://localhost:port/numbers?url=http://something.com/primes&url=http://anything.com/fibo
    urls = request.GET.getlist('url')
    final_nums = set()
    valid_urls = []
    for url in urls:
        if check_valid_url(url):
            valid_urls.append(url)

    response_data = {}
    response_data["urls"] = valid_urls

    for url in valid_urls:
        nums_res = requests.get(url)
        nums_dict = nums_res.json()
        new_numbers = nums_dict["numbers"]
        print(new_numbers)
        for num in new_numbers:
            final_nums.add(num)

    print("final_nums")
    print(final_nums)
    response_data["numbers"] = list(final_nums)

    return JsonResponse(response_data)
