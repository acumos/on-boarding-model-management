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

=======================================
Model Management Python Developer Guide
=======================================


Setting up a Local Environment
==============================

You will need at least a Python 3.5+ environment in order to run this
application. This application uses Flask and Flask-RESTPlus as it's web service
frameworks. To develop this service, a virtualenv is highly recommended and can
be created and activated via the following commands:

.. code:: bash
  $ python3 -m venv venv
  $ source venv/bin/activate


To install the requirements needed for local development:

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

You can view available command line arguments via the following command:

.. code:: bash

    $ ./run.py -h


Alternatively the application can be bundled with a production-grade WSGI
server, such as Gunicorn. An example of running gunicorn:

.. conde:: bash

    $ gunicorn --workers=4 wsgi


Testing
=======

We use a combination of ``tox``, ``pytest``, and ``flake8`` to test
``acumos_model_management``. Code which is not PEP8-compliant, with an exception
for line length increased to 120 characters, considered a failing test.
Furthermore, code which fails pyflakes and pycode style is also considered
failing. Example tool usage is below:

.. code:: bash

    $ pip install autopep8 pyflakes pycodestyle
    $ cd model-management
    $ autopep8 -r --in-place acumo_model_management


Run tox directly:

.. code:: bash

    $ cd model-management
    $ tox

You can also specify certain tox environments to test:

.. code:: bash

    $ tox -e py35  # only test against Python 3.5
    $ tox -e flake8  # only lint code

And finally, you can run pytest directly in your environment *(recommended starting place)*:

.. code:: bash

    $ pytest
    $ pytest -s   # verbose output
