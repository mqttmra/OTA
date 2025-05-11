from ota import OTAUpdater
from WIFI_CONFIG import SSID, PASSWORD

firmware_url = "http://192.168.26.68/OTA/"

ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "test.py")

ota_updater.download_and_install_update_if_available()