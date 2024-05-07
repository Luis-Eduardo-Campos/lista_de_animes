from django.shortcuts import render,redirect,HttpResponse
from .models import Registro_de_anime
from .forms import Registro_de_animeForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def lista_de_animes(request):
    dados = {
        'dados': Registro_de_anime.objects.all()
    }
    return render(request, 'informacoes/lista_de_animes.html', context=dados)

def detalhe(request, id_anime):
    dados = {
        'dados': Registro_de_anime.objects.get(pk=id_anime)
    }
    return render(request, 'informacoes/detalhe.html', dados)

@login_required
def criar(request):
    if request.method == 'POST':
        registro_de_anime_form = Registro_de_animeForm(request.POST)
        if registro_de_anime_form.is_valid():
            registro_de_anime_form.save()
        return redirect('lista_de_animes')
    else:    
        registro_de_anime_form = Registro_de_animeForm()
        formulario = {
            'formulario': registro_de_anime_form
        }
        return render(request, 'informacoes/novo_anime.html', context=formulario)

@login_required    
def editar(request, id_anime):
    registro_de_anime = Registro_de_anime.objects.get(pk=id_anime)
    # novo_anime/1 -> GET
    if request.method == 'GET':
        formulario = Registro_de_animeForm(instance=registro_de_anime)
        return render(request, 'informacoes/novo_anime.html', {'formulario':formulario})
    # caso a requisição seja POST
    else:
        formulario = Registro_de_animeForm(request.POST, instance=registro_de_anime)
        if formulario.is_valid():
            formulario.save()
        return redirect('lista_de_animes')

@login_required    
def excluir(request, id_anime):
    registro_de_anime = Registro_de_anime.objects.get(pk=id_anime)
    if request.method == 'POST':
        registro_de_anime.delete()
        return redirect('lista_de_animes')
    return render(request, 'informacoes/confirmar_exclusao.html', {'item': registro_de_anime})



