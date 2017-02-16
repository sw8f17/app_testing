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
for i in range(7):
    adb_android.shell("input tap " + str(0x22d) + " " + str(0x570))
    sleep(1)
    adb_android.shell("input keyevent 22") #Get focus
    adb_android.shell("input keyevent 22") #Get focus
    adb_android.shell("input keyevent 22")
    sleep(1)
    adb_android.shell("input tap " + str(0xae) + " " + str(0x49a))
    offset += 1
    do_test()

#Reset offset
adb_android.shell("input tap " + str(0x22d) + " " + str(0x570))
sleep(1)
adb_android.shell("input keyevent 22") #Get focus
adb_android.shell("input keyevent 22") #Get focus
for i in range(7):
    adb_android.shell("input keyevent 21")
    offset -= 1
sleep(1)
adb_android.shell("input tap " + str(0xae) + " " + str(0x49a))

#Halfway control
do_test()

#Test negative offsets
for i in range(7):
    adb_android.shell("input tap " + str(0x22d) + " " + str(0x570))
    sleep(1)
    adb_android.shell("input keyevent 22") #Get focus
    adb_android.shell("input keyevent 22") #Get focus
    adb_android.shell("input keyevent 21")
    sleep(1)
    adb_android.shell("input tap " + str(0xae) + " " + str(0x49a))
    offset -= 1
    do_test()

#Reset offset
adb_android.shell("input tap " + str(0x22d) + " " + str(0x570))
sleep(1)
adb_android.shell("input keyevent 22") #Get focus
adb_android.shell("input keyevent 22") #Get focus
for i in range(7):
    adb_android.shell("input keyevent 22")
    offset += 1
sleep(1)
adb_android.shell("input tap " + str(0xae) + " " + str(0x49a))

#End control
do_test()
