from ncclient import manager
import xml.dom.minidom

# Detalles de autenticación y conexión SSH
router = {
    'host': '192.168.56.107',
    'port': 22,
    'username': 'cisco',
    'password': 'cisco123!',
    'device_params': {'name': 'csr'}
}

# Configuración XML para cambiar el hostname
xml_config = """
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <hostname>RodrigoRC-MauricioAS</hostname>
    </native>
</config>
"""

try:
    with manager.connect(**router) as m:
        # Enviar la configuración XML al router
        result = m.edit_config(target='running', config=xml_config)
        print("Configuración enviada con éxito.")

except manager.operations.errors.TimeoutExpiredError:
    print("Error: Tiempo de espera agotado al intentar conectarse al router.")

except manager.transport.TransportError as e:
    print(f"Error de transporte: {str(e)}")

except Exception as e:
    print(f"Error desconocido: {str(e)}")