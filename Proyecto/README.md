# Gestor de Hojas de Vida (CVs)

Este proyecto en Python permite registrar, consultar, actualizar y exportar hojas de vida de candidatos. Incluye validaciones de entrada, generación de reportes y exportación a múltiples formatos.

## Estructura del Proyecto

```
proyecto_cv/
├── main.py
├── hojasdevida.py
├── reportes.py
├── utils/
│   ├── validators.py
│   ├── file_utils.py
│   ├── display.py
├── services/
│   └── report_service.py
├── data/
│   ├── cvs.json
│   ├── exportado.csv
│   └── exportado.txt
├── README.md
```

## Requisitos

- Python 3.8+
- Paquetes utilizados:
  - `tabulate` (para visualización en tablas)
  - `collections` (para contar habilidades)
  - `os`, `json`, `csv`, `re`, `datetime` (módulos estándar)

Instala `tabulate` si no lo tienes:

```bash
pip install tabulate
```

## Archivos Principales

### main.py

- Punto de entrada de la aplicación.
- Muestra el menú principal para interactuar con el sistema.

### hojasdevida.py

- Contiene la función `registrar_cv()` para capturar datos del usuario.
- Genera un diccionario estructurado de CV.

### reportes.py

- Contiene el menú de reportes.
- Permite ver habilidades más comunes, exportar datos a CSV, TXT o JSON.

## Módulos Utilitarios (utils/)

### validators.py

- Valida correos, fechas, números de documento y teléfono.

### file_utils.py

- Carga y guarda CVs en archivos JSON.
- Convierte habilidades (set/list) para que sean compatibles con JSON.

### display.py

- Muestra los CVs en formato de tabla usando `tabulate`.

## Servicios (services/)

### report_service.py

- Contiene la lógica para generar reportes como habilidades más comunes.

## Funciones Clave

- Registrar CV
- Actualizar datos personales, formación, experiencia o habilidades
- Ver CVs registrados
- Generar reportes de habilidades comunes
- Exportar datos en diferentes formatos (JSON, CSV, TXT)

## Ejecutar el Programa

Desde la terminal:

```bash
python main.py
```

## Ejemplo de ID de CV

Cada CV se identifica por una combinación única de documento + fecha de nacimiento:

```
12345678_1990-05-23
```

## Exportaciones

- JSON: `data/cvs.json`
- CSV: `data/exportado.csv`
- TXT: `data/exportado.txt`

## Notas Finales

- El sistema guarda automáticamente los datos en archivos locales.
- Se pueden añadir más funcionalidades como eliminación de CVs o búsqueda por filtros.
