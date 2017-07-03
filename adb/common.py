# Copyright 2014 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Common code for ADB and Fastboot.

Common usb browsing, and usb communication.
"""
import logging
import socket
import threading
import weakref


from adb import usb_exceptions

DEFAULT_TIMEOUT_MS = 1000

_LOG = logging.getLogger('android_usb')


def GetInterface(setting):
  """Get the class, subclass, and protocol for the given USB setting."""
  return (setting.getClass(), setting.getSubClass(), setting.getProtocol())


def InterfaceMatcher(clazz, subclass, protocol):
  """Returns a matcher that returns the setting with the given interface."""
  interface = (clazz, subclass, protocol)
  def Matcher(device):
    for setting in device.iterSettings():
      if GetInterface(setting) == interface:
        return setting
  return Matcher

class TcpHandle(object):
  """TCP connection object.

     Provides same interface as UsbHandle but ignores timeout."""

  def __init__(self, serial):
    """Initialize the TCP Handle.
    Arguments:
      serial: Android device serial of the form host or host:port.

    Host may be an IP address or a host name.
    """
    if ':' in serial:
      (host, port) = serial.split(':')
    else:
      host = serial
      port = 5555
    self._serial_number = '%s:%s' % (host, port)

    self._connection = socket.create_connection((host, port))

  @property
  def serial_number(self):
    return self._serial_number

  def BulkWrite(self, data, timeout=None):
      return self._connection.sendall(data)

  def BulkRead(self, numbytes, timeout=None):
      return self._connection.recv(numbytes)

  def Timeout(self, timeout_ms):
      return timeout_ms

  def Close(self):
      return self._connection.close()
