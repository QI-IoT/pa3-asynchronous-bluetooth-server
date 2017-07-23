# Introduction

Build an asynchronous Bluetooth echo server using that prints messages
received and send them back through Bluetooth channel.

# Bluetooth Setup
You can use `bluez-simple-agent` to pair your Android device with your
UDOO board. Run the following script:
```
$ sudo bluez-simple-agent
```
After you pair your Android device with your UDOO board, you need to add
the serial port profile
```
$ sudo sdptool add sp
```

# Usage
Run the following command on an UDOO Neo to start RFCOMM server:
```
$ python btserver.py
```