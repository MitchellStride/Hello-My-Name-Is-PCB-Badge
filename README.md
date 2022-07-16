# The 'Hello my name is' PCB Badge

![](./hello_my_name_is/img/badge.png)
![](./hello_my_name_is/img/badge2.png)

This **#Badgelife** PCB was created to test some circuits to be used in future art PCBs.
I also wanted a small project to bring to local hardware meetups.   

## Features:
* Powered by x2 AA Batteries
* Highly compatible with JLCPCB's basic SMT parts
* Raspberry Pi RP2040 uC w/ Dual core ARM Cortex-M0+
* OLED Screen, RGB LEDs, Buttons
* SAO Connector!

![](./hello_my_name_is/img/bot_ren.PNG)
![](./hello_my_name_is/img/top_ren.PNG)

## Issues:
* I seen someone's design online using a RGB led running at 3.3V (below spec). I tried to replicate it and the LEDs were very flaky and worked intermittently. Experiment failed 😢.
* AA boost converter not yet tested, just using USB power so far.

![](./hello_my_name_is/img/temp.gif)