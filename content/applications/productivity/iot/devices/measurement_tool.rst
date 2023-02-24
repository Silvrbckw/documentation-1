==========================
Connect a Measurement Tool
==========================

With Odoo's *IoT Box*, it is possible to connect measurement tools to the Odoo database. Find the
list of supported devices here: `Supported devices <https://www.odoo.com/page/iot-hardware>`__

Connect in USB
==============

To add a device connected by USB, just plug the USB cable in the *IoT Box*, and the device should
appear in the Odoo database.

.. image:: measurement_tool/measurement_tool_01.png
   :align: center
   :alt: Measurement tool recognized on the IoT box.

Connect in Bluetooth
====================

Activate the Bluetooth on the device (see the device manual for further explanation) and the IoT
Box will automatically try to connect to the device.

Here is an example of what it should look like:

.. image:: measurement_tool/measurement_tool_03.png
   :align: center
   :alt: Bluetooth indicator on measurement tool.

Link a measurement tool to a quality control point within a manufacturing process
=================================================================================

In the :menuselection:`Quality app`, a device can be setup on a *Quality Control Point*. Go to the
:menuselection:`Control Points --> Quality Control` and open the control point which will be linked
with the measurement tool.

Now, edit the control point and choose the device from the dropdown list. The changes will
automatically save when navigating away from the page with the changes.

.. image:: measurement_tool/measurement_tool_04.png
   :align: center
   :alt: Setting up the device on the quality control point.

Now, the measurement tool is linked to the chosen *Control Point*. The value, which usually needs to
be changed manually, will be automatically updated while the tool is being used.

.. image:: measurement_tool/measurement_tool_05.png
   :align: center
   :alt: Measurement tool input in the Odoo database.
