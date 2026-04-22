# Firmware
## Improved OTA Bootloader

nRF52-based Devices should be prepared with the OTAFIX Bootloader. This will ensure the device falls back to Bluetooth
OTA mode if the flashing process fails. It also contains a number of changes that make the transfer process more 
reliable.

https://github.com/oltaco/Adafruit_nRF52_Bootloader_OTAFIX

### Installing the Bootloader

1. Connect the device to a computer with a USB cable.
2. Place the device into DFU mode. On most devices, double-tap the RESET button.
3. A USB drive will show up. Copy the appropriate OTAFIX UF2 file to the device.
4. Wait for the device to reboot.

