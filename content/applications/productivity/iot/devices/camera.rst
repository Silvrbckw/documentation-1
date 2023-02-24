================
Connect a Camera
================

A camera can be used when using the :abbr:`IoT (Internet of Things)` Box with an Odoo database. It
can be added in a few easy steps. Then, it can be used in a manufacturing process and it can be
linked to a control point. Doing so will allow for the taking of pictures when a chosen quality
control point has been reached.

Connection
==========

To connect the camera to the :abbr:`IoT (Internet of Things)` Box, simply connect the two by cable.
This is likely a USB cable.

If the camera is a `supported one <https://www.odoo.com/page/iot-hardware>`__, there is no need to
set up anything as it will be detected as soon as it is connected.

.. image:: camera/camera_01.png
   :align: center
   :alt: Camera recognized on the IoT box.

Link a Camera to a quality control point within a manufacturing process
=======================================================================

In the :menuselection:`Quality app`, a device can be setup on a *Quality Control Point*. Go to the
:menuselection:`Control Points --> Quality Control` and open the control point which will be linked
with the camera.

Now, edit the control point and choose the device from the dropdown list. Makes sure the changes are
saved.

.. image:: camera/camera_03.png
   :align: center
   :alt: Setting up the device on the quality control point.

The camera can be used with the selected *Control Point*. When the *Quality Control Point* is
reached during the manufacturing process the database will prompt the operator to take a picture.

.. image:: camera/camera_04.png
   :align: center
   :alt: Graphic user interface of the device on the quality control point.
