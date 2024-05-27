# Python Upgrades

Estimar el tiempo y esfuerzo requerido para actualizar de una version de Python 3.X.Y a una versión más actual depende mucho del sistema al que se le este aplicando. Y de los cambios en los features de la vesion 3.X.Y a la nueva versión. 

- **Proyectos Pequeños**: Para proyectos pequeños, la actualización podría tomar desde unos pocos días hasta unas pocas semanas, mientras que para
- **Proyectos Medianos**: Los proyectos medianos pueden tomar desde unas pocas semanas, especialmente si requieren pruebas y refactorización extensas.
- **Proyectos Grandes**: Los proyectos grandes con muchas dependencias y lógica compleja pueden tomar desde varias semanas hasta unos pocos meses(inclusive un poco más).

Estimar el tiempo y esfuerzo necesario para actualizar Python de una version 3.X1.Y1 a 3.X2.Y2 implica varias fases y consideraciones. 

Primero debemos empezar por la fase de evaluación

## 1. Fase de Evaluación

#### Inventario
- **Identificar Dependencias**: Lista todas las bibliotecas y dependencias de terceros que utiliza tu proyecto. Verifica su compatibilidad con Python 3.12.
- **Análisis del Código**: Determina el tamaño y la complejidad de tu base de código. Los proyectos más grandes y complejos requerirán más tiempo.

