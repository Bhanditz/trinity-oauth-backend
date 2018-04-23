Trinity OAuth 2 Backend
=============================

|travis-badge|

Overview
--------

A Python Social Auth backend for Texas Gateway (Trinity), mostly used for Open edX but can be used elsewhere.

License
-------

The code in this repository is licensed under the MIT License unless
otherwise noted.

Please see ``LICENSE.txt`` for details.

The Backend Dependency on Python Social Auth
--------------------------------------------

The backend depends on Python Social Auth. It is compatible with both of the
`legacy monolithic Python Social Auth
<https://github.com/omab/python-social-auth>`_
that is being used on Ficus and previous releases,
and the
`new split Python Social Auth
<https://github.com/python-social-auth/>`_
that is being used on Ginkgo and upcoming releases.

SSO Endpoints
-------------
The backend consumes the following URLs:

-  **Registration:** ``https://pass.texasgateway.org/register``
-  **Login:** ``https://pass.texasgateway.org/oauth/v2/auth/login``
-  ``AUTHORIZATION_URL``:
   ``https://pass.texasgateway.org/oauth/v2/auth``
-  ``ACCESS_TOKEN_URL``:
   ``https://pass.texasgateway.org/oauth/v2/token``

When using the ``staging`` environment (see below), the domain
``pass-staging.texasgateway.org`` is used instead.

The OAuth server provides the following information about the user:

- ``email``
- ``username``
- ``fullname``
- ``district``

Backend Extra Settings
----------------------
In addition to the usual client, secret key and other settings.
This backend requires the ``ENVIRONMENT`` configuration:


::

  SOCIAL_AUTH_TRINITY_ENVIRONMENT = 'staging'  # or 'production'

In Open edX, this is usually set via the admin panel in the backend's **Other Settings** field:

::

  { "ENVIRONMENT": "staging" }

Reporting Security Issues
-------------------------

Please do not report security issues in public. Please email security@appsembler.org.

.. |travis-badge| image:: https://travis-ci.org/appsembler/trinity-oauth-backend.svg?branch=master
    :target: https://travis-ci.org/appsembler/trinity-oauth-backend
    :alt: Travis
