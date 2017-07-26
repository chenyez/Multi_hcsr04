
/* Second Sensor begin */

	MOV r3, GPIO1 | GPIO_OE
	LBBO r2, r3, 0, 4
	CLR r2, BIT_TRIGGER2
	SET r2, BIT_ECHO2


	SBBO r2, r3, 0, 4

TRIGGER2:

	// Fire the sonar
	// Set trigger pin to high
	MOV r2, 1<<BIT_TRIGGER2
	MOV r3, GPIO1 | GPIO_SETDATAOUT
	SBBO r2, r3, 0, 4

	// Delay 10 microseconds (200 MHz / 2 instructions = 10 ns per loop, 10 us = 1000 loops) 
	MOV delay, 1000
TRIGGER_DELAY2:
	SUB delay, delay, 1
	QBNE TRIGGER_DELAY2, delay, 0
	
	// Set trigger pin to low
	MOV r2, 1<<BIT_TRIGGER2
	MOV r3, GPIO1 | GPIO_CLEARDATAOUT
	SBBO r2, r3, 0, 4
	
	// Wait for BIT_ECHO to go high, i.e. wait for the echo cycle to start
	MOV r3, GPIO1 | GPIO_DATAIN
WAIT_ECHO2:
	// Read the GPIO until BIT_ECHO goes high
	LBBO r2, r3, 0, 4

	QBBC WAIT_ECHO2, r2, BIT_ECHO2

	// roundtrip measures the echo duration in microseconds, resolution is 1us

	MOV roundtrip, 0

SAMPLE_ECHO2:

	// Delay 1 microsecond (adjusted because it takes time to query the GPIO pin)
	MOV delay, 76
SAMPLE_ECHO_DELAY2:
	SUB delay, delay, 1
	QBNE SAMPLE_ECHO_DELAY2, delay, 0
	
	// Add 1us to the roundtrip counter
	ADD roundtrip, roundtrip, 1
	
	// Read GPIO until BIT_ECHO goes low
	LBBO r2, r3, 0, 4
	QBBS SAMPLE_ECHO2, r2, BIT_ECHO2


// Second Sensor End
	SBCO roundtrip, c24, 4, 4
	// Trigger the PRU0 interrupt (C program gets the event)
	MOV r31.b0, PRU0_ARM_INTERRUPT+16

	// Delay to allow sonar to stop resonating and sound burst to decay in environment
	MOV delay, 3000000

RESET_DELAY2:
	SUB delay, delay, 1
	QBNE RESET_DELAY2, delay, 0


















 "GPIO44", "GPIO45","GPIO46","GPIO47","GPIO62","GPIO63","GPIO23","GPIO26";

