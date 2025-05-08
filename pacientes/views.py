from django.shortcuts import get_object_or_404, render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from .models import Medico,Paciente

# Create your views here.


def home(request):
    if request.method == 'GET':
        return render(request,'home.html')
    
    elif request.method == 'POST':
        nome = request.POST.get('user')
        senha = request.POST.get('password')

        user_autenticado = authenticate(request,username=nome,password=senha)

        if user_autenticado:
            login(request,user_autenticado)
            return redirect('main')

        else:
            return render(request, 'home.html', {'erro': 'Senhas inválidas'})



def register(request):
    print(request.method)
    if request.method == 'GET':
        return render(request,'register.html')
    elif request.method == 'POST':
        nome = request.POST.get('user')
        email = request.POST.get('email')
        senha = request.POST.get('password')
        confirmed_senha = request.POST.get('confirm-password')

        if senha == confirmed_senha:
            novo_medico = User.objects.create_user( username = nome, password = senha, email = email)
            novo_medico.save()
            return redirect('home')

        elif User.objects.filter(username=nome).exists():
            return render(request, 'register.html', {'erro': 'Senhas inválidas'})
        
        else:
            return render(request, 'register.html', {'erro': 'Senhas inválidas'})


def pacientes(request):
    return HttpResponse('Teste')


@login_required(login_url='home')
def agendar(request):
    if request.method == 'GET':
        return render(request, 'agendar.html')
    if request.method == 'POST':
        nome = request.POST.get('nome')
        peso = request.POST.get('peso')
        altura = request.POST.get('altura')
        tipo_sang = request.POST.get('tipo_sangue')
        sintomas = request.POST.get('sintomas')
        data = request.POST.get('datePac')

        novo_paciente = Paciente.objects.create(nome= nome, peso=peso, altura=altura, tipo_sangue= tipo_sang, sintomas=sintomas ,data_agendamento = data,)
        #novo_paciente.save()
        return redirect('agendar')

@login_required(login_url='home')
def mainRed(request):
    return render(request,'main.html')

def deletePaciente(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    paciente.delete()
    return redirect('main') 


@login_required(login_url='home')
def agendamentos(request):

    lista = Paciente.objects.all()
    print(lista)
    return render(request,'agendamentos.html',{'agendamentos':lista}) 

@login_required(login_url='home')
def editPaciente(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)

    if request.method == 'POST':

        paciente.nome = request.POST.get('nome', paciente.nome)
        peso = request.POST.get('peso', paciente.peso)

        if peso is not '':
            paciente.peso = float(peso)

        altura = request.POST.get('altura', paciente.altura)
        if altura is not '':
            paciente.altura = float(altura)


        paciente.tipo_sangue = request.POST.get('tipo_sangue', paciente.tipo_sangue)
        paciente.sintomas = request.POST.get('sintomas', paciente.sintomas)
        paciente.data_agendamento = request.POST.get('datePac', paciente.data_agendamento)
        paciente.save()
        return redirect('agendamentos')  # ou qualquer URL de retorno

    # Se necessário, renderize o formulário com dados
    return render(request, 'editar.html', {'paciente': paciente})
