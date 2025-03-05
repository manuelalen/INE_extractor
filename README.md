
# INE_extractor

Repositorio para la automatización de extracción de datos desde la API del Instituto Nacional de Estadística (INE), procesado con Python y almacenamiento en una base de datos MySQL.

Este proyecto está pensado para integrarse en flujos de trabajo de análisis de datos (**Data Analytics**), facilitando la actualización periódica de información oficial.

---

## 📊 Esquema del flujo

![Esquema del proceso](images/schema.png)

---

## 🚀 ¿Qué hace este proyecto?

1️⃣ Conecta a la **API del INE** y descarga datos en formato JSON.

2️⃣ Procesa los datos, limpiando y estructurando la información (dividiendo los nombres por partes relevantes).

3️⃣ Carga los datos en una base de datos **MySQL**, creando automáticamente la tabla `ine_agregados_economicos`.

---

## ⚙️ ¿Qué datos descarga?
Actualmente extrae información desde la tabla del INE:

🔗 [`[https://servicios.ine.es/wstempus/jsCache/ES/DATOS_TABLA/69069]`]([https://servicios.ine.es/wstempus/jsCache/ES/DATOS_TABLA/69069])

Estos datos corresponden a **gasto medio por persona y hogar**.

---

## 🛠️ Requisitos
Antes de ejecutar el proyecto, asegúrate de tener instalado:

- Python 3.12 o superior
- MySQL
- pip

Además, instala las dependencias necesarias ejecutando:

```bash
pip install -r requirements.txt
```

---

## 🔐 Configuración
Crea un archivo `.env` en la raíz del proyecto con tus credenciales de acceso a MySQL:

```
MYSQL_USER=tu_usuario
MYSQL_PASSWORD=tu_contraseña
MYSQL_HOST=localhost
MYSQL_DB=dev_testeos
```

---

## 🧠 ¿Cómo funciona el código?

- **Carga el `.env`** para usar las credenciales de manera segura.
- **Conecta a MySQL** utilizando SQLAlchemy.
- **Solicita los datos al INE** mediante `requests`.
- **Procesa los datos** dividiendo los nombres de las series para organizarlos en campos como:
  - `indice`
  - `dato`
  - `tipo_dato`
  - `descripcion`
- **Inserta el resultado** en MySQL usando Pandas (`to_sql`).
- Informa cuando termina con éxito:  
  `🤙 Datos insertados correctamente en la tabla 'ine_agregados_economicos'`

---

## 🗂️ Estructura esperada de la tabla

| indice           | dato              | tipo_dato | descripcion         | anyo | valor     | secreto |
|------------------|-------------------|-----------|---------------------|------|-----------|---------|
| Total Nacional   | Indice general    | Base      | G medio hogar       | 2023 | 2810335.0 | False   |


---

## ✅ Ejecución
Para lanzar el script solo necesitas ejecutar:

```bash
python INE_extractor_v4.py
```

---

## 📌 Notas finales
- El proyecto está preparado para adaptarse fácilmente a otras tablas del INE, cambiando únicamente la URL.
- Si la estructura del `"Nombre"` varía, revisa el procesamiento con `.split('.')`.
- Recuerda actualizar tu `.env` si cambias de entorno.

---

## ✨ Mejoras futuras
- Añadir validación si la tabla ya existe y actualizar solo nuevos registros.
- Soporte para más tablas del INE de manera dinámica.
- Implementación de logs del proceso.
