#include <EnableInterrupt.h>
#include <math.h> // For tan function

#define NUM_CHANNELS 2 // Number of channels you want to support
const int INPUT_CHANNEL_PINS[] = {A0, A1}; // Corrected pin assignments

// InputChannel structure
struct InputChannel {
 int pin;
 volatile uint32_t startTime;
 volatile uint16_t pulseDuration;
 int value;
};

// Array of input channels
InputChannel inputChannels[NUM_CHANNELS];

// Function prototype for handleInterrupt
void handleInterrupt(int channelIndex);

// Interrupt handler functions for each channel
void handleInterruptChannel0() {
    handleInterrupt(0);
}

void handleInterruptChannel1() {
    handleInterrupt(1);
}

// Interrupt handler function
void handleInterrupt(int channelIndex) {
    InputChannel& channel = inputChannels[channelIndex];
    if (digitalRead(channel.pin) == HIGH) {
        channel.startTime = micros();
    } else {
        channel.pulseDuration = micros() - channel.startTime;
        // Map the pulse duration to a value (e.g., 1000-2000us to 0-100%)
        channel.value = map(channel.pulseDuration, 1000, 2000, -20, 20);
        // Ensure the value stays within bounds
        channel.value = constrain(channel.value, -20, 20);
        
        // Now you can use channel.value to control your device
        // For example, write it to a motor controller or log it to Serial
    }
}

// Function to initialize input channels
void setupInputChannels() {
 for (int i = 0; i < NUM_CHANNELS; i++) {
    inputChannels[i].pin = INPUT_CHANNEL_PINS[i];
    pinMode(inputChannels[i].pin, INPUT);
    // Use a different ISR for each channel
    if (i == 0) {
        enableInterrupt(inputChannels[i].pin, handleInterruptChannel0, CHANGE);
    } else if (i == 1) {
        enableInterrupt(inputChannels[i].pin, handleInterruptChannel1, CHANGE);
    }
 }
}

// Placeholder function to set the speed of an engine
void setEngineSpeed(int engine, int speed) {
 // Implement the logic to set the speed of the specified engine
 // For example, speed could be a PWM value for a motor controller
}

void setup() {  
 Serial.begin(9600);
 setupInputChannels();
}

void loop() {
 // Calculate the steering angle and power based on the input values
 float steeringAngle = (inputChannels[0].value / 20.0); // Assuming the first channel controls steering
 float power = (inputChannels[1].value / 20.0) * -1; // Assuming the second channel controls power

 // Calculate the bias based on the steering angle and wheelbase
 float wheelbase = 1.0; // Example wheelbase, adjust as needed
 float bias = tan(steeringAngle) * wheelbase / 2;

 // Calculate the power distribution between the engines
 float engine1Power = (power - bias);
 float engine2Power = (power + bias);

 // Ensure the power values are within the expected range
 engine1Power = constrain(engine1Power, -100, 100);
 engine2Power = constrain(engine2Power, -100, 100);

 // Set the speed of the engines
 setEngineSpeed(1, engine1Power/2);
 setEngineSpeed(2, engine2Power/2);

 // For debugging purposes, print the values to the serial monitor
 Serial.print("Steering Angle: ");
 Serial.print(steeringAngle);
 Serial.print("\tPower: ");
 Serial.print(power);
 Serial.print("\tEngine 1 Power: ");
 Serial.print(engine1Power);
 Serial.print("\tEngine 2 Power: ");
 Serial.println(engine2Power);

 delay(100);
}
