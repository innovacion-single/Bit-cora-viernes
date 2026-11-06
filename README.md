# Bitácora de Avances: versión de solo lectura

Página pública para consultar la bitácora. Se edita en Claude y aquí solo se muestra.

## Archivos

| Archivo | Para qué sirve |
| --- | --- |
| `index.html` | La página que publica Vercel, con los datos ya incluidos |
| `plantilla.html` | El diseño sin datos (no se borra) |
| `datos.json` | Copia de los proyectos y reportes |
| `generar.py` | Junta plantilla + datos y crea `index.html` |

## Publicar en Vercel (una sola vez)

1. Crea un repositorio en GitHub, por ejemplo `bitacora-avances`, y sube estos archivos.
2. En Vercel: **Add New > Project**, elige el repositorio, Framework Preset **Other** y **Deploy**.
3. No necesita variables de entorno ni base de datos.

## Actualizar

Pídele a Claude "actualiza la bitácora en Vercel". Claude genera un `index.html` nuevo con los datos del día:

- Manual: reemplaza `index.html` en GitHub y Vercel lo publica en un minuto.
- Automático: si el repositorio está conectado a la conversación, Claude lo sube directo.

La fecha "Actualizado el…" en la página indica cuándo se generó la copia.

## Privacidad

Cualquiera con la liga puede ver los proyectos. La página pide a los buscadores no indexarla, pero no tiene contraseña.
