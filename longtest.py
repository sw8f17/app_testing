from adb_android import adb_android
from time import sleep
from audioshift import run_test
import calendar
import time

offset = 0
def do_test():
    sleep(5)
    #Actually test here
    for i in range(5):
        res = run_test(5)
        print("Test {} {}:{}ms".format(i, calendar.timegm(time.gmtime()), res[0][1]), flush=True)

#Initial control
do_test()

#Test positive offsets
while True:
    sleep(10)
    offset += 1
    do_test()
