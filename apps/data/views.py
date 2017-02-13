
from django.shortcuts import render
from django.http import HttpResponse
from .models import Curriculum



def home(request):
    print ('hola mundo')
    return render(request, 'home.html', locals())


# def restaurante_list(request):
#     print ('restaurante list api')
#     serializer = None
#     result = {'status': 'error'}
#     time.sleep(5)
#     if request.method == 'GET':
#         restaurantes = Restaurante.objects.all()
#         serializer = RestaurantSerializer(restaurantes, many=True)
#         result = {'status': 'success', 'data': serializer.data}
#     return JSONResponse(result)


# def restaurante_detail(request, id):
#     print ('restaurante detail')
#     serializer = None
#     result = {'status': 'error'}
#     if request.method == 'GET':
#         restaurante = Restaurante.objects.filter(id=id)
#         if restaurante:
#             serializer = RestaurantSerializer(restaurante[0])
#             result = {'status': 'success', 'data': serializer.data}
#     print ('result ', result)
#     return JSONResponse(result)
