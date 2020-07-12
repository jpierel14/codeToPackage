********
Examples
********

Creating a Python Package
=========================

If you have a folder called ``myCodeBase`` containing a set of standalone working code,
then we can turn it into a package like this:

.. code-block:: python

	import codetopackage


	codetopackage.create_package(
	    PackageTargetDirectory= 'path/to/package/location/myPackageName',
	    PackageSourceDirectory= 'myCodeBase',
	    PackageName= "myPackageName",
	    CreateDocs=False
	    )

This is the bare minimum required to create package. Now we can add in docs, and
some optional additions to the docs:

.. code-block:: python

	import codetopackage=
		codetopackage.create_package(
	    PackageTargetDirectory= 'path/to/package/location/myPackageName',
	    PackageSourceDirectory= 'myCodeBase',
	    PackageName= "myPackageName",
	    CreateDocs=True,
	    PackageAuthor="YourNameHere",
	    IncludeInAPI=["importantModule"],
	    PackageDataFolders=['myDataFolder'],
	    PackageAuthorEmail='YourEmailHere'
	    )

This will create the exact same package as before, but with a ``Docs`` folder. The 
author and email will be propagated into the docs. The list of ``IncludeInAPI`` modules
will be added to the API documentation using autodoc. ``PackageDataFolders`` is a list
of folders containing data that you would like to have packaged up when your package
is installed by a user (say with pip). 

Finally, we can initialize this as a git repo and connect it to an existing remote 
repository. If you do this, you should create a new repository online and then 
run this stage with the online repository brand new and empty (no readme, no .gitignore):


.. code-block:: python

	import codetopackage

	 codetopackage.create_package(
	    PackageTargetDirectory= 'path/to/package/location/myPackageName',
	    PackageSourceDirectory= 'myCodeBase',
	    PackageName= "myPackageName",
	    CreateDocs=True,
	    PackageAuthor="YourNameHere",
	    IncludeInAPI=["importantModule"],
	    PackageDataFolders=['myDataFolder'],
	    PackageAuthorEmail='YourEmailHere',
	    InitAsGit= True,
    	ConnectRemoteGitRepository= 'https://github.com/username/myPackageName.git'
	    )

Editing Documentation
=====================

The documentation created by ``codetopackage`` will be barebones, you can go back
and improve it once it's created. You can create an account at readthedocs once your
package is created, and import the github repository connected to your new package. 
You should then be able to view this initial documentation. You can add a picture of
yourself in the ``_static`` folder, and then edit the ``contributors.rst`` file to use
your new picture and add your github page. You can edit the ``conf.py`` file to change your
html favicon (the image appearing in the tab) by uncommenting this line in the ``conf.py``: 
``#html_favicon = '_static/your_image_here.png'`` and replacing the png filename with an image of your choice.
Similarly, you can add an image to the top of the index on the left of your documentation by 
uncommenting this line ``#html_logo = "_static/mylogo.png"`` and replacing the logo image filename. 

You can add a textual example (like this one) to your docs by editing the ``examples.rst`` file, or a working
python script example by editing the ``_examples/plot_package.py`` file. Due to a known bug in the docs gallery
code, this example script **must** start with ``plot_``, but otherwise you can rename the rest of the filename. If
this file is edited, it will actually be run when readthedocs compiles your documentation, showing any plots 
and generating downloadable ``.py`` and ``.ipynb`` files (as well as creating an examples folder with the jupyter notebook
in your base directory). An example of this is shown on the main page of this documentation for reference. 


Making your package Pip Installable
===================================

``codetopackage`` finishes with a package that is installable with the normal ``python setup.py install``, and is ready
to be made pip installable. The only reason it isn't included, is because you need a PyPi account to make your package
pip installable. So just create your package, make sure it is installable using ``python setup.py intall`, then create 
a PyPi account here: `https://pypi.org/account/register/ <https://pypi.org/account/register/>`_. Make sure to confirm
your e-mail address, then install the `twine package <https://pypi.org/project/twine/>`_, and run the following commands in your terminal
(in your package main directory, where setup.py lives):

.. code-block:: bash
	
	rm dist/*
	python setup.py bdist_wheel
    twine upload dist/*

The first time you run this you'll likely get an error saying there is no such file as ``dist/*``, but then it will be created and
each time you want to update your pip distribution you'll need to run these same 3 lines. You'll be prompted for your username
and password, and then the package will upload to PyPi and be pip installable. **Every time you update your package with PyPi, you
must increment your package version number in the setup.py file**.


