# RaspberryPiSmartHome

### About
GSSL is a simple raspberry pi gpio object library

### rpi smart system
A simple gpio relay interface frontend for raspberry pi using GPIO

### Requirements
You will need "PRi.GPIO". This is pre installed on raspberry pis.

### Uses for GPIO
First init an object by `light = Relay(<pin number>, <'Human readable name'>)` <br>
Then you can call methods like `light.set(1)` for turning the relay to 1 <br>
You can also toggle the relay by `light.toggle()`

### Useing rpi smart system (frontend)
#### Flags
-v	Show relay setup verbosely<br>
-t	Toggle a relay using name<br>
-s	Set a relay to value using name<br>
-l	List all relays and their status<br>

read manpage for more frontend info
