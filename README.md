Jit Biswas Pressure sensor's Gateway
====================================

program to use the pressure sensors developed by Jit Biswas and to transfer the information to the server using the ubigate library.

This programe have to be set up on the beaglebone when the pressure sensors are installed in a home.

TO RUN THE PROGRAM WITH THE PRESSURE SENSOR
Turn on the pressure sensor
Plug the Gateway to your linux machine
Run 'sf.sh' script in gateway_pressure' folder.
Pipe the output the 'run.sh' of the 'gateway_pressure' folder in the 'jitPressureSensor-gw.py' file of the 'jitPressureSensor' folder.

TO RUN THE PROGRAM WITHOUT THE PRESSURE SENSOR
You can use the 'inputs.txt'file in the "ressources" folder. This file correspond to the outputs of the pressure sensor (so the inputs of our program). So just pipe this file in the 'jitPressureSensor-gw.py' file
