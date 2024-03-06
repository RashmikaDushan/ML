#include <Arduino.h>
#include <BLEDevice.h>
#include <BLEClient.h>
#include <BLEUtils.h>
#include <BLE2902.h>

BLEClient* pClient;

// Set your server's Bluetooth device address here
const char* serverAddress = "0C:E4:41:DA:C1:E1";

// The service UUID of the Bluetooth server
static BLEUUID serviceUUID("0000XXXX-0000-1000-8000-00805F9B34FB");

// The characteristic UUID of the Bluetooth server
static BLEUUID charUUID("0000YYYY-0000-1000-8000-00805F9B34FB");

BLERemoteCharacteristic* pCharacteristic; // Change type to BLERemoteCharacteristic*

void setup() {
  Serial.begin(115200);
  BLEDevice::init("");

  // Connect to the Bluetooth server
  pClient = BLEDevice::createClient();
  pClient->connect(BLEAddress(serverAddress));

  // Get the service and characteristic
  BLERemoteService* pRemoteService = pClient->getService(serviceUUID);
  if (pRemoteService != nullptr) {
    pCharacteristic = pRemoteService->getCharacteristic(charUUID);
  }
}

void loop() {
  if (pClient->isConnected() && pCharacteristic != nullptr) {
    // Generate a random value
    int randomValue = random(0, 100);

    // Convert the random value to a string
    String dataToSend = String(randomValue);

    // Send the data to the server
    pCharacteristic->writeValue(dataToSend.c_str(), dataToSend.length());
    
    Serial.println("Sent data: " + dataToSend);
  }

  delay(1000);  // Adjust the delay as needed
}
