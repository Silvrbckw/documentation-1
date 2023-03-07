============================================
Process receipts and deliveries in two steps
============================================

Depending on a company's business processes, multiple steps may be needed before receiving or
shipping products. In the two step receipt process, products are received in an input area, then
transferred to stock. An example of using two step receipts is if various storage locations are
being used, such as locked or secured areas, freezers and refrigerators, or various shelves.
Products can be sorted according to where they are going to be stored, and employees can stock all
the products going to a specific location. The products are not available for further processing
until they are transferred into stock.

In the two steps delivery  process, products which are part of a delivery order are picked from the
warehouse according to the removal strategy, and brought to an output location before being shipped.
One situation where this would be useful is when using either a :abbr:`FIFO (First In, First Out)`,
:abbr:`LIFO (Last In, First Out)`, or :abbr:`FEFO (First Expired, First Out)`  removal strategy,
where the products that are being picked need to be selected based on their receipt date or
expiration date.

Odoo is configured by default to :doc:`receive and deliver goods in one step
<receipts_delivery_one_step>`, so the settings need to be changed in order to utilize two-step
receipts and deliveries. Both incoming and outgoing shipments do not need to be set the same steps.
For example products can be received in two steps, but shipped in one step. In the following
example, two steps will be used for both receipts and deliveries.

Configuration
=============

First, make sure the :guilabel:`Multi-Step Routes` option is enabled in :menuselection:`Inventory
--> Configuration --> Settings --> Warehouse`. Note that activating :guilabel:`Multi-Step Routes`
will also activate :guilabel:`Storage Locations`.

.. image:: receipts_delivery_two_steps/multi-step-routes.png
   :align: center
   :alt: Activate multi-step routes and storage locations in inventory settings.

Next, the warehouse needs to be configured for two step receipts and deliveries. Go to
:menuselection:`Inventory --> Configuration --> Warehouses`, edit the warehouse, then, select
:guilabel:`Receive goods in input and then stock (2 steps)` for :guilabel:`Incoming Shipments` and
:guilabel:`Send goods in output and then deliver (2 steps)` for :guilabel:`Outgoing Shipments`, then
:guilabel:`Save` the changes.

.. image:: receipts_delivery_two_steps/two-step-warehouse-config.png
   :align: center
   :alt: Set incoming and outgoing shipment options to receive and deliver in two steps.

Activating two-step receipts and deliveries will create a new :guilabel:`Input` and
:guilabel:`Output` location (:guilabel:`WH/Input, WH/Output`). To rename these locations, go to
:menuselection:`Configuration --> Locations`, select the location to change, click :guilabel:`Edit`,
update the name, and finally, click :guilabel:`Save`.

Process a receipt in two steps (input + stock)
==============================================

Create a purchase order
-----------------------

In the :guilabel:`Purchase` application, create a new quote by clicking :guilabel:`Create`. Select a
vendor, add a storable product, and click :guilabel:`Confirm Order`.

A :guilabel:`Receipt` smart button will appear in the top right, and the receipt will be associated
with the purchase order. Clicking on the :guilabel:`Receipt` smart button will show the receipt
order.

.. image:: receipts_delivery_two_steps/two-step-po-receipt.png
   :align: center
   :alt: After confirming a purchase order, a :guilabel:`Receipt` smart button will appear.

Process a receipt
-----------------

The receipt and internal transfer will be created once the purchase order is confirmed. The status
of the receipt will be :guilabel:`Ready`, since the receipt must be processed first. The status of
the internal transfer will be :guilabel:`Waiting Another Operation`, since the transfer cannot
happen until the receipt is completed. The status of the internal transfer will only change to
:guilabel:`Ready` when the receipt has been marked :guilabel:`Done`.

The receipt can also be found in the :guilabel:`Inventory` application. In the overview dashboard,
click the :guilabel:`1 To Process` smart button in the :guilabel:`Receipts` Kanban card.

.. image:: receipts_delivery_two_steps/two-step-receipts-kanban.png
   :align: center
   :alt: One receipt ready to process in the Inventory Overview Kanban view.

