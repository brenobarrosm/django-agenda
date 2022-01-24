from django.shortcuts import redirect, render, get_object_or_404
from django.http import Http404
from .models import Contato
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.contrib import messages

def index(request):

    contatos = Contato.objects.order_by('-id').filter(
        mostrar=True
    )

    #paginacao
    paginator = Paginator(contatos, 5)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })

def contact_view(request, contato_id):
    contato = get_object_or_404(Contato, id=contato_id)

    if not contato.mostrar:
        raise Http404()

    return render(request, 'contatos/contact_view.html', {
        'contato': contato
    })

def busca(request):
    termo = request.GET.get('termo')

    if termo is None or not termo:
        messages.add_message(
            request,
            messages.ERROR,
            'Campo termo não pode estar vazio.'
        )
        return redirect('index')

    #Concatena os campos de nome e sobrenome para realizar a query
    #Value = simula um valor que não existe na base de dados
    campos = Concat('nome', Value(' '), 'sobrenome')

    contatos = Contato.objects.annotate(
        nome_completo = campos
    ).filter(
        #icontains = contém em alguma parte do valor
        #Q = fazer querys mais complexas
        Q(nome_completo__icontains = termo) | Q(telefone__icontains = termo)
    )

    #paginacao
    paginator = Paginator(contatos, 5)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/busca.html', {
        'contatos': contatos
    })
