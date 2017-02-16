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
    adb_android.shell("input tap " + str(0x37d) + " " + str(0x79))
    sleep(1)
    time = i
    do_test()

