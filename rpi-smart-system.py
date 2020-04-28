import gpio_smart_system_lib as gssl
import yaml
import sys

with open(f'config.yaml') as f:
    config = yaml.load(f, Loader=yaml.FullLoader)

for relay in config:
    print(f"{relay['name']} initiated at pin {relay['pin']}")
    exec(f"{relay['name']} = gssl.Relay({relay['pin']}, '{relay['name']}', '{relay['desc']}')")

if sys.argv[1] == "-t":
    exec(f"{sys.argv[2]}.toggle()")
    print(f"{sys.argv[2]}", "is now", eval(f"{sys.argv[2]}.status"))

#elif sys.argv[1] == "-s":
    exec(f"{sys.argv[2]}.set({sys.argv[3]})")

else:
    print("Not a command, use the man page")

