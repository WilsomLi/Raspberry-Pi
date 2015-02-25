# auto cool

import commands,time
import RPi.GPIO as io
io.setmode(io.BCM)

fan_pin = 23

io.setup(fan_pin,io.OUT)
io.output(fan_pin,False)
 
def get_cpu_temp():
    tempFile = open( "/sys/class/thermal/thermal_zone0/temp" )
    cpu_temp = tempFile.read()
    tempFile.close()
    return float(cpu_temp)/1000
    # Uncomment the next line if you want the temp in Fahrenheit
    #return float(1.8*cpu_temp)+32
 
def get_gpu_temp():
    gpu_temp = commands.getoutput( '/opt/vc/bin/vcgencmd measure_temp' ).replace( 'temp=', '' ).replace( '\'C', '' )
    return  float(gpu_temp)
    # Uncomment the next line if you want the temp in Fahrenheit
    # return float(1.8* gpu_temp)+32
 
def main():
    while True:
		cpuTmp = get_cpu_temp()
		gpuTmp = get_gpu_temp()
		if cpuTmp > 50 or gpuTmp > 50:
			# start cool fan 60 seconds
			io.output(fan_pin,True)
			time.sleep(60)
		else:
			io.output(fan_pin,False)
		# check every 5 seconds
		time.sleep(5)
 
if __name__ == '__main__':
    main()