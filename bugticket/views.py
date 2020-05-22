from django.shortcuts import render, reverse, HttpResponseRedirect
from bugticket.forms import SignUpForm, LoginForm
from django.contrib.auth import login, logout, authenticate
from bugticket.models import CustomUser, Ticket
from django.contrib.auth.decorators import login_required
from bugticket.forms import TicketForm

@login_required
def homeView(request):
    html = 'index.html'
    ticket_data = Ticket.objects.all()
    return render(request, html, {'ticket_data': ticket_data})

@login_required
def signUpView(request):
    html = 'signup.html'
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = CustomUser.objects.create_user(
                username=data['username'],
                display_name=data['display_name'],
                password=data['password1'],
                )
            new_user.save()
            login(request, new_user)
            return HttpResponseRedirect(reverse('home'))
    form = SignUpForm()
    return render(request, html, {'form': form})

def loginview(request):
    html = 'login.html'
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user= authenticate(request, username = data['username'], password= data['password'])
            if user:
                login(request, user)
                
            return HttpResponseRedirect(
                    request.GET.get('next', reverse('home'))
                )
    form = LoginForm()
    return render(request,'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

@login_required
def create_ticket(request, user_id):
    html = "createticketform.html"
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user =  CustomUser.objects.get(id=user_id)
            ticket = Ticket.objects.create(
                title=data['title'],
                description=data['description'],
                filed_user=user
            )
            return HttpResponseRedirect(reverse('home'))
    form = TicketForm()
    return render(request,html , {"form": form})

@login_required
def ticket_detail(request, id):
    html = 'ticket_detail.html'
    ticket = Ticket.objects.get(id=id)
    return render(request, html, {'ticket': ticket})

@login_required
def inprogress_ticket(request, ticket_id):
    #Peter Marsh assisted with fixing view
    ticket = Ticket.objects.get(id=ticket_id)
    ticket.ticket_status = "IN PROGRESS"
    ticket.assigned_user = request.user
    ticket.completed_user = None
    ticket.save()
    return HttpResponseRedirect(reverse('ticket_detail', args=(ticket_id,)))

@login_required
def complete_ticket(request, ticket_id):
    ticket= Ticket.objects.get(id=ticket_id)
    ticket.ticket_status = "DONE"
    ticket.completed_user = request.user
    ticket.assigned_user = None
    ticket.save()
    return HttpResponseRedirect(reverse('ticket_detail', args=(ticket_id,)))

@login_required
def invalid_ticket(request, ticket_id):
    ticket= Ticket.objects.get(id=ticket_id)
    ticket.ticket_status = "INVALID"
    ticket.assigned_user = None
    ticket.completed_user = None
    ticket.save()
    return HttpResponseRedirect(reverse('ticket_detail', args=(ticket_id,)))

@login_required
def edit_ticket(request, ticket_id):
    #followed demo by Instructor Joe
    ticket = Ticket.objects.get(id=ticket_id)
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            ticket.title = data['title']
            ticket.description = data['description']
            ticket.save()
        return HttpResponseRedirect(reverse('ticket_detail', args=(ticket_id,)))
    form = TicketForm(initial={
        'title':ticket.title,
        'description': ticket.description
    })
    return render(request, 'createticketform.html', {'form': form})

@login_required
def user_detail(request, user_id):
    filed_ticket = Ticket.objects.filter(filed_user=user_id)
    assigned_ticket = Ticket.objects.filter(assigned_user=user_id)
    completed_ticket = Ticket.objects.filter(completed_user=user_id)
    return render(request, 'user_detail.html', {'filed_ticket':filed_ticket, 'assigned_ticket':assigned_ticket, 'completed_ticket':completed_ticket})

