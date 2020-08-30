from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Calculate#, CalculateCreateForm, CalculateResult
from .serializers import CalculateSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def getList(request):
    calculate = Calculate.objects.all()
    serializer = CalculateSerializer(calculate, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getTotal(request, pk):
    calculate = Calculate.objects.get(id=pk)
    calculate.total = calculate.number1 + calculate.number2
    serializer1 = {
        'number1': calculate.number1,
        'number2': calculate.number2,
        'total': calculate.total,
    }
    serializer = CalculateSerializer(instance=calculate, data=serializer1)
    print('calculate.total',serializer)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def addTwoNumber(request, num1, num2):
    data = {
        'number1': num1,
        'number2': num2,
        'total': num1 + num2,
    }
    serializer = CalculateSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

def home_page(request):
    listCalculates = Calculate.objects.all()
    context = {
        'list': listCalculates,
    }
    return render(request, 'home.html', context)

# class home_view(TemplateView):
#     def get(self, request, *args, **kwargs):
#         context = {
#             'form': CalculateCreateForm(),
#             'list': Calculate.objects.all(),
#         }
#         return render(request, 'home.html', context)

#     def post(self, request, *args, **kwargs):
#         form = CalculateCreateForm(request.POST)
#         if form.is_valid:
#             calculate = form.save()
#             print(calculate.number1)
#             return self.get(request, *args, **kwargs)
#         content = {
#             'form': form,
#             'list': Calculate.objects.all()
#         }
#         return render(request, 'home.html', content)
