PyWiglenet
==========

With *PyWiglenet* you can get the location of an WiFi Access Point using the `Wigle.net <http://wigle.net/>`_ API. The response should give you latitude, longitude, SSID and historical data if the network is found.

You will need a username and password (don't worry, is free) from `Wigle.net <http://wigle.net/>`_.


Install
=======

Clone the repository::

    $ git clone https://github.com/atarantini/pywiglenet

Install dependencies::

    $ pip install -r requirements.txt

Use
===

Import and create an instance of the *Wigle* class with username and password; then query the API using the *query* method:

.. code-block:: python

    >>> from pywiglenet import Wigle
    >>> wigle = Wigle("username", "password")
    >>> print wigle.query_mac("00:14:A5:90:7A:A4")

    [
     {u'bcninterval': None,
      u'channel': u'11',
      u'comment': None,
      u'dhcp': u'?',
      u'discoverer': u'alansc02',
      u'firsttime': u'2012-11-29 12:35:36',
      u'flags': None,
      u'freenet': u'?',
      u'lasttime': u'2013-06-04 03:47:00',
      u'lastupdt': u'2013-06-04 03:50:27',
      u'locationData': [
       {u'accuracy': u'10',
        u'alt': u'55',
        u'lastupdt': u'2012-11-29 11:28:25',
        u'latitude': u'-34.57761383',
        u'longitude': u'-58.50290680',
        u'month': u'201211',
        u'name': None,
        u'netid': u'00:14:A5:90:7A:A4',
        u'noise': None,
        u'signal': u'-82',
        u'snr': None,
        u'ssid': u'FIBERTEL-WIFI',
        u'time': u'2012-11-29 12:35:36',
        u'wep': u'Y'}
      ],
      u'name': None,
      u'netid': u'00:14:A5:90:7A:A4',
      u'paynet': u'?',
      u'qos': u'2',
      u'ssid': u'FIBERTEL-WIFI',
      u'transid': u'20121129-00735',
      u'trilat': u'-34.57771683',
      u'trilong': u'-58.50284195',
      u'type': u'infra',
      u'visible': u'Y',
      u'wep': u'Y'}
    ]

You can find the aproximate location looking at the *trilat* and *trilong* keys.


License
=======

`GPLv3 <http://www.gnu.org/licenses/gpl.html>`_, see COPYNG file.


Author
======

Andres Tarantini (atarantini@gmail.com)