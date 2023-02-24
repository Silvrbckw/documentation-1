====================
Connect a Footswitch
====================

When working, it is always better for an operator to have two hands available. Odoo's
:abbr:`IoT (Internet of Things)` Box makes this possible when using a footswitch.

In fact, the operator will be able to go from one screen to another and perform actions by using
their foot and the footswitch. This is very convenient, and it can be configured in just a few
steps.

Connection
==========

Connecting the footswitch to the :abbr:`IoT (Internet of Things)` Box is easy, just connect the two
by cable. More often than not this is a USB cable.

If the footswitch is a `supported device <https://www.odoo.com/page/iot-hardware>`__, there is no
need to set up anything since it will be automatically detected when connected.

.. image:: footswitch/footswitch_01.png
   :align: center
   :alt: Footswitch recognized on the IoT box.

Link a Footswitch to a Workcenter in the Manufacturing App
==========================================================

To link the footswitch to an action, it needs to be configured on a workcenter. Go to the workcenter
the footswitch will be used in and add the device in the :guilabel:`IoT Triggers` tab. Then, it can
be linked it to an action and a key can be added to trigger it.

.. image:: footswitch/footswitch_03.png
   :align: center
   :alt: Setting the IoT trigger for the footswitch.

It should be noted that the trigger that is first in the list will be chosen first. So, the
order matters and these triggers can be dragged into order. In the picture above, using the
footswitch will automatically skip the current part of the process currently being worked on.

.. note::
   On the work order screen, a status graphic indicates whether the database is correctly connected
   to the footswitch.
