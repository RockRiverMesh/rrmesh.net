# MQTT for Meshtastic

[MQTT](https://mqtt.org/) is a lightweight messaging protocol designed for small embedded devices and low-bandwidth networks. Meshtastic utilizes your node or client's Internet connection to send and receive messages from a central server. It is often used to bridge portions of the mesh not covered by LoRa radios.

## Limitations

Meshtastic packets that arrive from the MQTT server have their hop limit reduced to 0, so the receiving gateway will not rebroadcast them over LoRa. Only nodes within direct LoRa range of an MQTT-connected gateway will receive packets that come in over MQTT.

<figure markdown="span">
  ![](mqtt_hops.drawio){ width="300" }
</figure>

If **\[ALCE\] Alice** wants to talk to **\[BOB\] Bob**, her messages reach him over MQTT via the **\[MG-1\]** gateway. **\[CHAR\] Charlie**, however, is out of LoRa range of **\[MG-1\]** — and because packets arriving from MQTT have their hop limit reduced to 0, **\[MG-1\]** can't relay them any further. Charlie never receives Alice's messages.

## Radio Configuration

### Network

Your node must have working Internet access before MQTT can connect. Most users join the node to a Wi-Fi network via the Meshtastic app under **Radio configuration → Network → WiFi**. If your node has Ethernet, configure that instead. Confirm the **Network status** in the app shows a green/connected state before moving on.

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

If you want your node to appear on the [Portal](../../portal.md) map, enable **Map reporting** under the MQTT settings. The node will publish its position and basic metadata to the configured MQTT root topic on a periodic interval. Position precision is configurable — pick a value you're comfortable broadcasting publicly.

| Setting            | Value           |
|--------------------|-----------------|
| Map reporting      | Yes             |
| Publish interval   | `900` (15 min)  |
| Precision          | `14` (~1.2 km)  |

### Channels

| Setting  | Value |
|----------|-------|
| Uplink   | Yes   |
| Downlink | Yes   |

### LoRa

| Setting    | Value |
|------------|-------|
| OK to MQTT | Yes   |

