# MQTT for Meshtastic

[MQTT](https://mqtt.org/) is a lightweight messaging protocol designed for small embedded devices and low-bandwidth networks. Meshtastic utilizes your node or clients TCP/IP network to send and receive messages from a central server. It is often used to bridge portions of the mesh not covered by LoRa radios.

Meshtastic packets that go through the MQTT server have their hop limits reduced to 1. Nodes connected to MQTT will only rebroadcast messages to nodes within range of itself.

<figure markdown="span">
  ![](mqtt_hops.drawio){ width="300" }
</figure>

If **\[ALCE\] Alice** wanted to talk to **\[BOB\] Bob**, her messages would reach. However, due to Hop Limit restrictions and being out of range of **\[MG-1\]**, **\[CHAR\] Charlie** won't receive any.

## Radio Configuration

| Channel            |                   |
|--------------------|-------------------|
| Uplink             | Yes               |
| Downlink           | Yes               |
| **MQTT**           |                   |
| Server             | `mqtt.rrmesh.net` |
| Username           | `meshnode`        |
| Password           | `rock815river`    |
| Root Topic         | `msh/US`          |
| Encryption enabled | Yes               |
| TLS enabled        | Yes               |
| **LoRa**           |                   |
| OK to MQTT         | Yes               |

For help configuring your radio, see the official [MQTT Module](https://meshtastic.org/docs/configuration/module/mqtt/) page.