# twautoblocker
Detecta cuentas sospechosas y las elimina del follower list (o las bloquea) 

*Napoleon E. Cornejo <br>
May 2 2021*

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

Estos datos se obtienen siguiendo las siguientes instrucciones (es necesario esperar unos dias a que twitter apruebe):
https://developer.twitter.com/en/docs/twitter-api/getting-started/getting-access-to-the-twitter-api

Una vez han llenado el **credentials.json** con los valores que les dá twitter, pueden correr el script de la siguiente manera, todo desde la misma carpeta.
En una terminal:
```
python twautoblocker.py
```
