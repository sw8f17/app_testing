from adb_android import adb_android
from time import sleep

offset = 0
def do_test():
    sleep(5)
    print("Testing {}".format(offset))
    #Actually test here

#Initial control
do_test()

#Test positive offsets
for i in range(10):
    adb_android.shell("input tap " + str(0x3ec) + " " + str(0xa7))
    sleep(1)
    adb_android.shell("input keyevent 22") #Get focus
    adb_android.shell("input keyevent 22")
    adb_android.shell("input tap " + str(0x390) + " " + str(0x49c))
    offset += 40
    do_test()

#Reset offset
adb_android.shell("input tap " + str(0x3ec) + " " + str(0xa7))
sleep(1)
adb_android.shell("input keyevent 21") #Get focus
for i in range(10):
    adb_android.shell("input keyevent 21")
    offset -= 40
adb_android.shell("input tap " + str(0x390) + " " + str(0x49c))

#Halfway control
do_test()

#Test negative offsets
for i in range(10):
    adb_android.shell("input tap " + str(0x3ec) + " " + str(0xa7))
    sleep(1)
    adb_android.shell("input keyevent 21") #Get focus
    adb_android.shell("input keyevent 21")
    adb_android.shell("input tap " + str(0x390) + " " + str(0x49c))
    offset -= 40
    do_test()

#Reset offset
adb_android.shell("input tap " + str(0x3ec) + " " + str(0xa7))
sleep(1)
adb_android.shell("input keyevent 22") #Get focus
for i in range(10):
    adb_android.shell("input keyevent 22")
    offset -= 40
adb_android.shell("input tap " + str(0x390) + " " + str(0x49c))

#End control
do_test()
