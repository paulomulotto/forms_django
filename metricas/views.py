from django.shortcuts import render
from django.http import HttpResponse

from .forms import  MetricForm, MetricListView
from .models import Metrica

import numpy

from django.db.models import Avg

def index(request):

    lista_metricas = []

    print("\n--------------------------------")
    print("Qual é o método da requisição?")
    print("Em geral, GET é utilizado para acessar a página pela primeira vez. Dessa forma, o usuário ainda não está informando nenhuma informação de filtro, por exemplo.")
    print("O POST é utilizado para enviar as informações de forma encapsulada. Quando o usuário aplicar o filtro, ele irá realizar uma requisição POST para dar as informações de input para a nossa função.")

    form = MetricForm()
    print("\n--------------------------------")
    print("Como é renderizado o formulário criado?")
    print(form.as_table())
    print("\n Isso significa que o forms já está construindo a estrutura de dados")

    
    if request.method == 'POST':
        print("\n--------------------------------")
        print("Esta requisição é um POST")
        print("Isso significa que o usuário está enviando informações para nós de forma encapsulada")
        print("Veja como essas informações estão dispostas")
        print(request.POST)

        print("Agora vamos obter as informações que precisamos filtrar.")
        print("Nome: ", request.POST.get('nome', ''))
        print("Granularidade: ", request.POST.get('granularidade', ''))
        nome = request.POST.get('nome')
        
        granularidade = request.POST.get('granularidade')


        print("Iniciamos obtendo todas as métricas por default")
        lista_metricas = Metrica.objects.all()
        
        print("Agora, baseado nos parâmetros recebidos, iremos realizar o filtro")
        lista_metricas = lista_metricas.filter(nome=nome)

        print("Esse filtro, deveria ser realizado dentro do forms para facilitar implementações futuras e manutenções")
        lista_metricas = form.get_metricas(nome=nome)


    elif request.method == 'GET':
        print("\n--------------------------------")
        print("Esta requisição é um GET")
        print("Isso significa que o usuário está acessando a página para realizar seu trabalho")
        print("Veja quais são as informações recebidas")
        print(request.GET)

    


    context = {
        'form': form,
        'lista_metricas': lista_metricas
    }

    return render(request, 'metricas/form.html', context)