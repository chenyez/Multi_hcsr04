import pypruss
import time


pypruss.modprobe(1000)

print 'Initializing PRU'
pypruss.init()

print 'successfully initialized!'

pypruss.open(0)
#    print 'PRU open failed'
#    return 1


pypruss.pruintc_init()

pruData=pypruss.map_prumem(0)

pypruss.exec_program(0, "./hcsr04.bin") 

i=0
while i<=20:
    pypruss.wait_for_event(0)                           # Wait for event 0 which is connected to PRU0_ARM_INTERRUPT
    pypruss.clear_event(0,pypruss.PRU0_ARM_INTERRUPT)           # Clear the event
    print 'Orange Distance = ', round(float(pruData[0]),2), 'cm, Yellow Distance =', round(float(pruData[1]),2),'cm, Red Distance =', round(float(pruData[2]),2),'cm, Blue Distance =', round(float(pruData[3]),2),'cm, Green Distance = ',round(float(pruData[4]),2),'cm\n'
    time.sleep(1)
    i=i+1

#disable PRU0
pypruss.pru_disable(0)               
pypruss.exit()

#return 0

