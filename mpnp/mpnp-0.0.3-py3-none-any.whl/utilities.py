#coding=utf-8
from datetime import datetime
import platform











def create_readme( author = 'Mário Popolin Neto (mariopopolin@gmail.com)', msg = '', folder = './' ):


	writer = open( folder + 'README.txt', 'w' )
	separator = '-----------------------------------\n\n\n'

	
	writer.write( 'Author: ' + author + '\n' )
	now = datetime.now()
	writer.write( now.strftime( '%d/%m/%Y %H:%M:%S' ) + '\n\n' )
	writer.write( 'Este projeto não pode ser utilizado sem a completa e expressa autorização de seu autor.\n' )
	writer.write( 'This project can not be used without its author\'s full and express authorization.\n' )
	writer.write( separator )

	
	if msg != '':
		writer.write( msg + '\n' )
		writer.write( separator )

	
	writer.write( 'System: ' + platform.system() + '\n' )
	writer.write( 'Processor: ' + platform.processor() + '\n' )
	writer.write( 'Python Version: ' + platform.python_version() + '\n' )
	writer.write( 'Python Implementation: ' + platform.python_implementation() + '\n' )
	writer.write( separator )

	
	writer.write( 'Python Packages (pip freeze):\n\n' )

	try:
	    from pip._internal.operations import freeze
	except ImportError:  # pip < 10.0
	    from pip.operations import freeze

	for p in freeze.freeze():
		writer.write( p  + '\n' )

	writer.write( separator )


	writer.close()