# twautoblocker
## Detecta cuentas sospechosas y las elimina del follower list (o las bloquea) 
### Napoleon E. Cornejo
### May 2 2021

Este script busca entre los followers las cuentas que parecen sospechosas según algunos citerios:
- fecha de creacion
- cantidad de followers
- demasiados numeros en el screen name
- que no sea verificada

Criterios que Falta agregar:
- Que no tenga foto de perfil o de background
- Que tenga pocos tweets
- Cuentas a las que sigue

Para poder correrlo, primero es necesario editar los siguientes campos en el archivo **credenciales.json**:
tw_apikey
tw_secretkey
tw_bearertoken
tw_access_token
tw_access_token_secret

Estos valores se obtienen siguiendo las siguientes instrucciones en su cuenta:

Una vez han llenado eso con los valores que les dá twitter, pueden correr el script de la siguiente manera:
```
python twautoblocker.py
```
