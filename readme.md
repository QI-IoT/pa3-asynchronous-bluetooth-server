# Introduction

Build an asynchronous Bluetooth echo server using that prints messages
received and send them back through Bluetooth channel.

# Required Python Modules

The required modules are

1.  PyBluez

They can be installed with the following command:
```
$ sudo pip install -r requirements.txt
```
If you encounter errors during the installation, please refer to FAQ
section.

# Bluetooth Setup
First, you need to put your Bluetooth adapter in discoverable mode with
```
$ sudo hciconfig hci0 piscan
```
The default device name is `udoo-0`. To customize your Bluetooth device
name, please refer to FAQ section.

You can then use `bluez-simple-agent` to pair your Android device with
your UDOO board. Run the following script:
```
$ sudo bluez-simple-agent
```
You only need to pair UDOO board with your Android phone once. Once they
are paired, you can skip this step in the future. After you pair your
Android device with your UDOO board, you need to add the serial port
profile
```
$ sudo sdptool add sp
```

# Usage
Run the following command on an UDOO Neo to start RFCOMM server:
```
$ python btserver.py
```

# FAQ
* Why `pip` cannot verify server's certificates?

   This might happen if your system time is not properly synced. You may
   first check your system time with `date` command. If so, then use
   ```
   $ sudo service ntp stop
   $ sudo ntpdate -u time.nist.gov
   $ sudo service ntp start
   ```
   To sync your system time with an NTP server. If unfortunately, this
   still does not work, you will need to set your system time manually
   with
   ```
   $ sudo date MMDDhhmmyyyy[.ss]
   ```

* How to customize Bluetooth broadcast name?

   The default broadcast name of UDOO Neo board is `udoo-0`, if you want
   to customize its name, create a `machine-info` file in `/etc` folder,
   and add `PRETTY_HOSTNAME=device-name`. After that, restart your
   Bluetooth service with
   ```
   $ sudo service bluetooth restart
   ```