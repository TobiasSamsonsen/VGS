#include <EnableInterrupt.h>

#define THROTTLE_CHANNEL_PIN A0 // Connect this to the receiver output for throttle

// These variables will hold the start times and pulse durations for each channel
volatile uint32_t startTimeThrottle;
volatile uint16_t pulseDurationThrottle;
int throttleValue; // Declare throttleValue as a global variable

// Function to calculate the throttle value
void calcThrottle() {
  if (digitalRead(THROTTLE_CHANNEL_PIN) == HIGH) {
    startTimeThrottle = micros();
  } else {
    pulseDurationThrottle = micros() - startTimeThrottle;
    // Map the pulse duration to a throttle value (e.g.,  1000-2000us to  0-100%)
    throttleValue = map(pulseDurationThrottle,  1000,  2000,  0,  100);
    // Ensure the throttle value stays within bounds
    throttleValue = constrain(throttleValue,  0,  100);
    
    // Now you can use throttleValue to control your device
    // For example, write it to a motor controller or log it to Serial
  }
}

void setup() {  
  Serial.begin(9600);
  pinMode(THROTTLE_CHANNEL_PIN, INPUT);
   
  // Set up the interrupt for the throttle channel
  enableInterrupt(THROTTLE_CHANNEL_PIN, calcThrottle, CHANGE);
}

void loop() {
  // Here you can use the throttleValue variable to control your device
  // For debugging purposes, print the throttle value to the serial monitor
  float actualThrottleValue = throttleValue / 100;
  Serial.println(String(throttleValue));
  delay(100);
}