import psutil
import paho.mqtt.publish as publish
import time

# Configurações do MQTT broker
mqtt_broker = "172.16.0.166"
mqtt_porta = 1883
mqtt_topico_cpu = "system-info/cpu"
mqtt_topico_ram = "system-info/ram"
mqtt_topico_disco = "system-info/disco"
mqtt_topico_gpu = "system-info/gpu"

# Loop infinito para enviar as informações periodicamente
while True:
    # Obter informações de uso do sistema
    uso_cpu = psutil.cpu_percent()
    uso_ram = psutil.virtual_memory().percent
    uso_disco = psutil.disk_usage('/').percent
    uso_gpu = psutil.cpu_percent()

    # Publicar as informações no broker MQTT
    publish.single(mqtt_topico_cpu, str(uso_cpu), hostname=mqtt_broker, port=mqtt_porta)
    publish.single(mqtt_topico_ram, str(uso_ram), hostname=mqtt_broker, port=mqtt_porta)
    publish.single(mqtt_topico_disco, str(uso_disco), hostname=mqtt_broker, port=mqtt_porta)
    publish.single(mqtt_topico_gpu, str(uso_gpu), hostname=mqtt_broker, port=mqtt_porta)

    print(uso_cpu, uso_ram, uso_disco, uso_gpu)

    # Esperar um tempo antes de coletar e enviar as informações novamente
    time.sleep(5)