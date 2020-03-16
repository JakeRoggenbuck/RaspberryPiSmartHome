# RaspberryPiSmartHome

### About
GSSL is a simple raspberry pi gpio object library

### Requirements
You will need "PRi.GPIO". This is pre installed on raspberry pies.

### Uses
First init an object by `light = Relay(<pin number>, <'Human readable name'>)` <br>
Then you can call methods like `light.set(1)` for turning the relay to 1 <br>
You can also toggle the relay by `light.toggle()`
