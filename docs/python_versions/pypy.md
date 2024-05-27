# Pypy

Puedes utilizar PyPy dentro de un ambiente virtual (virtual environment) creado con `venv`. Aquí te explico cómo hacerlo:

### Instalación de PyPy

Primero, asegúrate de tener PyPy instalado en tu sistema. Puedes instalarlo utilizando `snap` en Ubuntu:

```sh
sudo snap install pypy --classic
```

tendras una salida como la siguiente:

```bash
sudo snap install pypy --classic
pypy 7.3.16 from The PyPy Project (pypyproject) installed
```

para instalar python 3 su correspondiente es

```sh
sudo snap install pypy3 --classic
```

tendras una salida como la siguiente:

```bash
sudo snap install pypy3 --classic
pypy3 7.3.16 from The PyPy Project (pypyproject) installed
```
dentro del folder de snap encontraremos los binarios:
```bash
ls /snap/pypy/current/bin/
libpypy-c.so  libpypy-c.so.debug  pypy  pypy.debug  pypy2  pypy2.7  python  python2  python2.7
```

```bash
 ls /snap/pypy3/current/bin/
libpypy3.9-c.so  libpypy3.9-c.so.debug  pypy  pypy3  pypy3.9  pypy3.9.debug  python  python3  python3.9
```

### Como crear un Ambiente Virtual con PyPy

Para crear un ambiente virtual utilizando PyPy, sigue estos pasos:

1. **Instalar virtualenv**: Aunque `venv` funciona bien con CPython, `virtualenv` es más flexible y puede utilizarse fácilmente con diferentes intérpretes de Python, incluyendo PyPy.

    ```sh
    pip install virtualenv
    ```

2. **Crear el Ambiente Virtual**: Utiliza `virtualenv` especificando PyPy como el intérprete de Python.

   ```sh
   virtualenv -p /usr/bin/pypy3 myenv
   ```

   Asegúrate de ajustar la ruta a PyPy (`/usr/bin/pypy3`) si es diferente en tu sistema. Este comando creará un directorio llamado `myenv` que contiene el nuevo ambiente virtual.

   En mi caso tuve que correr:
   ```sh
    /home/pepe/.local/bin/virtualenv -p /snap/bin/pypy3 myenv
    created virtual environment PyPy3.9.19.final.0-64 in 1637ms
    creator PyPy3Posix(dest=/home/pepe/CURSOS/course_python/myenv, clear=False, no_vcs_ignore=False, global=False)
    seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/home/pepe/.local/share/virtualenv)
        added seed packages: pip==24.0, setuptools==69.5.1, wheel==0.43.0
    activators BashActivator,CShellActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator
   ```

### Activar el Ambiente Virtual

Para activar el ambiente virtual, usa el siguiente comando:

- En Linux/MacOS:
  ```sh
  source myenv/bin/activate
  ```

- En Windows:
  ```sh
  myenv\Scripts\activate
  ```

Una vez activado, el prompt de tu terminal debería cambiar para indicar que estás dentro del ambiente virtual.

### Verificar la Instalación

Para verificar que el ambiente virtual está utilizando PyPy, puedes ejecutar:

```sh
python --version
```

Esto debería mostrar algo similar a:

```
Python 3.9.13 (7.3.11+dfsg-1, Oct 14 2023, 19:30:22)
[PyPy 7.3.11 with GCC 10.2.1 20210110]
```

```bash
python --version
Python 3.9.19 (a2113ea87262, Apr 21 2024, 05:40:24)
[PyPy 7.3.16 with GCC 10.2.1 20210130 (Red Hat 10.2.1-11)]
```

### Instalación de Paquetes

Puedes instalar paquetes dentro de este ambiente virtual de la misma manera que lo harías en cualquier ambiente virtual de Python, utilizando `pip`:

```sh
pip install nombre-del-paquete
```

### Desactivar el Ambiente Virtual

Cuando termines de trabajar en tu proyecto, puedes desactivar el ambiente virtual con:

```sh
deactivate
```

