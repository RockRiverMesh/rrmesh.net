# MeshCore

[MeshCore](https://meshcore.io/) is a lightweight, mesh-routed messaging protocol for LoRa radios. It is optimized for low-power, store-and-forward operation across repeaters and was designed as a more spectrum-efficient alternative to traditional flood-based LoRa meshes. Rock River Mesh primarily operates MeshCore repeaters across the region.

## Why MeshCore

- **Routed, not flooded** — packets traverse the mesh along discovered paths instead of being rebroadcast by every node, which keeps airtime usage low even as the network grows.
- **Repeater-friendly** — repeaters can run unattended on solar, with minimal duty cycle.
- **Compatible hardware** — runs on the same Heltec, RAK, and LilyGO LoRa boards as Meshtastic.

## Getting on the Mesh

We're still publishing the local channel keys and onboarding guide. In the meantime, see the upstream [MeshCore documentation](https://docs.meshcore.io/) for general setup. Once your radio is flashed and configured, reach out via the [contact page](../contact.md) and we'll get you connected to the regional channels.
