from django.forms import ModelForm
from .models import Registro_de_anime

class Registro_de_animeForm(ModelForm):
    class Meta:
        model = Registro_de_anime
        fields = '__all__'