# Switchboard

## Software requirements

```bash
sudo apt-get install python-dev
sudo pip install Flask
sudo pip install flask-hmacauth
sudo pip install schedule
```

## Components

 * Raspberry Pie
 * 5v relay module
 * 10 pin female to female breadboard jumper wires

Examples:
 * http://www.amazon.co.uk/Raspberry-Pi-Official-Desktop-Starter/dp/B01CSD1X3E/278-1401132-0851767?ie=UTF8&psc=1&redirect=true&ref_=oh_aui_detailpage_o02_s00
 * http://www.amazon.co.uk/GoTron-8-channel-Optocoupler-Arduino-Raspberry/dp/B01D19AYXY?ie=UTF8&psc=1&redirect=true&ref_=oh_aui_detailpage_o01_s00
 * http://www.amazon.co.uk/Alwayswish-Multicolored-Female-Breadboard-Jumper/dp/B018W4L6D0?ie=UTF8&psc=1&redirect=true&ref_=oh_aui_detailpage_o01_s00

## Wiring

https://www.youtube.com/watch?v=oaf_zQcrg7g

https://www.raspberrypi.org/documentation/usage/gpio-plus-and-raspi2/

http://i.stack.imgur.com/sVvsB.jpg

http://pinout.xyz/pinout/ground

This application will use BOARD numbering instead of BCM.

http://raspberrypi.stackexchange.com/questions/12966/what-is-the-difference-between-board-and-bcm-for-gpio-pin-numbering

Multimeter to test the connections: https://www.amazon.co.uk/gp/product/B00EYYJRC0/ref=oh_aui_detailpage_o00_s00?ie=UTF8&psc=1

# Configuration

## Server

```bash
cp config.sample.json config.json
```

Customize config.json with your own values!

## Client

```bash
cp client.sample.json client.json
```

Customize client.json with your own values!
