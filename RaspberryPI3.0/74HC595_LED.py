import RPi.GPIO as GPIO
import time

SDI = 11
RCLK = 12
SRCLK = 13

LED0 = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80]
LED1 = [0x01, 0x03, 0x07, 0x0f, 0x1f, 0x3f, 0x7f, 0xff]
LED2 = [0x01, 0x05, 0x15, 0x55, 0xb5, 0xf5, 0xfb, 0xff]
LED3 = [0x01, 0x03, 0x0b, 0x0f, 0x2f, 0x3f, 0xbf, 0xff]

def print_msg():
    print("program is running...")
    print("please press ctrl+c to end the program...")

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(SDI, GPIO.OUT)
    GPIO.setup(RCLK, GPIO.OUT)
    GPIO.setup(SRCLK, GPIO.OUT)
    GPIO.output(SDI, GPIO.LOW)
    GPIO.output(RCLK, GPIO.LOW)
    GPIO.output(SRCLK, GPIO.LOW)

def hc595_in(dat):
    for bit in range(0, 8):
        GPIO.output(SDI, 0x80 & (dat << bit))
        GPIO.output(SRCLK, GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(SRCLK, GPIO.LOW)

def hc595_out():
    GPIO.output(RCLK, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(RCLK, GPIO.LOW)

def loop():
    WhichLeds = LED3 #LED값 변경되는곳
    sleeptime = 0.1
    while True:
        for i in range(0, len(WhichLeds)):
            hc595_in(WhichLeds[i])
            hc595_out()
            time.sleep(sleeptime)

        for i in range(len(WhichLeds)-1, -1, -1):
            hc595_in(WhichLeds[i])
            hc595_out()
            time.sleep(sleeptime)

def destroy():
    GPIO.cleanup()

if __name__ == '__main__':
    print_msg()
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
