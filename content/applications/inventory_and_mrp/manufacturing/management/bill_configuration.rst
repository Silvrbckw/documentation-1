================================
Create a Bill of Materials (BoM)
================================

A *Bill of Materials* (or *BoM*) is a document that defines the quantity of each component required
to manufacture (or deliver) a finished product. It can also include various operations types,
steps, and instructions for the individual guidelines needed to complete a production process.

In Odoo Manufacturing, multiple :abbr:`BoMs (Bills of Materials)` can be linked to a product, so
even product variants can have their own specific :abbr:`BoMs (Bills of Materials)`.

Correctly setting up a :abbr:`BoM (Bill of Materials)` helps optimize the manufacturing process,
and saves time.

Set up a Bill of Materials (BoM)
================================

:abbr:`BoMs (Bills of Materials)` can be set up with (or without) operations steps or instructions.
They can include as many (or as few) components, as needed. The simplest setup is one without
operations (or instructions). In that case, the production is solely managed with *Manufacturing
Orders*.

To create a :abbr:`BoM (Bill of Materials)`, navigate to :menuselection:`Manufacturing -->
Products --> Bills of Materials`, and click :guilabel:`Create`. Then, in the :guilabel:`Product`
field, choose the product that will be associated with the :abbr:`BoM (Bill of Materials)`.

.. image:: bill_configuration/bill-configuration-bom-creation.png
   :align: center
   :alt: Bill of materials creation screen.

There are three :guilabel:`BoM Types` that can be chosen for any Bill of Materials:

- :guilabel:`Manufacture this product` indicates that this product is manufactured in-house, from
  start to finish using the components listed on the :abbr:`BoM (Bill of Materials)`.
- :guilabel:`Kits` are sets of unassembled components that may be sold as products, and are useful
  for managing more complex :abbr:`BoMs (Bills of Materials)`.
- :guilabel:`Subcontracting` outsources the production of some (or all) components or products to
  outside manufacturers. This feature needs to be enabled in :menuselection:`Manufacturing -->
  Configuration --> Settings`, under the :guilabel:`Operations` section.

.. note::
    A :abbr:`BoM (Bill of Materials)` can also be created directly from the
    :abbr:`BoM (Bill of Materials)` :guilabel:`Smart Button` on the product template, in which case
    the :guilabel:`Product` field is pre-filled.

The most common :guilabel:`BoM Type` is :guilabel:`Manufacture this product`. Once the
:guilabel:`BoM Type` is chosen, click :guilabel:`Add a Line` to add all the :guilabel:`Components`
that go into the production of the final product, as well as the :guilabel:`Quantity` of each
component. Finally, click :guilabel:`Save` to finish creating the :abbr:`BoM (Bill of Materials)`.

.. tip::
    New components can be created on-the-fly directly from the :abbr:`BoM (Bill of Materials)`.
    After selecting :guilabel:`Add a line`, create the new component and select :guilabel:`Create`
    or :guilabel:`Create and Edit`. Components can also be created by going to
    :menuselection:`Manufacturing --> Products --> Products`, and clicking :guilabel:`Create`.

Specify a Bill of Materials (BoM) for a product variant
-------------------------------------------------------

:abbr:`BoMs (Bills of Materials)` can also be assigned to specific *Product Variants*, with two
setup options available to choose from.

.. image:: bill_configuration/bill-configuration-product-variants.png
   :align: center
   :alt: Bill of materials product variants and apply on variants options.

The first method is to create one :abbr:`BoM (Bill of Materials)` per *Product Variant*, by
specifying the :guilabel:`Product Variant` every time a new :abbr:`BoM (Bill of Materials)` is
created. The second method is to create *one* master :abbr:`BoM (Bill of Materials)` that contains
all components, and specify which variant each component applies to in the
:guilabel:`Apply on Variants` column.

.. note::
   The :guilabel:`Apply on Variants` column in hidden by default and can be accessed by clicking on
   the :guilabel:`Additional Options` menu icon at the right of the :guilabel:`Components` tab.

.. important::
    To assign *Product Variants* to :abbr:`BoMs (Bills of Materials)`, the feature must be enabled
    in :menuselection:`Inventory --> Configuration --> Settings`, under the :guilabel:`Products`
    section by selecting :guilabel:`Variants` and clicking :guilabel:`Save`.

Set up operations steps
=======================

Some :abbr:`BoMs (Bills of Materials)` require multiple operations and steps during the
manufacturing process. To create :guilabel:`Operations` on a :abbr:`BoM (Bill of Materials)`, first
enable the :guilabel:`Work Orders` feature in :menuselection:`Manufacturing --> Configuration -->
Settings --> Operations`.

.. image:: bill_configuration/bill-configuration-create-operation.png
   :align: center
   :alt: An example of a Bill of Materials operation and the steps creation tab.

When creating a new :abbr:`BoM (Bill of Materials)`, click the :guilabel:`Operations` tab and click
:guilabel:`Add a line` to add a new operation. In the :guilabel:`Create Operations` box, give the
operation a name, specify the :guilabel:`Work Center` and the :guilabel:`Default Duration`
settings. Under the :guilabel:`Work Sheet` tab, the type of :guilabel:`Work Sheet` can also be
chosen, if assembly instructions need to be attached.

The :guilabel:`Work Sheet` types that can be added are: :guilabel:`Text` (with a
:guilabel:`Description`); :guilabel:`PDF` files; and :guilabel:`Google Slide` presentations. When
all the information has been filled out, select :guilabel:`Save & Close`.

.. image:: bill_configuration/bill-configuration-operations-popup.png
   :align: center
   :alt: Bill of materials create operations popup on operations tab.

Add by-products to a Bill of Materials (BoM)
============================================

A *By-Product* is a residual product that is created during production of a
:abbr:`BoM (Bill of Materials)`. Unlike the finished product, there can be more than one by-product
on a :abbr:`BoM (Bill of Materials)`.

To add by-products to a :abbr:`BoM (Bill of Materials)`, first enable the :guilabel:`By-Products`
feature in :menuselection:`Manufacturing --> Configuration --> Settings --> Operations`.

Once the feature is enabled, by-products can be added to a :abbr:`BoM (Bill of Materials)` from the
:guilabel:`By-products` tab by clicking :guilabel:`Add a line`. The by-product can be named, its
:guilabel:`Quantity` specified, and a :guilabel:`Unit of Measure` chosen. If the
:abbr:`BoM (Bill of Materials)` has :guilabel:`Operations` steps, specify exactly which operation
the by-product is produced from in the :guilabel:`Produced in Operation` field. Finally, click
:guilabel:`Save`.

.. seealso::
    - :doc:`kit_shipping`
    - :doc:`product_variants`
    - :doc:`routing_kit_bom`
