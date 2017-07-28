import pypruss
import time

class PyprussTest():
	def work2(self):

		pypruss.modprobe(100)

		print 'Initializing PRU'
		pypruss.init()

		print 'successfully initialized!'

		if pypruss.open(0):
			print 'PRU open failed'
			return 1


		pypruss.pruintc_init()

		pruData=pypruss.map_prumem(pypruss.PRUSS0_PRU0_DATARAM)
#		pruData=int(pruDataMem)
#		print pruData
		pypruss.exec_program(0, "./hcsr04.bin") 

		i=0
		while i<=20:
  			pypruss.wait_for_event(0)                           # Wait for event 0 which is connected to PRU0_ARM_INTERRUPT
			pypruss.clear_event(0,pypruss.PRU0_ARM_INTERRUPT)           # Clear the event
#			print 'Orange Distance = ', round(float(pruData[0])/58.44,2), 'cm, Yellow Distance =', round(float(pruData[1])/58.44,2),'cm, Red Distance =', round(float(pruData[2])/58.44,2),'cm, Blue Distance =', round(float(pruData[3])/58.44,2),'cm, Green Distance = ', round(float(pruData[4])/58.44,2), 'cm\n'
			print pruData[0]
    			time.sleep(1)
    			i=i+1

#disable PRU0
		pypruss.pru_disable(0)               
		pypruss.exit()

		return 0



pyprusstest=PyprussTest()
i=pyprusstest.work2()
