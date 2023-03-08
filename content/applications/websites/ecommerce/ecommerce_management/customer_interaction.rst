====================
Customer interaction
====================

Odoo offers many ways to interact with customers, and for customers to interact with your website.

.. _product-reviews:

Product reviews
===============

Customers can give a rating to your products. This is a great way to promote your products or
services since product review can influence purchase processes. To activate the **rating** feature,
from your **shop page**, select a product and go to :menuselection:`Edit --> Customize` and enable
:guilabel:`Rating`.

.. note::
   Only portal users who purchased the product can leave rating.

.. tip::
   Customer reviews can be hidden by clicking the :guilabel:`Visible` button next to a published
   review.

.. image:: customer_interaction/interaction-rating.png
   :align: center
   :alt: Rating of a product on the product page

Live chat
=========

A chatbot is available and can simulate a human-like conversation with website visitors via text
messages in a chat box.

.. seealso::
   - :doc:`../../livechat/overview/get_started`
   - :doc:`../../livechat/overview/ratings`
   - :doc:`../../livechat/overview/responses`

'Contact Us' and 'Helpdesk' pages
=================================

Helpdesk
--------

Customers may need support after purchasing a product or subscribing to a service. It is possible to
create a **contact form** page, which, when fulfilled, automatically creates a new ticket for your
**support team**.

.. image:: customer_interaction/interaction-form.png
   :align: center
   :alt: Contact form to submit a ticket to the support team

To add a contact form, **create** a new page (:menuselection:`+ New --> Page`) if necessary, and
drag and drop a :guilabel:`Form` block from the :guilabel:`Dynamic Content` section onto the page.
Once placed, click on the form (while in :guilabel:`Edit` mode), and in the :guilabel:`Action`
field, select :guilabel:`Create a Ticket`. You can then select to which :guilabel:`Helpdesk team`
the ticket should be assigned to.

.. image:: customer_interaction/interaction-ticket.png
   :align: center
   :alt: Action field to create a task upon submitting a form

Contact us
----------

A 'Contact Us' page makes it easier for customers and prospects to contact your company and get in
touch.

To have a 'Contact Us' page, create a new page (:menuselection:`+ New --> Page`) and click on
:menuselection:`Edit --> Customize`. Then, drag and drop a :guilabel:`Form` block onto the page.
Select the form and define the action to be performed when submitted in the :guilabel:`Action`
field.

.. tip::
   If you choose the action :guilabel:`Subscribe to Newsletter`, make sure to add a checkbox in the
   contact form in which visitors agree to be added to a mailing list.

If you want to create new opportunities that could be interested in different services, you can
create a contact form with a *required* :guilabel:`Tag` field, in which visitors select the services
they are interested in.

.. image:: customer_interaction/interaction-tags.png
   :align: center
   :alt: Tags to be selected on the 'Contact Us' form

.. image:: customer_interaction/interaction-checkboxes.png
   :align: center
   :alt: 'Checkboxes' configuration settings

Newsletter
==========

Customers can be updated on your eCommerce activities by subscribing to a newsletter. Visitors
subscribing to the newsletter will automatically be added to the mailing list of the **Email
Marketing** application. You can either choose a newsletter **block**, a newsletter **popup**, or
both.

- **Popup**: prompts up a newsletter box when the visitor scrolls-down the page;
- **Block**: Displays a field on the page where the customer can sign up by entering its email.

The newsletter **block** can be configured according to different :guilabel:`Templates`. To do,
click the **block** while in :menuselection:`Edit --> Customize`, and select a :guilabel:`Template`
in the :guilabel:`Newsletter Block` section. There are **three** templates available:

- :guilabel:`Email Subscription`: visitors can sign up by email to the newsletter, without any
  choice to the content. The content is defined in :menuselection:`Edit --> Customize` in the
  :guilabel:`Newsletter` field;
- :guilabel:`SMS Subscription`: is the same as :guilabel:`Email Subscription`, but by SMS;
- :guilabel:`Form Subscription`: allows to add several fields, as well as a checkbox for the visitor
  to agree to the **GDPR policy** of your website.

.. image:: customer_interaction/interaction-news.png
   :align: center
   :alt: Form subscription configuration and settings
