from django.forms import ModelForm

from . import models

class TicketForm(ModelForm):
    class Meta:
        model = models.Ticket
        fields = ["title", "description", "image"]


class ReviewForm(ModelForm):
    pass