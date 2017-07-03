python-adb
==========
[![Coverage Status][coverage_img]][coverage_link]
[![Build Status][build_img]][build_link]

This repository contains a pure-python implementation of the ADB and Fastboot
protocols, using libusb1 for USB communications.

This is a complete replacement and rearchitecture of the Android project's [ADB
and fastboot code](https://github.com/android/platform_system_core/tree/master/adb)

This code is mainly targeted to users that need to communicate with Android
devices in an automated fashion, such as in automated testing. It does not have
a daemon between the client and the device, and therefore does not support
multiple simultaneous commands to the same device. It does support any number of
devices and _never_ communicates with a device that it wasn't intended to,
unlike the Android project's ADB.

### Using with Emulator
This is a stripped down version of the upstream repo with USBHandler 
and signing removed.  Only support for TCPHandle remains.  The additional 
dependencies are also removed making it easier to install on Windows environment.

It is meant to be used with AmiDUOS emulator Lollipop version.

```python

from adb.adb_commands import AdbCommands

device = AdbCommands.ConnectDevice(serial='localhost:5565')
device.Shell('echo 1')
device.Shell('screencap -p')
```


### History

#### 1.0.0

 * Initial version

#### 1.1.0

 * Added TcpHandle (jameyhicks)
 * Various timing and other changes (alusco)


[coverage_img]: https://coveralls.io/repos/github/google/python-adb/badge.svg?branch=master
[coverage_link]: https://coveralls.io/github/google/python-adb?branch=master
[build_img]: https://travis-ci.org/google/python-adb.svg?branch=master
[build_link]: https://travis-ci.org/google/python-adb
[pycon_preso]: https://docs.google.com/presentation/d/1bv8pmm8TZp4aFxoq2ohA-ms_a3BWci7D3tYvVGIm8T0/pub?start=false&loop=false&delayms=10000
