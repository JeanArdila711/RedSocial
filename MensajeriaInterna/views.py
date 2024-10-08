from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Message

def inbox(request):
    messages_received = Message.objects.filter(receiver=request.user).order_by('-timestamp')
    return render(request, 'chat/inbox.html', {'messages': messages_received})

def send_message(request):
    if request.method == 'POST':
        receiver_username = request.POST.get('receiver')
        message_content = request.POST.get('message')

        try:
            receiver = User.objects.get(username=receiver_username)
            Message.objects.create(sender=request.user, receiver=receiver, content=message_content)
            return redirect('inbox')
        except User.DoesNotExist:
            # Aquí podrías manejar el caso en el que el usuario no exista
            return redirect('send_message')

    return render(request, 'chat/send_message.html')
