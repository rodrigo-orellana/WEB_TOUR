import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'composeexample.settings')

import django

django.setup()
#import sys
#sys.path.append('visitas_granada')
from visitas_granada.models import Visita, Comentario
#from models import Visita, Comentario

if __name__ == "__main__":
    v = Visita(nombre="plaza1", descripción="Texto plaza1")
    v.save()

    # ...

    print(Visita.objects.all())
