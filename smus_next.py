from adb_android import adb_android
from time import sleep
from audioshift import run_test

offset = 0
def do_test():
    sleep(5)
    #Actually test here
    for i in range(5):
        res = run_test(5)
        print("Test {} {}:{}ms".format(i, offset, res[0][1]), flush=True)

#Initial control
do_test()

#Test positive offsets
for i in range(5):
    sleep(1)
    #adb_android.shell("input tap " + str(0x3e4) + " " + str(0x717))
    sleep(10)
    offset += 1
    do_test()
