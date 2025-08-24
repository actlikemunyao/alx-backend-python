import pytest
from django.contrib.auth import get_user_model
from chat.models import Conversation, Message

@pytest.mark.django_db
def test_create_conversation_and_message():
    User = get_user_model()
    user = User.objects.create_user(username='alice', password='pwd12345')
    conv = Conversation.objects.create(title='General')
    msg = Message.objects.create(conversation=conv, sender=user, content='Hello')
    assert msg.pk is not None
    assert conv.messages.count() == 1
