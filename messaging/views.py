
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user_model
from .models import Message

User = get_user_model()


@login_required
def inbox(request):
    received_messages = Message.objects.filter(
        receiver=request.user
    ).order_by('-sent_at')

    return render(request, 'messaging/inbox.html', {
        'received_messages': received_messages
    })


@login_required
def send_message(request):
    users = User.objects.exclude(id=request.user.id)

    if request.method == 'POST':
        receiver_id = request.POST.get('receiver')
        subject = request.POST.get('subject')
        body = request.POST.get('body')

        receiver = get_object_or_404(User, id=receiver_id)

        if subject and body:
            Message.objects.create(
                sender=request.user,
                receiver=receiver,
                subject=subject,
                body=body
            )

            messages.success(request, 'Message sent successfully!')
            return redirect('inbox')

        messages.error(request, 'Please complete all fields.')

    return render(request, 'messaging/send_message.html', {
        'users': users
    })


@login_required
def message_detail(request, message_id):
    message = get_object_or_404(
        Message,
        id=message_id,
        receiver=request.user
    )

    message.is_read = True
    message.save()

    return render(request, 'messaging/message_detail.html', {
        'message': message
    })
