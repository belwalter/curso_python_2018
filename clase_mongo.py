
from pymongo import MongoClient


cliente = MongoClient(host='localhost', port=27017)

db = cliente.get_database('curso_python')


print(db.collection_names())
documentos = db.get_collection('mi_coleccion').find({}).sort([('nombre', -1)])
#documentos = db.get_collection('mi_coleccion').find({'lista': {'$exists' : 'true'}})
print(documentos)

for documento in documentos:
    print(documento['nombre'])
    #for elemento in documento['lista']:
        #print(elemento)




db.get_collection('mi_coleccion').update({'nombre':"walter"},{'$set':{'dic':{}}})
db.get_collection('mi_coleccion').update({'nombre':"walter"},{'$push':{'lista':'nuevo valor'}})

doc = db.get_collection('mi_coleccion').find_one({'nombre':'walter'})
print(doc)


#db.get_collection('mi_coleccion').insert({'nombre': "nuevo", 'valor': 150})
