from django.db.models.query import QuerySet
from .models import ReservasLaboratorios, Laboratorios
from .models import Periodos, Blocos
from professores.models import Professores
from django.contrib.auth.models import User, Group

from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, get_object_or_404, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate
from django.contrib import messages
from braces.views import GroupRequiredMixin
from django.views.generic import ListView, UpdateView, DeleteView, CreateView


def verificarReserva(lab,bloco, periodo, data):
    verificar = ReservasLaboratorios.objects.filter(laboratorio=lab).filter(bloco_id=bloco).filter(data_reserva=data).filter(periodo_id=periodo)
    return True if verificar else False

def registrarReserva(lab, bloco, periodo, data, professor):
        reserva = ReservasLaboratorios.objects.create(
            data_reserva = f'{data}',
            professor = Professores.objects.get(nome=professor),
            periodo_id = f'{periodo}',
            laboratorio = Laboratorios.objects.get(id=lab),
            bloco_id = f'{bloco}'
        )
        reserva.save()

class ReservarLabs(GroupRequiredMixin, ListView):
    group_required = u'Funcionarios'
    model = Blocos
    queryset = Blocos.objects.all()
    template_name = 'reserva_labs.html'


def modules(request):
    bloco = request.GET.get('blocos')

    professores = Professores.objects.all()
    laboratorios = Laboratorios.objects.filter(bloco_id=bloco)
    periodos = Periodos.objects.all()

    contexto = {'laboratorios': laboratorios,
                'periodos':periodos,
                 'professores':professores}
    return render(request, 'partials/modules.html', contexto)


def registrarReservarLaboratorio(request):
    blocos = Blocos.objects.all()
    
    if request.method == 'POST':
        bloco = request.POST.get('blocos')
        data = request.POST.get('data')
        periodo = request.POST.get('periodo')
        lab = request.POST.get('nome_lab')
        professor = request.POST.get('nome_professor')

        professor = professor.lower()
        professor = professor.title()

        if bloco == 'Selecione o Bloco':
            mensagem_erro = 'Favor preencher todos os campos'
            return render(request,'reserva_labs.html',{'blocos': blocos,
                                                        'mensagem_erro': mensagem_erro})
        if data == "":
            mensagem_erro = 'Favor preencher todos os campos'
            return render(request,'reserva_labs.html',{'blocos': blocos,
                                                        'mensagem_erro': mensagem_erro})
        if periodo == 'Selecione o Periodo':
            mensagem_erro = 'Favor preencher todos os campos'
            return render(request,'reserva_labs.html',{'blocos': blocos,
                                                        'mensagem_erro': mensagem_erro})
        if lab == 'Selecione o Laboratório':
            mensagem_erro = 'Favor preencher todos os campos'
            return render(request,'reserva_labs.html',{'blocos': blocos,
                                                        'mensagem_erro': mensagem_erro})
        if professor == "":
            mensagem_erro = 'Favor preencher todos os campos'
            return render(request,'reserva_labs.html',{'blocos': blocos,
                                                        'mensagem_erro': mensagem_erro})
    
        
        if not Professores.objects.filter(nome=professor):
            salva_nome_professor = Professores.objects.create(
            nome = f'{professor}')
            salva_nome_professor.save()


        if verificarReserva(lab, bloco, periodo, data):
            nome_lab = Laboratorios.objects.get(id=lab)
            str_periodo = Periodos.objects.get(id=periodo)
            erro = f'{nome_lab.nome} já está reservado no periodo {str_periodo} para data {data} '
            return render(request, 'reserva_labs.html', {'blocos':blocos,
                                                     'erro':erro})
        else:
            registrarReserva(lab, bloco, periodo, data, professor)
            sucesso = 'Reserva registrada com sucesso'
            return render(request, 'consulta.html', {'blocos': blocos,
                                                      'sucesso': sucesso})


# Apagar uma reserva do banco de dados
def cancelar_form(request, id):
    reserva = ReservasLaboratorios.objects.get(id=id)
    return render(request, 'cancelar.html', {'reserva':reserva})

def cancelar_reserva(request,id):
    reserva = ReservasLaboratorios.objects.filter(id=id)
    reserva.delete()
    blocos = Blocos.objects.all()
    return render(request, 'consulta.html', {'blocos':blocos})

# class CancelarForm(GroupRequiredMixin, DeleteView):
#     group_required = u'Funcionarios'
#     model = ReservasLaboratorios
#     context_object_name = 'reserva'
#     template_name = 'cancelar.html'
#     success_url = reverse_lazy('consulta:consulta')


# Editar reserva do banco de dados
def editar_form(request, id):
    usuario = request.user
   # id = pk
    if usuario.groups.filter(name='Funcionarios').exists():
        blocos = Blocos.objects.all()
        reserva = ReservasLaboratorios.objects.get(id=id)
        context =  {'reserva':reserva, 'id': id, 'blocos':blocos}
        return render(request, 'editar_form.html',context)
    else:
        return render(request,'editar_form.html', {'id':id})


def editar_modules(request):
    bloco = request.GET.get('blocos')
    professores = Professores.objects.all()
    laboratorios = Laboratorios.objects.filter(bloco_id=bloco)
    periodos = Periodos.objects.all()

    contexto = {'laboratorios': laboratorios,
                'periodos':periodos,
                 'professores':professores}
    return render(request, 'partials/editar_modules.html', contexto)


def editar(request, id):
    
    if request.method == 'POST':
        professor = request.POST.get('professor')

        data = request.POST.get('data')
        periodo = request.POST.get('periodo')
        lab = request.POST.get('lab')
        bloco = request.POST.get('blocos')

        blocos = Blocos.objects.all()

        if verificarReserva(lab, bloco, periodo, data):
            if verificarReserva(lab, bloco, periodo, data):
                #id = pk
                nome_lab = Laboratorios.objects.get(id=lab)
                str_periodo = Periodos.objects.get(id=periodo)
                erro = f'{nome_lab.nome} já está reservado no periodo {str_periodo} para data {data} '
                return render(request, 'editar_form.html', {'blocos':blocos, 'id':id,
                                                        'erro':erro})
        else:
            if not Professores.objects.filter(nome=professor):
                salva_nome_professor = Professores.objects.create(
                nome = f'{professor}')
                salva_nome_professor.save()

            ReservasLaboratorios.objects.filter(id=id).update(data_reserva=data,
                                                            periodo_id = Periodos.objects.get(id_periodo=periodo),
                                                            laboratorio = Laboratorios.objects.get(id=lab),
                                                            bloco_id = Blocos.objects.get(id_bloco=bloco),
                                                            professor_id = Professores.objects.get(nome=professor)
            )

        sucesso = "Reserva atualizada com sucesso"
        return render(request, 'consulta.html', {'sucesso':sucesso, 'blocos': blocos})
        