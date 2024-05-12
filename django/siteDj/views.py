from django.shortcuts import render

# Create your views here.

def cont(request):
    x = "Olá, mundo!\n Lista de ingredientes que preciso comprar para meu almoço hoje."
    listaCompra = ["Arros", "Feijão", "Macarrão", "Massa de Tomate", "Óleo"]
    return render(request,'index.html',{'x': x, 'listaCompra': listaCompra})