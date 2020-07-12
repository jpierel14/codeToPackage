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