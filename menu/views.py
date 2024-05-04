from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ItemSerializers
from .models import Item


# def item_list(request):
#     items = Item.objects.all()
#     query_set = []
#     for item in items:
#         query_set.append({
#             "name": item.name,
#             "price": item.price,
#             "description": item.description,
#         })
#     return JsonResponse(query_set, safe=False)

@api_view(['GET'])
def query_set(request):
    items = Item.objects.all()
    serializer = ItemSerializers(items, many=True)
    return Response(serializer.data)

def query_set_serialized(request):
    items = Item.objects.all()
    serializer = ItemSerializers(items, many=True)
    return JsonResponse(serializer.data, safe=False)

@api_view(['GET'])
def query_detail(request, pk):
    item = Item.objects.get(id=pk)
    serializer = ItemSerializers(item)
    return Response(serializer.data)