Click on the receipt associated with the purchase order, then click :guilabel:`Validate` to complete
the receipt and move the product to the :guilabel:`Input Location`.

.. image:: receipts_delivery_two_steps/validate-two-step-receipt.png
   :align: center
   :alt: Validate the receipt by clicking Validate, then the product will be transferred to the
         WH/Input location.

Process an internal transfer
----------------------------

Once the product is in the :guilabel:`Input Location`, the internal transfer is ready to move the
product to :guilabel:`Stock`. In the inventory overview dashboard, click the :guilabel:`1 To
Process` smart button in the :guilabel:`Internal Transfers` Kanban card.

.. image:: receipts_delivery_two_steps/transfer-two-step-kanban.png
   :align: center
   :alt: One Internal Transfer ready to process in the Inventory Overview Kanban view.

Click on the transfer associated with the purchase order, then click :guilabel:`Validate` to
complete the receipt and move the product to :guilabel:`Stock`. Once the transfer is validated, the
product enters the stock and is available for customer deliveries or manufacturing orders.

.. image:: receipts_delivery_two_steps/two-step-validate-transfer.png
   :align: center
   :alt: Validate the internal transfer to move the item to stock.

Process a delivery order in two steps (pick + ship)
===================================================

Create a sales order
--------------------

In the :guilabel:`Sales` application, create a new quote by clicking :guilabel:`Create`. Select a
customer, add a storable product, and click :guilabel:`Confirm`.

A :guilabel:`Delivery` smart button will appear in the top right. Clicking on the
:guilabel:`Delivery` smart button will show both the picking order and delivery order, which are
both associated with the sales order.

.. image:: receipts_delivery_two_steps/two-step-sales-quote.png
   :align: center
   :alt: After confirming the sales order, the Delivery smart button appears showing two items
         associated with it.

Process a picking
-----------------

The picking and delivery order will be created once the sales order is confirmed. The status of the
picking will be :guilabel:`Ready`, since the product must be picked from stock before it can be
shipped. The status of the delivery order will be :guilabel:`Waiting Another Operation`, since the
delivery cannot happen until the picking is completed. The status of the delivery order will only
change to :guilabel:`Ready` when the picking has been marked :guilabel:`Done`.

.. image:: receipts_delivery_two_steps/two-step-status.png
   :align: center
   :alt: Ready status for the pick operation while the delivery operation is Waiting Another
         Operation.

The receipt can also be found in the :guilabel:`Inventory` application. In the overview dashboard,
click the :guilabel:`1 To Process` smart button in the :guilabel:`Pick` Kanban card.

.. image:: receipts_delivery_two_steps/two-step-pick-kanban.png
   :align: center
   :alt: The pick order can be seen in the Inventory Kanban view.

Click on the picking to process. If the product is in stock, Odoo will automatically reserve the
product. Click :guilabel:`Validate` to mark the picking as :guilabel:`Done`, then the delivery order
will be ready to be processed. Since the documents are linked, the products which have been
previously picked are automatically reserved on the delivery order.

.. image:: receipts_delivery_two_steps/validate-two-step-pick.png
   :align: center
   :alt: Validate the picking by clicking Validate.

Process a delivery
------------------

The delivery order will be ready to be processed once the picking is completed, and can be found in
the :guilabel:`Inventory` application overview dashboard. Click the :guilabel:`1 To Process` smart
button in the :guilabel:`Delivery Orders` Kanban card.

.. image:: receipts_delivery_two_steps/deliver-two-step-kanban.png
   :align: center
   :alt: The delivery order can be seen in the Inventory Kanban view.

Click on the delivery order associated with the sales order, then click on :guilabel:`Validate` to
complete the move.

.. image:: receipts_delivery_two_steps/validate-two-step-delivery.png
   :align: center
   :alt: Click Validate on the delivery order to transfer the product from the output location to the
         customer location.

Once the delivery order is validated, the product leaves the :guilabel:`WH/Output` location and
moves to the :guilabel:`Partners/Customers` location. Then, the status of the document will change
to :guilabel:`Done`.
