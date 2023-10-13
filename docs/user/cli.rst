.. _cli:

Command-line interface (CLI)
=============================


Directory scan:

.. code:: bash

    $ direnumerate Ds -t "testphp.vulnweb.com" -w wordlist.txt

Port scan:

.. code:: bash

    $ direnumerate Ps -t 44.228.249.3 -p 22 80 443

Finds patterns in logs:

.. code:: bash

    $ direnumerate Fp -log test.log -key ERROR

Ip info:

.. code:: bash

    $ direnumerate info -t 8.8.8.8


To list all command line options, simply type

.. code:: bash

    $ direnumerate -h


Finally, if you're filing a bug report, the cli contains a switch called
``--build-playback-report``, which bundles up the state, allowing others
to easily replay your issue.
