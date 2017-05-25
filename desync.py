from adb_android import adb_android
from time import sleep
from audioshift import run_test
from datetime import datetime

offset = 0
def do_test():
    sleep(5)
    #Actually test here
    for i in range(5):
        res = run_test(5)
        print("Test {};{} {}:{}ms".format(datetime.now(), i, offset, res[0][1]), flush=True)

#Initial control
do_test()

#Test positive offsets
for i in range(120):
    sleep(60)
    do_test()

do_test()
