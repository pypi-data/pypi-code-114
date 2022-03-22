def say_hello( name = None ):
	if name is None:
		return print( "Hello, World" )
	else:
		return print( "Hello, " + name )