import cpuTimer
from cpuTimer import CPUTimer

cpuTimer = CPUTimer(0)

cpuTimer.start()

for i in range(0,100000):
    a = i

cpuTimer.stop()

print(cpuTimer.get_time("last", "ms"))

cpuTimer.start()

for i in range(0,100000):
    a = i

cpuTimer.stop()

print(cpuTimer.get_time("last", "ms"))