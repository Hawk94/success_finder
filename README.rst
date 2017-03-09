Django Zoo
===========

OOP Practice + Django
----------------------

Installation Instructions
-------------------------

1. Clone the repository and create a virtual environment for the project, using Python 3.4:

   .. code:: bash

      mkvirtualenv --python=/usr/local/bin/python3.4 django-zoo

2. Install the pip requirements.

   .. code:: bash

    cd django-zoo
    pip install -r requirements.txt

4. Run the database migrations.

   .. code:: bash

       python manage.py migrate


Zoo Game
--------

1.  You are a zoo keeper. Write a set of objects in a language of your choice that simulates a simple zoo.
    You should be able to do the following using the language's command line console:​
    Create different cages in the zoo.  At any time, you should be able to find out how many cages are in the zoo.
    Put different animals in the cages. Each animal should be of a particular species (e.g. 'Lion'), and have a name given to them by the zookeeper (e.g. 'Growler').
    Find out which animals are in a particular cage.
    Some species of animals like eating other species of animals.  For example, lions like eating wildebeest.  If you put prey and predator in the same cage, then all the prey should be eaten by the predator.  (The program should tell you which predator ate which prey.)


Bonus task
----------
2.  Each cage needs a reference number so the zoo keeper doesn't get confused.  Automatically generate a reference number when building each cage.  The first cage should be 1, the second 2, etc.


Testing:
--------

    # TODO