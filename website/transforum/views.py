from django.http.response import HttpResponse
from django.shortcuts import render
from .models import TransTreeNode
import json

import logging as logger

# list
def origin_list(request):
    query_set = TransTreeNode.objects.filter(
        parent_id=-1).order_by('-likes').values()
    query_set = list(query_set)
    query_set = json.dumps(query_set, default=str)
    return HttpResponse(query_set, content_type='application/json')


# single trans tree
def trans_tree(request, id):
    result = TransTreeNode.objects.filter(
        id=id).values().first()

    child_list = TransTreeNode.objects.filter(
        parent_id=id).order_by('-likes').values()
    child_list = list(child_list)

    result['child_list'] = child_list
    result = json.dumps(result, default=str)
    return HttpResponse(result, content_type='application/json')
