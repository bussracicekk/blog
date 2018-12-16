from django.shortcuts import render, HttpResponse


def post_index(request):
    return HttpResponse('Here is index page of post')


def post_detail(request):
    return HttpResponse('Here is detail page of post')


def post_create(request):
    return HttpResponse('Here is create page of post')


def post_update(request):
    return HttpResponse('Here is update page of post')


def post_delete(request):
    return HttpResponse('Here is delete page of post'),




