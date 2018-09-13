
from firebase import firebase

firebase = firebase.FirebaseApplication('https://python-b0b51.firebaseio.com/', None)

#dioses = ['Zeus', 'Hera', 'Poseidon','Demeter', 'Hades', 'Hestia', 'Ares']



#agregar con key
'''
for elemento in heroes:
    firebase.post('/heroes', elemento)
'''
elemento = {'prueba': 'ejemplo'}
#firebase.post('/dioses2', elemento)
#agregar sin key etiqueta
'''
for elemento in heroes:
    firebase.put('/heroes/', 'heroes2', elemento)
'''
firebase.put('/dioses2', 'nuevo', elemento)
#obtener uno
'''
respuesta = firebase.get('heroes/-LCfG8n4AlCS41-yjY5A', None)
print(respuesta)
'''

#eliminar uno
#firebase.delete('/dioses2/-LCcqjhZG8Q_q8aXW_Wl', None)

#eliminar todos
#firebase.delete('/dioses', None)

dic = {'otro': 'nuevo campo'}

#firebase.put('/dioses2', '-LCcqibnN8cpP8HHIbPz', dic)
#firebase.patch('/dioses2/-LCcqibnN8cpP8HHIbPz', dic)


#listar
'''
result = firebase.get('dioses2', None)
for i in result:
    print (firebase.get('/dioses2/'+i, None))
'''
