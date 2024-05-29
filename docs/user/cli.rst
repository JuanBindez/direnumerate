.. _cli:

Command-line interface (CLI)
=============================


Directory scan:

.. code:: bash

    $ direnumerate -t "testphp.vulnweb.com" -w wordlist.txt

Directory scan with all outputs verbose, (-v command):

.. code:: bash

    $ direnumerate -v -t "testphp.vulnweb.com" -w wordlist.txt

Port scan:

.. code:: bash

    $ direnumerate -t 44.228.249.3 -p 22 80 443

Finds patterns in logs:

.. code:: bash

    $ direnumerate -log test.log -key ERROR

Ip info:

.. code:: bash

    $ direnumerate -i 8.8.8.8


To list all command line options, simply type

.. code:: bash

    $ direnumerate -h


Finally, if you're filing a bug report, the cli contains a switch called
``--build-playback-report``, which bundles up the state, allowing others
to easily replay your issue.
