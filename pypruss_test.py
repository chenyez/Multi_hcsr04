from __future__ import print_function

import pypruss

class TestPypruss:
	def work(self):

		print("Running modprobe")
		pypruss.modprobe(1000)
		print("modprobe ok")

		pypruss.init()
		print("init ok")

		pypruss.open(0)
#			print("open ok")
#			return 1
#		else:
#			return 0

		pypruss.pruintc_init()
		print("intc ok")

		print("ddr addr is " + hex(pypruss.ddr_addr()))
		print("ddr size is " + hex(pypruss.ddr_size()))

		pypruss.exit()
		print("exit ok")

		pypruss.modunprobe()
		print("modunprobe ok")
testpypruss=TestPypruss()
testpypruss.work()
