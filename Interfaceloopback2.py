from ncclient import manager
from lxml import etree

# Configuración de conexión al router
router = {
    "host": "192.168.56.107",
    "port": 22,
    "username": "cisco",
    "password": "cisco123!"
}

# Definir la configuración XML para crear la interfaz loopback
loopback_config = """
<config>
    <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
            <name>Loopback1</name>
            <description>Examen-T-Riquelme-Ano</description>
            <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:softwareLoopback</type>
            <enabled>false</enabled>
            <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                <address>
                    <ip>1.1.1.1</ip>
                    <netmask>255.255.255.255</netmask>
                </address>
            </ipv4>
        </interface>
    </interfaces>
</config>
"""

# Establecer la conexión NETCONF con el router
with manager.connect(**router) as m:
    # Enviar la configuración al router
    response = m.edit_config(target="running", config=etree.fromstring(loopback_config))

    # Imprimir la respuesta del router
    print(response)
