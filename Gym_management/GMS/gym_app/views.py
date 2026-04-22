from django.shortcuts import render, redirect
from .models import Member, Trainer

def dashboard(request):
    members = Member.objects.count()
    trainers = Trainer.objects.count()
    return render(request, 'gym_app/dashboard.html', {'members': members, 'trainers': trainers})


def add_member(request):
    trainers = Trainer.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        phone=request.POST['phone'],
        email=request.POST['email'],
        join_date=request.POST['join_date'],
        membership_plan=request.POST['membership_plan'],
        fees_paid='fees_paid' in request.POST
        trainer_id = request.POST['trainer']

        trainer = Trainer.objects.get(id=trainer_id)

        Member.objects.create(
            name=name,
            age=age,
            phone=phone,
            email=email,
            join_date=join_date,
            membership_plan=membership_plan,
            fees_paid=fees_paid,
            trainer=trainer
        )
        return redirect('gym_app/member_list')

    return render(request, 'gym_app/add_member.html', {'trainers': trainers})


def member_list(request):
    members = Member.objects.all()
    return render(request, 'gym_app/member_list.html', {'members': members})


def add_trainer(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        Trainer.objects.create(name=name, phone=phone)
        return redirect('gym_app/dashboard')

    return render(request, 'gym_app/add_trainer.html')