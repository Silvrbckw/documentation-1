===================================================================
Choosing the right inventory flow to handle receipts and deliveries
===================================================================

There are several ways to handle how a warehouse receives products (receipts) and ships products
(deliveries). Depending on factors such as the type of products stocked and sold, warehouse size,
and the amount of daily confirmed receipts and delivery orders, the way products are handled when
coming in and out of the warehouse can vary a lot. Different settings can be configured for receipts
and deliveries; they do not have to be configured to have the same number of steps.

Odoo handles shipping and receiving in 3 different ways, in one, two, or three steps. The simplest
configuration is one step, which is the default. Each additional step required for a warehouse for
either the receiving or shipping process will add an additional layer of operations to perform
before a product is either received or shipped. These configurations depend entirely on the
requirements for the products stored, such as performing quality checks on received products, or
using special packaging on shipped products.

One step flow
=============

**Receipt**: Receive products directly into stock. No intermediate steps between receipt and stock
occur, such as a transfer to a quality location.

**Shipping**: Ship products directly from stock.  No intermediate steps between stock and shipping
occur, such as a transfer to a packing location.

- Can only be used if not using :abbr:`FIFO (First In, First Out)`, :abbr:`LIFO (Last In, First
  Out)`, or :abbr:`FEFO (First Expired, First Out)` removal strategies.
- Configuration is easy; it is the default configuration in Odoo.
- Receipts and/or deliveries are handled quickly.
- Recommended for small warehouses with low stock levels, and for non-perishable items.
- Items are received or shipped directly into/from stock.

.. seealso::
   - :doc:`receipts_delivery_one_step`

Two step flow
=============

**Input + stock**: Bring products to an input location before moving into stock. Products can be
organized by different internal storage locations, such as various shelves, freezers, and locked
areas, before being stocked in the warehouse.

**Pick + ship**: Bring products to an output location before shipping. Packages can be organized by
different carriers or shipping docks before being shipped.

- Minimum requirement for tracking products by lot or serial numbers with a :abbr:`FIFO (First In,
  First Out)`, :abbr:`LIFO (Last In, First Out)` and :abbr:`FEFO (First Expired, First Out)` removal
  strategy.
- Recommended for larger warehouses with high stock levels, or when stocking large items (such as
  mattresses, large furniture, heavy machinery, etc.).
- Products received will not be available for manufacturing, shipping, etc., until they are
  transferred into stock.

.. seealso::
   - :doc:`receipts_delivery_two_steps`

Three step flow
===============

**Input + quality + stock**: Receive products at the input location, then transfer to a quality
control area, and finally, the products that pass inspection are moved into stock.

**Pick + pack + ship**: Pick products according to the removal strategy, then create packages in a
dedicated packing area, and finally, bring them to an output location for shipping.

- Can be used when tracking products by lot or serial numbers when using a :abbr:`FIFO (First In,
  First Out)`, :abbr:`LIFO (Last In, First Out)`, or :abbr:`FEFO (First Expired, First Out)` removal
  strategy.
- Recommended for very large warehouses with very high stock levels.
- Required for any warehouse needing to perform quality control inspections before receiving items
  into stock.
- Products received will not be available for manufacturing, shipping, etc., until they are
  transferred into stock.

.. seealso::
   - :doc:`delivery_three_steps`
   - :doc:`receipts_three_steps`
