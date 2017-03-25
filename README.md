## Pytest Demo

This repository contains the code I demonstrated during my presentation at the January meeting of the [Austin Python Meetup](http://www.meetup.com/austinpython/events/205376942/).

Python 3 is required to run this code! To run, create a virtualenv and install the dependencies (the instructions assume Python 3 is installed and is your main Python):

```
pyvenv /path/to/my/env
source /path/to/my/env/bin/activate
pip install -r requirements.txt

# run the tests
py.test -v
```

The commit history in this repository mostly mirrors the sequence of changes I described in the [presentation slides](https://www.slideshare.net/ereyes01/tdd-in-python-with-pytest-43671276?qid=03b75440-686e-4aef-bf6b-4ffba28d751b&v=&b=&from_search=4).
