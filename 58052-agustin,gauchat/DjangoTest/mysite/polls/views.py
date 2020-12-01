from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

import MySQLdb

def index(request):
    template = loader.get_template('polls/index.html')

    db = MySQLdb.connect(user='root', db='Cine', passwd='Agu-42159187', host='localhost')
    cursor = db.cursor()
    cursor.execute('SELECT nombre FROM consultas_pelicula ORDER BY nombre')
    names = [row[0] for row in cursor.fetchall()]
    db.close()

    context = {
        'nombres': names,
        'prueba': True,
    }
    return HttpResponse(template.render(context, request))