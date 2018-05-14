import RPi.GPIO as GPIO
import time
import gc


def ustawienia():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(14, GPIO.OUT)
    GPIO.setup(15, GPIO.OUT)
    GPIO.setup(1, GPIO.OUT)
    GPIO.setup(2, GPIO.OUT)
    GPIO.setup(3, GPIO.OUT)
    GPIO.setup(4, GPIO.OUT)
    GPIO.setup(5, GPIO.OUT)

    global serwo
    skn = GPIO.PWM(12,46 )
    sko = GPIO.PWM(15,46 )
    rT = GPIO.PWM(14, 46)
    lT = GPIO.PWM(15, 46)
    GPIO.output(18, False)


def zerowanie():
    gc.enable()
    reload(PWM)
    GPIO.setup(11, GPIO.ALT0)
    GPIO.setup(13, GPIO.ALT0)
    GPIO.setup(12, GPIO.ALT0)
    GPIO.setup(16, GPIO.ALT0)
    GPIO.setup(7, GPIO.ALT0)
    GPIO.setup(18, GPIO.ALT0)


licznik = 0





for licznik in range(2000):
    try:
        ustawienia()
        rT.start(3)
        lT.start(3)
        time.sleep(1)
        rT.stop()
        lT.stop()
        time.sleep(1)
        rT.start(11)
        lT.start(11)
        time.sleep(1)
        rT.stop()
        lT.stop()
        time.sleep(1)
        rT.start(11)
        lT.start(3)
        time.sleep(1)
        rT.stop()
        lT.stop()
        time.sleep(1)
        rT.start(3)
        lT.start(11)
        time.sleep(1)
        rT.stop()
        lT.stop()
        GPIO.cleanup()
        GPIO.setwarnings(False)


    except KeyboardInterrupt:
        pass
        serwo.stop()
        skn.stop()
        sko.stop()
        GPIO.cleanup()
        zerowanie() 