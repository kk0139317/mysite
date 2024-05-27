# myapp/management/commands/start_gradio.py
from django.core.management.base import BaseCommand
from home.gradio_interface import start_gradio

class Command(BaseCommand):
    help = 'Start Gradio interface'

    def handle(self, *args, **kwargs):
        start_gradio()
