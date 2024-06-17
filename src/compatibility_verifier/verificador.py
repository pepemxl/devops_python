import importlib
import pkg_resources

def verificar_compatibilidad(requirements_file):
    with open(requirements_file, 'r') as f:
        lines = f.readlines()
    
    for line in lines:
        paquete, version = line.strip().split('==')
        try:
            modulo = importlib.import_module(paquete)
            instalada = pkg_resources.get_distribution(paquete).version
            if instalada == version:
                print(f"{paquete} {version} - Compatible")
            else:
                print(f"{paquete} - Incompatible. Instalado: {instalada}, Esperado: {version}")
        except ImportError:
            print(f"{paquete} no está instalado.")
        except Exception as e:
            print(f"Error al verificar {paquete}: {e}")

if __name__ == "__main__":
    verificar_compatibilidad('requirements.txt')
