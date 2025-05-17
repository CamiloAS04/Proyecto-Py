# Sistema de Gestión de Hojas de Vida

## Integrantes y Grupo
- **Nombre:** [Tu Nombre Aquí]  
- **Grupo:** [Nombre del grupo o número de equipo]

## Descripción General

Este sistema permite registrar, consultar, actualizar y generar reportes sobre hojas de vida de candidatos. Cada hoja de vida incluye datos personales, formación académica, experiencia laboral, referencias y habilidades.  
El sistema almacena la información en formato JSON y ofrece funcionalidades para exportar los datos en formatos JSON, CSV y TXT.

### Funcionalidades principales:
- Registro de hojas de vida
- Consulta por nombre, documento o correo
- Actualización de datos personales, experiencia, formación o habilidades
- Reportes de experiencia laboral, certificaciones específicas y habilidades comunes
- Exportación de datos en múltiples formatos

## Instrucciones para Ejecutar el Programa

1. Clona o descarga este repositorio.
2. Asegúrate de tener Python 3 instalado.
3. Instala las dependencias necesarias (ver siguiente sección).
4. Ejecuta el archivo principal:

```bash
python main.py
```

## Librerías Utilizadas

El sistema utiliza las siguientes librerías:

- `json` (estándar de Python)
- `csv` (estándar de Python)
- `collections` (estándar de Python)
- `rich` - Para una interfaz en consola más amigable
- `tabulate` - Para mostrar tablas de manera visual

### Instalación de librerías externas:

```bash
pip install rich tabulate
```

## Ejemplos de Uso

### Registro de una hoja de vida:
El sistema te guiará paso a paso para ingresar los datos:
- Nombre: Juan Pérez
- Documento: 123456789
- Correo: juan.perez@email.com
- Formación: Universidad Nacional, Ingeniería de Sistemas, 2015-2020
- Experiencia: Empresa ABC, Desarrollador, Desarrollo de software, 2020-2023
- Habilidades: Python, SQL, Certificación SCRUM

### Consulta:
Puedes buscar por:
- Nombre: `Juan Pérez`
- Documento: `123456789`
- Correo: `juan.perez@email.com`

### Reportes:
- Ver candidatos con más de 2 años de experiencia.
- Listar quienes tienen la habilidad "Python".
- Mostrar habilidades más frecuentes.

### Exportación:
Se puede exportar a:
- `exportado.json`
- `exportado.csv`
- `exportado.txt`

## Captura del Tablero de Trabajo

*(Agrega aquí una captura de pantalla del programa en ejecución o del tablero visual si usaste uno como Trello, Notion, etc.)*

![Captura de Ejemplo](captura.png)
