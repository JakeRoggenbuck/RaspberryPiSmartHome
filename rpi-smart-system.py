import gpio_smart_system_lib as gssl
import sys

if sys.argv[1] == "-t":
   gssl.toggle()

elif sys.argv[1] == "-s":
    gssl.set(sys.argv[2])

else:
    print("Not a command, use the man page")

