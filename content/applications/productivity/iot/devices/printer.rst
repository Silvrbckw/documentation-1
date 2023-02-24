=================
Connect a printer
=================

A printer can be attached to the *IoT Box* in a Odoo database. Installation is easy and convenient
and can be done in a few easy steps. The printer can used to print receipts, orders or even reports
from the different Odoo apps.

Connection
==========

The IoT Box supports printers connected through USB, network or Bluetooth. `Supported printers
<https://www.odoo.com/page/iot-hardware>`__ will be detected automatically and will appear in the
:guilabel:`Devices` list of the IoT app.

.. note::
         The printer can take up to two minutes to appear in the IoT app devices list.

.. image:: printer/printer_01.png
   :align: center
   :alt: The printer as it would appear in the IoT app devices list.

Link the printer
================

To work orders
--------------

*Work Orders* can be linked to printers via a *Quality Control Point* to print labels for
manufactured products.

To do so, a *Quality Control Point* needs to be created within the *Quality* app. Afterwards the
correct manufacturing operation and work order operation can be selected. In type, choose
:guilabel:`Print Label`. The changes will automatically save once navigating away from the page the
changes were made on.

.. image:: printer/printer_03.png
   :align: center
   :alt: This is the quality control point setup.

Now, each time the quality control point is reached for the chosen product, a *Print Label* button
will appear.

.. image:: printer/printer_04.png
   :align: center
   :alt: The print label icon that populates once the quality control point is reached.

To reports
----------

It's also possible to link a type of report to a certain printer. In the :menuselection:`IoT` app,
go to the :guilabel:`Devices` menu and select the printer that needs to be configured.

.. image:: printer/printer_05.png
   :align: center
   :alt: The printer devices listed in the IoT Devices menu.

Now, go to the *Printer Reports* tab.

.. image:: printer/printer_06.png
   :align: center
   :alt: Printer configuration on the IoT devices list.

Click edit and then, select :guilabel:`Add a line`. In the window that appears, check all the types
of reports that should be linked to this printer.

.. image:: printer/printer_07.png
   :align: center
   :alt: Report types to be added onto the printer configuration.

Now, each time :guilabel:`Print` is selected in the control panel, instead of downloading a PDF,
Odoo will send the report to the selected printer and automatically print it.

.. _iot/pos_printer:

Print receipts from the PoS
---------------------------

A printer can be linked to the :menuselection:`Point of Sale` app so that receipts can be printed
directly from the :guilabel:`PoS`.

Set up is simple and can be completed in just a few easy steps. Go to the
:menuselection:`Point of Sale` app and open the :guilabel:`Point of Sale` settings, under
:guilabel:`Configuration`. Select the :guilabel:`IoT Box` feature. Then, choose the
:guilabel:`Receipt Printer` from the dropdown. Save the settings.

.. image:: printer/printer_08.png
   :align: center
   :alt: IoT box configuration in the Point of Sale app.

Now, different kinds of tickets can be printed from the :guilabel:`PoS` including **receipts**,
**sale details** and **bills**.

Receipts are printed once the order is validated. The process is automated when the
feature is enabled in the :guilabel:`PoS configuration`.

Sales details can be printed by clicking on the printer icon on the navbar at the top of the
:guilabel:`PoS`. It will print the details of the sales of the current day.

.. image:: printer/printer_09.png
   :align: center
   :alt: Printer icon in the navbar of the POS.

As for the bill, it is only available in restaurant mode. In the restaurant settings, activate
:guilabel:`Print Bills` and a :guilabel:`Bill` button will appear in the left panel of the
:guilabel:`PoS`.

.. image:: printer/printer_10.png
   :align: center
   :alt: This is the Bill button as it appears in restaurant mode.

Print orders in the kitchen
---------------------------

In restaurant mode, order tickets can be sent to the kitchen.

To do so, go to the :menuselection:`PoS` app and open the :guilabel:`PoS` settings. Then, tick
:guilabel:`Order Printer`.

.. image:: printer/printer_11.png
   :align: center
   :alt: Order printer configuration in the POS settings.

Now, go to the :guilabel:`Printers` menu. click on create, select the printer from the dropdown and,
in the :guilabel:`Printer Product Categories` field, choose all the categories of products that
should be printed on this printer.

.. image:: printer/printer_12.png
   :align: center
   :alt: Printer configuration for specific product categories.

In the :guilabel:`PoS`, when a product is added or removed from one of the selected categories, the
:guilabel:`Order` button will be green. If clicked on, the IoT Box will print a receipt on the
corresponding printer.
