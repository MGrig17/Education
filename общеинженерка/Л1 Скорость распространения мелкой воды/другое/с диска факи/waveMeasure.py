import RPi.GPIO as gpio
import sys
from time import sleep
import time
from matplotlib import pyplot
gpio.setmode(gpio.BCM)
dac=[26, 19, 13, 6, 5, 11, 9, 10]
comp=4
knop_out=2
knop_in=22
gpio.setup(knop_out, gpio.OUT, initial=gpio.HIGH)
gpio.setup(knop_in, gpio.IN)
gpio.setup(dac, gpio.OUT)
gpio.setup(comp, gpio.IN)

def perev(a):
    return [int (elem) for elem in bin(a)[2:].zfill(8)]

def adc():
    k=0
    for i in range(7, -1, -1):
        k+=2**i
        gpio.output(dac, perev(k))
        sleep(0.005)
        if gpio.input(comp)==0:
            k-=2**i
    return k

def waitForOpen():

    print('GPIO initialized. Wait for door opening...')

    while gpio.input(knop_in) >0:
        pass

    print('The door is open. GPIO has been cleaned up. Start sampling...')

volt=[]
time_start=0
time_len=0

try:
    waitForOpen()
    time_start=time.time()
    while True:
        volt.append(adc()/256*3.3)
    
    
finally:
    time_len=time.time()-time_start

    with open('wave-data-120mm-kalibr.txt', 'w') as file:
        file.write(str(time_len) +'\n')
        for i in volt:
            file.write(str(i) +'\n')

    
    time_step=[i*time_len/len(volt) for i in range(len(volt))]
    pyplot.plot(time_step, volt)
    pyplot.show()
    gpio.output(dac, 0)
    gpio.cleanup() 