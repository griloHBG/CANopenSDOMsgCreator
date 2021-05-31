
ssh bbb6 cansend can1 000#82.00
sleep .1
ssh bbb6 cansend can1 000#81.00
sleep .1

ssh bbb6 cansend can1 000#02.00
sleep .1
ssh bbb6 cansend can1 000#80.00
sleep .1

ssh bbb6 cansend can1 $(python main.py create 1 -i 1800 -si 2 -sdo transmit -f download -d 1 -sz 1)
sleep .1
ssh bbb6 cansend can1 $(python main.py create 1 -i 1801 -si 2 -sdo transmit -f download -d 1 -sz 1)
sleep .1
ssh bbb6 cansend can1 $(python main.py create 1 -i 1802 -si 2 -sdo transmit -f download -d 1 -sz 1)
sleep .1

ssh bbb6 cansend can1 $(python main.py create 1 -i 6060 -si 0 -sdo transmit -f download -d FD -sz 1)
sleep .1

ssh bbb6 cansend can1 $(python main.py create 1 -i 6410 -si 1 -sdo transmit -f download -d 5000 -dec -sz 1)
sleep .1
ssh bbb6 cansend can1 $(python main.py create 1 -i 6410 -si 4 -sdo transmit -f download -d 9500 -dec -sz 4)
sleep .1
ssh bbb6 cansend can1 $(python main.py create 1 -i 6410 -si 5 -sdo transmit -f download -d 70 -dec -sz 4)
sleep .1

ssh bbb6 cansend can1 $(python main.py create 1 -i 6040 -si 0 -sdo transmit -f download -d 6 -sz 2)
sleep .1
ssh bbb6 cansend can1 $(python main.py create 1 -i 6040 -si 0 -sdo transmit -f download -d F -sz 2)
sleep .1

ssh bbb6 cansend can1 000#01.00
sleep .1

ssh bbb6 cansend can1 $(python main.py create 1 -i 2030 -si 0 -sdo transmit -f download -d 0 -sz 2)
sleep .1
