from tinydb import TinyDB, Query
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def registrarVenta(request):
    db = TinyDB('db.json')
    if(request.method=='POST'):
        datos = json.loads(request.body)
        db.insert(datos)
    return HttpResponse('Funciono')
def darFactura(request,idFactura):
    db = TinyDB('db.json')
    Q =Query()
    return HttpResponse(db.search(Q.idFactura==idFactura))
def anularFactura(request,idFactura):
    db = TinyDB('db.json')
    Q =Query()
    db.remove(Q.idFactura==idFactura)
    return HttpResponse("Funciono")
