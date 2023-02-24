===========================
Use the IoT Box for the PoS
===========================

.. image:: pos/pos01.png
   :align: center
   :alt: Point of Sale layout diagram.

Prerequisites
=============

Before starting, make sure the following equiptment is available:

-  An IoT Box, with its power adapter.

-  A computer or tablet with an up-to-date web browser

-  An Odoo Online or Odoo instance with the Point of Sale and IoT apps installed or running

-  A local network setup with DHCP (this is the default setting)

-  An RJ45 Ethernet Cable (optional, WiFi is built in)

-  Any of the supported hardware (receipt printer, barcode scanner, cash drawer, payment terminal,
   scale, customer display, etc.). The list of supported hardware can be found on the `POS Hardware
   page <https://www.odoo.com/page/point-of-sale-hardware>`__

SetUp
=====

To connect hardware to the PoS, the first step is to connect an IoT Box to the database. For this,
follow this :doc:`documentation <connect>`.

Then, connect the peripheral devices to the IoT Box.

-  **Printer**: Connect a supported receipt printer to a USB port or to the network and power it on.
   Refer to :ref:`iot/pos_printer`.

-  **Cash drawer**: The cash drawer should be connected to the printer with an RJ25 cable.

-  **Barcode scanner**: Connect the barcode scanner. In order for the barcode scanner to be
   compatible it must end barcodes with an ENTER character (keycode 28). This is most likely the
   default configuration of the barcode scanner.

-  **Scale**: Connect the scale and power it on. Refer to
   :doc:`/applications/productivity/iot/devices/scale`.

-  **Customer Display**: Connect a screen to the IoT Box to display the PoS order. Refer to
   :doc:`/applications/productivity/iot/devices/screen`.

-  **Payment terminal**: The connection process depends on the terminal, refer to the
   :doc:`payment terminals documentation </applications/sales/point_of_sale/payment>`.

Once this is completed, connect the IoT Box to the PoS application. For this, go in
:menuselection:`Point of Sale --> Configuration --> PoS`, tick :guilabel:`IoT Box` and select the
devices to be used in this Point of Sale. Save the changes.

.. image:: pos/pos02.png
   :align: center
   :alt: Configuring the connected devices in the POS application.

Set up is done, a new PoS Session can be launched.
