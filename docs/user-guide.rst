.. ===============LICENSE_START=======================================================
.. Acumos CC-BY-4.0
.. ===================================================================================
.. Copyright (C) 2018 AT&T Intellectual Property. All rights reserved.
.. ===================================================================================
.. This Acumos documentation file is distributed by AT&T
.. under the Creative Commons Attribution 4.0 International License (the "License");
.. you may not use this file except in compliance with the License.
.. You may obtain a copy of the License at
..
..      http://creativecommons.org/licenses/by/4.0
..
.. This file is distributed on an "AS IS" BASIS,
.. WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
.. See the License for the specific language governing permissions and
.. limitations under the License.
.. ===============LICENSE_END=========================================================

==================================
Model Management User Guide
==================================

|Build Status|

.. |Build Status| image:: https://jenkins.acumos.org/buildStatus/icon?job=on-boarding-model-management-tox-verify-master
   :target: https://jenkins.acumos.org/job/on-boarding-model-management-tox-verify-master/

Requirements
===========

You will need at least a Python 3.5+ environment in order to run this
application.


Installation
============

This package may be installed with:

.. code:: bash

   $ python3 setup.py install


Running the Application
=======================

To run this microservice locally, you must first copy the
properties/settings.cfg.sample to properties/setting.cfg. You will then need to
configure the properties/settings.cfg file  You may run the application in
development mode using:

.. code:: bash

    $ ./run.py


Alternatively the application can be bundled with a production-grade WSGI
server, such as Gunicorn. An example of running gunicorn:

.. conde:: bash

    $ gunicorn --workers=4 wsgi


RESTFUL Endpoints
================

Once the application is running, the swagger spec can be accessed at the /v2
path. For example: http://localhost:8081/v2/