#### Verificación de Compatibilidad
- **Revisar Compatibilidad**: Utiliza herramientas como `pip` para verificar problemas de compatibilidad. Por ejemplo:
  ```sh
  pip list --outdated
  ```
  Esto ayuda a identificar qué paquetes necesitan actualizaciones.
  Otras Herramientas disponibles son:

    - 1. **caniusepython3**: Esta herramienta te ayuda a identificar si las dependencias de tu proyecto son compatibles con una versión más reciente de Python.
        ```sh
        pip install caniusepython3
        caniusepython3 -r requirements.txt
        ```
        - **Más información**: [caniusepython3](https://github.com/brettcannon/caniusepython3)
        - example
        ```sh
            caniusepython3 -r requirements.txt
            Finding and checking dependencies ...

            You need 2 projects to transition to Python 3.
            Of those 2 projects, 2 have no direct dependencies blocking their transition:

            jellyfish
            python-markdown-math
        ```
    - 2. **tox**: Tox es una herramienta para automatizar las pruebas en diferentes entornos de Python. Puede ser muy útil para probar tu código en múltiples versiones de Python.
        - Configura un archivo `tox.ini` en tu proyecto:
            ```ini
            [tox]
            envlist = py38, py312

            [testenv]
            deps = pytest
            commands = pytest
            ```
        - Ejecuta tox:
            ```sh
            tox
            ```
        - **Más información**: [tox](https://tox.readthedocs.io/en/latest/)
    - 3. **pyupgrade**: Pyupgrade es una herramienta que actualiza automáticamente tu código para usar la sintaxis más reciente de Python. Esto puede ayudarte a migrar tu código a Python 3.12.
        ```sh
        pip install pyupgrade
        pyupgrade --py3-plus **/*.py
        ```
        - **Más información**: [pyupgrade](https://github.com/asottile/pyupgrade)
    - 4. **pip-check-reqs**: Esta herramienta comprueba si todas las dependencias que se encuentran en tu archivo `requirements.txt` se están utilizando en tu proyecto y si hay dependencias no declaradas.
        ```sh
        pip install pip-check-reqs
        pip-missing-reqs
        ```
        - **Más información**: [pip-check-reqs](https://github.com/r1chardj0n3s/pip-check-reqs)
    - 5. **bandit**: Bandit es una herramienta para analizar la seguridad del código Python. Puede ayudarte a identificar problemas de seguridad que podrían surgir al actualizar a una nueva versión de Python.
        ```sh
        pip install bandit
        bandit -r path/to/your/code
        ```
        - **Más información**: [bandit](https://bandit.readthedocs.io/en/latest/)
    - 6. **mypy**: Mypy es un verificador de tipos estáticos para Python. Puede ayudarte a asegurar que tu código sea compatible con las nuevas versiones verificando la corrección de tipos.
        ```sh
        pip install mypy
        mypy path/to/your/code
        ```
        - **Más información**: [mypy](http://mypy-lang.org/)
    - 7. **pytest y coverage.py**: Pytest es un framework de pruebas que, junto con coverage.py, puede ayudarte a asegurar que tu código esté bien probado y que todas las partes relevantes estén cubiertas.
        ```sh
        pip install pytest coverage
        pytest --cov=path/to/your/code
        ```
        - **Más información**: [pytest](https://docs.pytest.org/en/latest/) y [coverage.py](https://coverage.readthedocs.io/)




### 2. Fase de Preparación

#### Configuración del Entorno
- **Crear un Entorno de Pruebas**: Crea un nuevo entorno con Python 3.12. Puedes usar entornos virtuales o Docker para aislar esta configuración.
  ```sh
  python3.12 -m venv mi_entorno
  source mi_entorno/bin/activate
  ```

#### Actualización de Dependencias
- **Actualizar Dependencias**: Actualiza las bibliotecas de terceros a sus versiones más recientes que soporten Python 3.12.
  ```sh
  pip install --upgrade nombre_paquete
  ```

### 3. Fase de Pruebas

#### Pruebas Automatizadas
- **Ejecutar Pruebas Unitarias**: Asegúrate de que todas las pruebas unitarias existentes pasen con Python 3.12. Utiliza frameworks de pruebas como `pytest`.
  ```sh
  pytest
  ```

#### Pruebas Manuales
- **Pruebas Manuales de QA**: Realiza pruebas manuales en rutas críticas de tu aplicación para detectar problemas que las pruebas automatizadas podrían no captar.

#### Pruebas de Rendimiento
- **Pruebas de Benchmark**: Ejecuta benchmarks de rendimiento para comparar Python 3.8 y Python 3.12. Esto ayuda a identificar cualquier regresión en el rendimiento.

### 4. Fase de Refactorización

#### Cambios en el Código
- **Abordar Deprecaciones y Errores**: Actualiza el código para manejar deprecaciones y errores que puedan surgir debido a los cambios en Python 3.12.
- **Utilizar Nuevas Funcionalidades**: Opcionalmente, refactoriza el código para aprovechar las nuevas características y optimizaciones introducidas en Python 3.12.

### 5. Fase de Despliegue

#### Entorno de Staging
- **Desplegar en Staging**: Despliega la aplicación actualizada en un entorno de staging para una validación adicional.

#### Monitorización
- **Monitorizar Métricas**: Supervisa de cerca el rendimiento de la aplicación y los registros de errores después de desplegar la actualización para garantizar la estabilidad.

### 6. Fase de Implementación

#### Despliegue Gradual
- **Despliegue Gradual**: Realiza el despliegue de la actualización de manera gradual para reducir riesgos. Usa despliegues canarios o fases.
  
#### Ciclo de Retroalimentación
- **Recoger Retroalimentación**: Recolecta feedback de usuarios y desarrolladores para identificar cualquier problema que pueda haber sido pasado por alto.

### Métricas de Estimación

#### Estimación de Tiempo
- **Proyectos Pequeños**
- **Proyectos Medianos**
- **Proyectos Grandes**

#### Estimación de Trabajo
- **Actualización de Dependencias**: Esto podría variar desde unas pocas horas hasta unos días, dependiendo del número de dependencias.
- **Pruebas**: Las pruebas automatizadas y manuales podrían tomar desde varios días hasta semanas.
- **Refactorización**: El tiempo requerido aquí depende de la extensión de los cambios necesarios en el código. Podría variar desde unos pocos días hasta unas semanas.
- **Despliegue y Implementación**: Esta fase podría tomar desde unos pocos días hasta una semana, dependiendo de la estrategia de despliegue.

### Herramientas y Recursos
- **Pipelines de CI/CD**: Utiliza pipelines de Integración Continua/Despliegue Continuo para automatizar los procesos de pruebas y despliegue.
- **Herramientas de Verificación de Compatibilidad**: Herramientas como `caniusepython3` pueden ayudar a identificar problemas de compatibilidad con bibliotecas de terceros.
- **Documentación**: Consulta la [documentación oficial de Python](https://docs.python.org/3.12/whatsnew/3.12.html) para información detallada sobre los cambios y nuevas funcionalidades en Python 3.12.

 

No, `python-future` no es la herramienta adecuada para migrar código de Python 3.8 a Python 3.12. `python-future` está diseñado principalmente para facilitar la compatibilidad entre Python 2 y Python 3, permitiendo escribir código que funcione tanto en versiones antiguas como modernas de Python.

Para migrar de una versión de Python 3 a otra más reciente, como de Python 3.8 a 3.12, lo mejor es seguir las siguientes prácticas y utilizar herramientas específicas para este propósito:

### 1. **Revisar la Documentación de Cambios**
- **What’s New in Python**: Consulta la documentación oficial para cada versión de Python entre la versión actual y la nueva para entender los cambios y mejoras.
  - [What’s New in Python 3.12](https://docs.python.org/3.12/whatsnew/3.12.html)
  - [What’s New in Python 3.11](https://docs.python.org/3.11/whatsnew/3.11.html)
  - [What’s New in Python 3.10](https://docs.python.org/3.10/whatsnew/3.10.html)
  - [What’s New in Python 3.9](https://docs.python.org/3.9/whatsnew/3.9.html)
  

### 2. **Usar Herramientas de Análisis y Actualización**
- **caniusepython3**: Para verificar si todas las dependencias son compatibles con Python 3.12.
  ```sh
  pip install caniusepython3
  caniusepython3 -r requirements.txt
  ```
- **tox**: Para probar el código en múltiples versiones de Python y asegurar que todas las pruebas pasan.
  ```ini
  [tox]
  envlist = py38, py312

  [testenv]
  deps = pytest
  commands = pytest
  ```
  ```sh
  tox
  ```

### 3. **Actualizar Dependencias**
- **pip list --outdated**: Lista las dependencias que tienen actualizaciones disponibles.
  ```sh
  pip list --outdated
  pip install --upgrade nombre_paquete
  ```

### 4. **Utilizar pyupgrade**
- **pyupgrade**: Actualiza automáticamente el código a la sintaxis más moderna de Python.
  ```sh
  pip install pyupgrade
  pyupgrade --py3-plus **/*.py
  ```

### 5. **Ejecutar Pruebas y Verificación de Tipos**
- **pytest**: Ejecuta pruebas unitarias y de integración para asegurar que el código sigue funcionando correctamente.
  ```sh
  pytest
  ```
- **mypy**: Verifica la corrección de tipos para asegurar la compatibilidad y la detección de errores potenciales.
  ```sh
  pip install mypy
  mypy path/to/your/code
  ```

### 6. **Resolver Deprecaciones y Mejorar el Código**
- Revisa las advertencias de deprecación y ajusta el código según sea necesario para eliminar dependencias de características obsoletas.
- Aprovecha las nuevas características y optimizaciones introducidas en las versiones más recientes de Python para mejorar el rendimiento y la legibilidad del código.

### 7. **Documentar y Desplegar**
- Actualiza la documentación del proyecto para reflejar los cambios realizados durante la migración.
- Despliega el código actualizado en un entorno de staging antes de pasar a producción para asegurar que todo funciona correctamente.

### Recursos Adicionales
- [Python Enhancement Proposals (PEPs)](https://www.python.org/dev/peps/): Para entender los cambios detallados y las nuevas características de cada versión.
- [Real Python: Python 3.x Migration Guide](https://realpython.com/python3-migration-guide/): Guía detallada sobre la migración de Python 2 a 3, pero con principios aplicables a migraciones dentro de Python 3.

Estas prácticas y herramientas te ayudarán a realizar una migración eficiente y segura de Python 3.8 a Python 3.12.

