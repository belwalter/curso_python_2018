
from pymongo import MongoClient
import museo
import pintura

def conexion():
    cliente = MongoClient(host='localhost', port=27017)
    db = cliente.get_database('curso_python')
    return db

def guardar_museo(museo):
    db = conexion()
    db.get_collection('museos').insert({'nombre': museo.nombre,
            'direccion': museo.direccion, 'muestras': museo.muestras})

def guardar_pintura(museo, pintura):
    db = conexion()
    db.get_collection('museos').find({'nombre': museo.nombre})
    db.get_collection('museos').update({'nombre':museo.nombre},{'$push':
        {'muestras': {'artista': pintura.artista, 'anio': pintura.anio, 'titulo': pintura.titulo,
        'descripcion': pintura.descripcion, 'tipo': pintura.tipo, 'material': pintura.material,
        'estilo': pintura.estilo, 'tipo_muestra': 'Pintura'}}})

def lista_muestras(museo):
    db = conexion()
    documento = db.get_collection('museos').find_one({'nombre': museo.nombre})
    for muestra in documento['muestras']:
        if(muestra['tipo_muestra'] == 'Pintura'):
            m = pintura.Pintura()
            m.artista = muestra['artista']
            m.anio = muestra['anio']
            m.museo = museo
            # falta completar
            museo.muestras.append(m)


def lista_museos():
    db = conexion()
    documentos = db.get_collection('museos').find({})
    lista_museos = []
    for elemento in documentos:
        m = museo.Museo(elemento['nombre'], elemento['direccion'], elemento['tipo'])
        lista_muestras(m)
        lista_museos.append(m)
    return lista_museos
