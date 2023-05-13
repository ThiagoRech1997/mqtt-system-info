Para executar o script automaticamente durante o início do sistema operacional, você pode adicionar uma tarefa agendada ou um serviço ao seu sistema.

Uma maneira de fazer isso é criar um arquivo de serviço systemd. Siga os passos abaixo para criar um arquivo de serviço para o seu script:

- Crie um arquivo de serviço mqtt-system-info.service em /etc/systemd/system/ com o seguinte conteúdo:

```ini
[Unit]
Description=MQTT System Info Service
After=multi-user.target

[Service]
Type=simple
User=<user>
ExecStart=/path/to/python /path/to/main.py
Restart=always

[Install]
WantedBy=multi-user.target
```

Substitua <user> pelo nome do usuário que irá executar o script e /path/to pelos caminhos corretos para o executável do Python e o arquivo main.py.

- Salve e feche o arquivo.

- Ative o serviço com o seguinte comando:

```bash
sudo systemctl enable mqtt-system-info.service
```

- Inicie o serviço com o seguinte comando:

```bash
sudo systemctl start mqtt-system-info.service
```
A partir de agora, o serviço será iniciado automaticamente durante o início do sistema operacional. Você pode verificar o status do serviço usando o seguinte comando:

```bash
sudo systemctl status mqtt-system-info.service
```

Se você precisar fazer alterações no arquivo de serviço, edite-o e depois recarregue o systemd com o seguinte comando:

```bash
sudo systemctl daemon-reload
```

Lembre-se de que, se o script depende de outras bibliotecas, você precisa garantir que elas estejam instaladas em um ambiente ou sistema operacional adequado.

Para configurar no Home Assistant adicione no arquivo configuration.yaml

```yaml
# MQTT-Broker
sensor:
  - platform: mqtt
    state_topic: "system-info/cpu"
    name: "CPU Usage"
    unit_of_measurement: "%"
    value_template: "{{ value_json }}"
  - platform: mqtt
    state_topic: "system-info/ram"
    name: "Memory Usage"
    unit_of_measurement: "%"
    value_template: "{{ value_json }}"
  - platform: mqtt
    state_topic: "system-info/disco"
    name: "Disk Usage"
    unit_of_measurement: "%"
    value_template: "{{ value_json }}"
```
Reinicie seu Home Assistant ante de seguir com o proximo passo.

E na interface Lovelace crie um card contendo:

```yaml
type: entities
entities:
  - entity: sensor.cpu_usage
    name: CPU Usage
    icon: mdi:cpu-64-bit
  - entity: sensor.memory_usage
    name: Memory Usage
    icon: mdi:memory
  - entity: sensor.disk_usage
    name: Disk Usage
    icon: mdi:harddisk
```