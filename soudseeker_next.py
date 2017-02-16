from adb_android import adb_android
from time import sleep
from audioshift import run_test

time = 0
def do_test():
    sleep(5)
    #Actually test here
    for i in range(5):
        res = run_test(5)
        print("Test {} {}:{}ms".format(i, time, res[0][1]), flush=True)

#Initial control
for i in range(5):
    #Next
    adb_android.shell("input tap " + str(0x3fb) + " " + str(0x8ea))
    #Play/Pause
    adb_android.shell("input tap " + str(0x2c2) + " " + str(0x8f4))
    sleep(5)
    #Prev
    adb_android.shell("input tap " + str(0x1aa) + " " + str(0x8f9))
    #Prev
    adb_android.shell("input tap " + str(0x1aa) + " " + str(0x8f9))
    #Play/Pause
    adb_android.shell("input tap " + str(0x2c2) + " " + str(0x8f4))
    sleep(10)
    time = i
    do_test()

