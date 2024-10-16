from django.shortcuts import render, redirect
from .models import Message
from .forms import MessageForm, MessageForm2
from users.models import User, Aspirante


def inbox(request):
    print(f"Current User: {request.user.email}, Tipo Usuario: {request.user.tipo_usuario}")  # Debugging line

    if request.user.tipo_usuario == 'Aspirante':
        base_template = 'base_aspirante.html'
    else:
        base_template = 'base_reclutador.html'

    messages_received = Message.objects.filter(receiver=request.user).order_by('-timestamp')
    return render(request, 'inbox.html', {'messages': messages_received, 'base_template': base_template})



def send_message(request, user_reciever_id=None):
    if request.user.tipo_usuario == 'Aspirante':
        base_template = 'base_aspirante.html'
    else:
        base_template = 'base_reclutador.html'

    # Fetch the user_reciever object using the ID passed
    if user_reciever_id:
        user_reciever = User.objects.get(id=user_reciever_id)  # Assuming 'Usuario' is your model name

        if request.method == 'POST':
            form = MessageForm2(request.POST)
            if form.is_valid():
                message = form.save(commit=False)
                message.sender = request.user
                message.receiver = user_reciever
                message.save()
                return redirect('inbox')
        else:
            form = MessageForm2()

        return render(request, 'send_message.html', {
            'form': form,
            'user_reciever': user_reciever,
            'base_template': base_template
        })


    else:
        if request.method == 'POST':
            form = MessageForm(request.POST)
            if form.is_valid():
                message = form.save(commit=False)
                message.sender = request.user
                message.save()
                return redirect('inbox')
        else:
            form = MessageForm()

        return render(request, 'send_message.html', {
            'form': form,
            'user_reciever': None,  # No user_reciever in this case
            'base_template': base_template
        })