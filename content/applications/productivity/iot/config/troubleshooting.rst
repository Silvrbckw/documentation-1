===============
Troubleshooting
===============

IoT Box Connection
==================

Unable to locate the pairing code to connect the IoT Box
--------------------------------------------------------

The pairing code should be printed on receipt printers connected to the
:abbr:`IoT (Internet of Things)` Box and should also be displayed on connected monitors.

The pairing code doesn't show under the following circumstances:

-  The :abbr:`IoT (Internet of Things)` Box is already connected to an Odoo database;

-  The :abbr:`IoT (Internet of Things)` Box is not connected to the Internet;

-  The code is only valid for 5 minutes after the :abbr:`IoT (Internet of Things)` Box has started.
   It’s automatically removed from connected displays when this delay has expired; from connected
   displays when this delay has expired;

-  The version of the :abbr:`IoT (Internet of Things)` Box image is too old. It should use version
   20.06 or more recent. If the :abbr:`IoT (Internet of Things)` Box image is from an earlier
   version, then the SD card of the :abbr:`IoT (Internet of Things)` Box will need to be re-flashed
   to update the image. (see :doc:`Flashing the SD Card <flash_sdcard>`)

If none of the cases listed above correct the issue, then make sure that the
:abbr:`IoT (Internet of Things)` Box has correctly started, by checking that a fixed green LED is
showing next to the USB-C power port.

IoT Box is connected but it's not showing in the database
---------------------------------------------------------

When an :abbr:`IoT (Internet of Things)` Box connects to a database, the
:abbr:`IoT (Internet of Things)` Box might restart, if that is the case, it might take up to one
minute before appearing in the database. If after some time the :abbr:`IoT (Internet of Things)` is
still not showing, make sure that the database can be reached from the
:abbr:`IoT (Internet of Things)` Box and that the server doesn't use a multi-database environment.

The IoT Box is connected to the Odoo database, but cannot be reached
--------------------------------------------------------------------

Make sure that the :abbr:`IoT (Internet of Things)` Box and the device running the browser are
located on the same network as the :abbr:`IoT (Internet of Things)` Box cannot be reached from
outside the local network.

Printer
=======

The printer is not detected
---------------------------

If one of the printers doesn't show up in the devices list, go to the
:abbr:`IoT (Internet of Things)` Box homepage and make sure that it is listed under
:guilabel:`Printers`.

.. image:: troubleshooting/troubleshooting_printer_01.png
   :align: center
   :alt: The IoT box console landing page.

If the printer is not present on the :abbr:`IoT (Internet of Things)` Box homepage, click
:guilabel:`Printers Server`, go to the :guilabel:`Administration` tab and click on :guilabel:`Add
Printer`. If the printer is not present in the list, it's likely not connected properly.

The printer outputs random text
-------------------------------

For most printers, the correct driver should be automatically detected and selected. However, in
some cases, the automatic detection mechanism might not be enough, and if no driver is found the
printer might print random characters.

The solution is to manually select the corresponding driver. On the :abbr:`IoT (Internet of Things)`
Box homepage, click on :guilabel:`Printers Server`, go to the :guilabel:`Printers` tab and select
the printer in the list. In the Administration dropdown, click on :guilabel:`Modify Printer`.
Follow the steps and select the :guilabel:`Make and Model`` corresponding to the printer.

.. image:: troubleshooting/troubleshooting_printer_02.png
   :align: center
   :alt: Edit the printer connected to the IoT box.

.. note::
   Epson and Star receipt printers and Zebra label printers do not need a driver to work. Make sure
   that no driver is selected for those printers.

The Zebra Printer doesn't print anything
----------------------------------------

Zebra printers are quite sensitive to the format of the ZPL code that is printed. If nothing comes
out of the printer or blank labels are printed, try changing the format of the report that is sent
to the printer by accessing :menuselection:`Settings --> Technical --> Views` in developer mode and
look for the corresponding template.

Barcode Scanner
===============

The characters read by the barcode scanner don't match the barcode
------------------------------------------------------------------

By default, most barcode scanners are configured in the US QWERTY format. If the barcode scanner
uses a different layout, go to the form view of the device and select the correct one.

Nothing happens when a barcode is scanned
-----------------------------------------

Make sure that the correct device is selected in the Point of Sale configuration and that the
barcode is configured to send an ENTER character (keycode 28) at the end of every barcode.

The barcode scanner is detected as a keyboard
---------------------------------------------

Some poorly built barcode scanners do not advertise themselves as barcode scanners but as a USB
keyboard instead, and will not be recognized by the :abbr:`IoT (Internet of Things)` Box.

The device type can be manually changed by going to its form view and activating the
:guilabel:`Is scanner` option.

.. image:: troubleshooting/troubleshooting_barcode_01.png
   :align: center
   :alt: Modifying the form view of the barcode scanner.

Cash drawer
===========

The cash drawer does not open
-----------------------------

The cash drawer should be connected to the printer and the :guilabel:`Cash drawer` checkbox should
be ticked in the POS configuration.
