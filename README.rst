Foswiki - Enterprise Wiki Platform
==================================

`Foswiki`_ is a structured wiki, typically used to run a collaboration
platform, knowledge or document management system, a knowledge base, or
team portal. Users can create wiki applications using the Foswiki Markup
Language, and developers can extend its functionality with plugins.

This appliance includes all the standard features in `TurnKey Core`_,
and on top of that:

- Foswiki configurations:
   
   - Installed from upstream source code to /var/www/foswiki.
   - Configured cron jobs (daily maintenance, hourly stats, 15min
     notifications).
   - Preconfigured mail settings.

- SSL support out of the box.
- Postfix MTA (bound to localhost) to allow sending of email (e.g.,
  password recovery).
- Webmin modules for configuring Apache2 and Postfix.

WebMasterEmail is configured in */etc/foswiki/LocalSite.cfg*

Credentials *(passwords set at first boot)*
-------------------------------------------

-  Webmin, Webshell, SSH: username **root**
-  Foswiki: username **AdminUser**

.. _Foswiki: http://foswiki.org
.. _TurnKey Core: https://www.turnkeylinux.org/core
