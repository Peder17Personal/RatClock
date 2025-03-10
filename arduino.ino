void setup() {
    // Start the serial communication with the Raspberry Pi
    Serial.begin(9600);
    // Wait for the serial port to connect
    while (!Serial) {
        ; // Wait for serial port to connect. Needed for native USB port only
    }
    Serial.println("Arduino is ready to receive data from Raspberry Pi");
}

void loop() {
    // Check if data is available to read
    if (Serial.available() > 0) {
        // Read the incoming byte
        char incomingByte = Serial.read();
        // Print the received byte to the Serial Monitor
        Serial.print("Received: ");
        Serial.println(incomingByte);
    }
}