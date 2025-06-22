# MQTT for Meshtastic

[MQTT](https://mqtt.org/) is a lightweight messaging protocol designed for small embedded devices and low-bandwidth networks. Meshtastic utilizes your node or client's Internet connection to send and receive messages from a central server. It is often used to bridge portions of the mesh not covered by LoRa radios.

## Limitations

Meshtastic packets that go through the MQTT server have their hop limits reduced to 1. Nodes connected to MQTT will only rebroadcast messages to nodes within range of itself.

<figure markdown="span">
  ![](mqtt_hops.drawio){ width="300" }
</figure>

If **\[ALCE\] Alice** wanted to talk to **\[BOB\] Bob**, her messages would reach. However, due to Hop Limit restrictions and being out of range of **\[MG-1\]**, **\[CHAR\] Charlie** won't receive any packets.

## Radio Configuration

### Network

### MQTT
| Setting            | Value             |
|--------------------|-------------------|
| Server             | `mqtt.rrmesh.net` |
| Username           | `meshnode`        |
| Password           | `rock815river`    |
| Root Topic         | `msh/US`          |
| Encryption enabled | Yes               |
| TLS enabled        | Yes               |

#### Map Reporting (Optional)

### Channels

| Setting  | Value |
|----------|-------|
| Uplink   | Yes   |
| Downlink | Yes   |

### LoRa

| Setting    | Value |
|------------|-------|
| OK to MQTT | Yes   |

