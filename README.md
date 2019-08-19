# vcrtoy-aio
toy repo to reproduce vcrpy issue #475

# Installation

just make a venv and install the requirements:

    $ python -m venv venv
    $ pip install -r requirements.txt

# Usage

The script is set up to remove any cassette files, do a run with two requests to record a file, then do another run to compare the real run results to the recorded run results. The results are printed as well as compared (by header). Just running it in the environment should be enough to demonstrate the issue:

    $ venv/bin/python demo.py
