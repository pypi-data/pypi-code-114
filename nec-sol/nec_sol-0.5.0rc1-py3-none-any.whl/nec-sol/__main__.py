from collections import OrderedDict
from simple_term_menu import TerminalMenu
import getpass
import platform
import re
import requests
import subprocess
import sys

#-------------------------------------------------------------------------------
class Plugin:
	def __init__(self, name, version, url, condition):
		self.name			= name
		self.version		= version
		self.raw_version	= re.sub(r'\+.*', '', version)
		self.url			= url
		self.condition		= condition

	def eval(self, mods):
		if self.condition is None:
			return True

		for pkg in mods:
			if self.condition(pkg):
				return True
		
		return False

	def __repr__(self):
		return '[Plugin name={}, version={}, url={}, condition={}]'.format(self.name, self.version, self.url, self.condition)

L_EMPH  	= "\033[1m"
L_RESET 	= "\033[0m"

s_plugins		= None
s_modules		= None
s_available		= OrderedDict()
s_local_repo	= False
s_globally		= False
s_trust			= False

#-------------------------------------------------------------------------------
def add(plugin, version, url, mod, conds):
	if mod not in s_available:
		s_available[mod] = {}
	s_available[mod][plugin] = Plugin(plugin, version, url, conds)

#-------------------------------------------------------------------------------
arch = platform.machine()
add("nec-sol-license", "1.0", "https://sol.neclab.eu/license/index.php/pip-license-index", "license",   None)
add('nec-sol-core', '0.5.0rc1', 'https://sol.neclab.eu/core/v0.5.0rc1', 'core', None)
add('nec-sol-omp', '0.5.0rc1', 'https://sol.neclab.eu/core/v0.5.0rc1', 'core', None)
add('nec-sol-device-x86', '0.5.0rc1', 'https://sol.neclab.eu/core/v0.5.0rc1', 'core', lambda pkg: arch == 'x86_64' or pkg == 'x86')
add('nec-sol-device-ve', '0.5.0rc1', 'https://sol.neclab.eu/ve/v0.5.0rc1', 've', None)
add('nec-sol-jit-gcc', '0.5.0rc1', 'https://sol.neclab.eu/core/v0.5.0rc1', 'core', None)
add('nec-sol-jit-dot', '0.5.0rc1', 'https://sol.neclab.eu/core/v0.5.0rc1', 'core', None)
add('nec-sol-jit-python', '0.5.0rc1', 'https://sol.neclab.eu/core/v0.5.0rc1', 'core', None)
add('nec-sol-jit-ispc', '0.5.0rc1', 'https://sol.neclab.eu/x86/v0.5.0rc1', 'x86', None)
add('nec-sol-jit-ncc', '0.5.0rc1', 'https://sol.neclab.eu/ve/v0.5.0rc1', 've', None)
add('nec-sol-backend-gcc', '0.5.0rc1', 'https://sol.neclab.eu/x86/v0.5.0rc1', 'x86', None)
add('nec-sol-backend-dfp', '0.5.0rc1', 'https://sol.neclab.eu/core/v0.5.0rc1', 'core', None)
add('nec-sol-backend-dnn', '0.5.0rc1', 'https://sol.neclab.eu/core/v0.5.0rc1', 'core', None)
add('nec-sol-backend-dnn-mkl', '0.5.0rc1', 'https://sol.neclab.eu/x86/v0.5.0rc1', 'x86', None)
add('nec-sol-backend-dnn-dnnl', '0.5.0rc1', 'https://sol.neclab.eu/x86/v0.5.0rc1', 'x86', None)
add('nec-sol-backend-ispc', '0.5.0rc1', 'https://sol.neclab.eu/x86/v0.5.0rc1', 'x86', None)
add('nec-sol-backend-dfp-ispc', '0.5.0rc1', 'https://sol.neclab.eu/x86/v0.5.0rc1', 'x86', None)
add('nec-sol-backend-ncc', '0.5.0rc1', 'https://sol.neclab.eu/ve/v0.5.0rc1', 've', None)
add('nec-sol-backend-dfp-ncc', '0.5.0rc1', 'https://sol.neclab.eu/ve/v0.5.0rc1', 've', None)
add('nec-sol-backend-dnn-veblas', '0.5.0rc1', 'https://sol.neclab.eu/ve/v0.5.0rc1', 've', None)
add('nec-sol-backend-dnn-vednn', '0.5.0rc1', 'https://sol.neclab.eu/ve/v0.5.0rc1', 've', None)
add('nec-sol-backend-dnn-veasl', '0.5.0rc1', 'https://sol.neclab.eu/ve/v0.5.0rc1', 've', None)
add('nec-sol-dist-x86-jsoncpp', '1.9.4', 'https://sol.neclab.eu/core/dist', 'core', lambda pkg: arch == 'x86_64')
add('nec-sol-dist-x86-openssl', '1.1.1+n', 'https://sol.neclab.eu/core/dist', 'core', lambda pkg: arch == 'x86_64')
add('nec-sol-dist-x86-sqlite', '3380000', 'https://sol.neclab.eu/core/dist', 'core', lambda pkg: arch == 'x86_64')
add('nec-sol-dist-x86-ispc', '1.17.0', 'https://sol.neclab.eu/x86/dist', 'x86', None)
add('nec-sol-dist-x86-sleef', '3.5.1', 'https://sol.neclab.eu/x86/dist', 'x86', None)
add('nec-sol-dist-ve-vednn', '2020.7.2', 'https://sol.neclab.eu/ve/dist', 've', None)
add('nec-sol-framework-pytorch', '0.5.0rc1', 'https://sol.neclab.eu/core/v0.5.0rc1', 'pytorch', None)
add('nec-sol-framework-pytorch-x86', '0.5.0rc1', 'https://sol.neclab.eu/core/v0.5.0rc1', 'pytorch', lambda pkg: arch == 'x86_64' or pkg == 'x86')
add('nec-sol-framework-pytorch-ve', '0.5.0rc1', 'https://sol.neclab.eu/ve/v0.5.0rc1', 'pytorch', lambda pkg: pkg == 've')
add('nec-sol-framework-tensorflow', '0.5.0rc1', 'https://sol.neclab.eu/core/v0.5.0rc1', 'tensorflow', None)
add('nec-sol-framework-tensorflow-x86', '0.5.0rc1', 'https://sol.neclab.eu/core/v0.5.0rc1', 'tensorflow', lambda pkg: arch == 'x86_64' or pkg == 'x86')
add('nec-sol-framework-tensorflow-ve', '0.5.0rc1', 'https://sol.neclab.eu/ve/v0.5.0rc1', 'tensorflow', lambda pkg: pkg == 've')
add('nec-sol-docs', '0.5.0rc1', 'https://sol.neclab.eu/core/v0.5.0rc1', 'core', None)
add('nec-sol-tests', '0.5.0rc1', 'https://sol.neclab.eu/dev/v0.5.0rc1', 'tests', None)


#-------------------------------------------------------------------------------
# taken from: https://stackoverflow.com/questions/1871549/determine-if-python-is-running-inside-virtualenv
def is_virtualenv():
	return (hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix))

print(getattr(sys, "base_prefix", None), getattr(sys, "real_prefix", None), sys.prefix)

#-------------------------------------------------------------------------------
def run(cmd):
	ret = subprocess.run(cmd)
	if ret.returncode != 0:
		raise Exception("PIP error detected")

#-------------------------------------------------------------------------------
def run_output(cmd):
	ret = subprocess.run(cmd, stdout=subprocess.PIPE)
	if ret.returncode != 0:
		raise Exception("PIP error detected")
	return ret.stdout.decode('utf-8')

#-------------------------------------------------------------------------------
def lookup_modules(plugins):
	assert isinstance(plugins, list)
	reverse	= {
		"nec-sol-backend-dnn_cudnn-bundle":	"cudnn",
		"nec-sol-dist-arm64-ispc":				"arm64",
		"nec-sol-dist-x86-ispc":				"x86",
		"nec-sol-core":						"core",
		"nec-sol-device-nvidia":				"nvidia",
		"nec-sol-device-ve":					"ve",
		"nec-sol-framework-dl4j":				"dl4j",
		"nec-sol-framework-numpy":				"numpy",
		"nec-sol-framework-onnx":				"onnx",
		"nec-sol-framework-pytorch":			"pytorch",
		"nec-sol-framework-tensorflow":		"tensorflow",
		"nec-sol-license":						"license",
		"nec-sol-tests":						"tests",
		"nec-sol-sdk":							"sdk",
	}

	modules = []
	for p in plugins:
		r = reverse.get(p)
		if r:
			modules.append(r)
	return modules

#-------------------------------------------------------------------------------
def initialize():
	def init_plugins():
		input = run_output(['python3', '-m', 'pip', 'list', 'installed']).split('\n')
		plugins = {}
		prog = re.compile('^(nec-sol[a-z0-9-]+)\s+([0-9\.a-z]+)')
		for x in input:
			match = prog.match(x)
			if match:
				plugins[match[1]] = match[2]
		return plugins
	
	global s_plugins, s_modules
	s_plugins = init_plugins()
	s_modules = lookup_modules(list(s_plugins.keys()))

#-------------------------------------------------------------------------------
def get_plugins():		return s_plugins
def get_modules():		return s_modules
def get_available():	return s_available

#-------------------------------------------------------------------------------
# Callbacks
#-------------------------------------------------------------------------------
def install(plugins, is_install):
	assert isinstance(plugins, list)
	assert isinstance(is_install, bool)

	cmd = ['python3', '-m', 'pip', 'install' if is_install else 'download']

	if is_install and not is_virtualenv() and not s_globally:
		cmd.append('--user')

	urls = set()
	for p in plugins:
		cmd.append('{}=={}'.format(p.name, p.version))
		urls.add(p.url)

	if s_local_repo:
		cmd.append('-f')
		cmd.append('.')
	else:
		if s_trust:
			cmd.append('--trusted-host')
			cmd.append('sol.neclab.eu')

			# https://gitlab.neclab.eu/darp-git-SOL-CLOSED-BETA/sol-closed-beta/-/issues/436
			cmd.append('--trusted-host')
			cmd.append('download.pytorch.org')

		for u in urls:
			cmd.append('-f')
			cmd.append(u)		

	run(cmd)
	initialize() # update database

#-------------------------------------------------------------------------------
def uninstall(plugins=None):
	global s_modules

	if plugins is None:
		initialize()
		if len(get_plugins()) == 0:
			print('SOL is not installed on this machine')
			return

		options			= ['no, not really', 'yes of course!']
		terminal_menu	= TerminalMenu(options, title='Are you sure you want to uninstall SOL?\n')
		choice			= terminal_menu.show()
		if choice == 1:
			plugins		= list(get_plugins().keys())
		else:
			return
	
	assert isinstance(plugins, list)
	if len(plugins):
		run(['python3', '-m', 'pip', 'uninstall', '-y'] + plugins)

		# update lookups -------------------------------------------------------
		for p in plugins:
			get_plugins().pop(p)
		s_modules = lookup_modules(list(get_plugins().keys()))

#-------------------------------------------------------------------------------
def get_plugin_list(mods):
	assert isinstance(mods, list)
	plugins = []

	for m in mods:
		for p in get_available().get(m).values():
			if p.eval(mods):
				plugins.append(p)

	return plugins

#-------------------------------------------------------------------------------
def select_modules(is_install):
	assert isinstance(is_install, bool)
	if is_install:
		initialize()

	check_license	(is_install)
	upgrade			(is_install)

	mods				= ['core', 'license']
	modules				= []
	already_installed	= []

	for m in get_available().keys():
		if m == 'core' or 'license' in m: # core and license can't be selected by the user
			continue

		if is_install and m in get_modules():
			already_installed.append(len(modules))
		modules.append(m)

	terminal_menu = None

	def preview(_):
		mod_list = list(mods)
		for idx in terminal_menu._selection:
			mod_list.append(modules[idx])

		plugin_list = get_plugin_list(mod_list)
		plugins	= []
		urls	= set()
		for p in plugin_list:
			plugins.append('\n- {}=={}'.format(p.name, p.version))
			urls.add(p.url)
		urls = list(urls)

		out = L_EMPH + 'Access to following URLs is required:' + L_RESET
		urls.sort()
		for u in urls:
			out += '\n{}'.format(u)

		out += '\n\n' + L_EMPH + 'Following Python packages will be {}:'.format('installed' if is_install else 'downloaded') + L_RESET
		plugins.sort()
		for p in plugins:
			out += p

		return out

	terminal_menu = TerminalMenu(
		modules,
		multi_select					= True,
		show_multi_select_hint			= True,
		multi_select_empty_ok			= True,
		multi_select_select_on_accept	= False,
		preselected_entries				= already_installed,
		title							= "Please select the modules that you want to {}:".format('install' if is_install else 'download'),
		preview_title					= "",
		preview_command					= preview,
		preview_size					= 0.5
	)

	choices = terminal_menu.show()

	if choices:
		for i in choices:
			mods.append(modules[i])

		# get final list of plugins to install ---------------------------------
		plugins = get_plugin_list(mods)

		# uninstall unwanted packages ------------------------------------------
		if is_install:
			to_remove = []
			for k in get_plugins().keys():
				def run():
					for p in plugins:
						if p.name == k:
							return
					to_remove.append(k)
				run()
			uninstall(to_remove)

		# install/download plugins ---------------------------------------------
		install(plugins, is_install)

#-------------------------------------------------------------------------------
def list_installed():
	initialize()
	if len(get_plugins()) == 0:
		print('SOL is not installed on this machine')
		return
		
	print(L_EMPH + 'Installed SOL Modules:' + L_RESET)
	for m in get_modules():
		print('- {}'.format(m))

	print('')
	print(L_EMPH + 'Installed SOL Plugins:' + L_RESET)
	for p, v in get_plugins().items():
		print('- {} v{}'.format(p, v))
	print('')

#-------------------------------------------------------------------------------
def check_license(is_install):
	# Helper Functions ---------------------------------------------------------		
	def less(text, step = 40):
		assert isinstance(text, list)
		cnt = len(text)
		for i in range(0, (cnt + step - 1) // step):
			start	= i * step
			end		= min(cnt, start + step)
			for n in range(start, end):
				print(text[n])

			if end < cnt:
				print('')
				input('Press <Enter> for more')
		print('')

	def convert(markdown):
		out	= []
		for l in markdown.split('\n'):
			l = l.replace('<br/>', ' ')
			l = re.sub(r'<[^>]+>', '', l) # removes HTML tags

			def find():
				i = 0
				for i in range(0, len(l)):
					if l[i] != '#' and l[i] != ' ' and l[i] != '*':
						return i
				return i

			r = l[:find()]
			if		r == '# ':	l = "\033[47m\033[1;30m"	+ l[2:] + "\033[0m"
			elif	r == '## ':	l = "\033[1;37m\033[4;37m"	+ l[3:] + "\033[0m"
			elif	r == '**':	l = "\033[1;37m"			+ l[2:-2] + "\033[0m"

			out.append(l)
		return out

	# Local installs can't check license ---------------------------------------
	if s_local_repo:
		return

	# Check if license is installed and with correct version -------------------
	if is_install:
		v = get_plugins().get('nec-sol-license')
		if v == '1.0':
			return

		# If wrong version is installed, uninstall it before continuing --------
		if v:
			uninstall('nec-sol-license')

	# Fetch License Agreement for this user ------------------------------------
	print('Please authenticate using your SOL login for verifying your license status:')
	print('User for sol.neclab.eu: ', end='')
	username = input()
	password = getpass.getpass()
	print()

	# Process license request --------------------------------------------------	
	r = requests.get("https://sol.neclab.eu/license/index.php/fetch-license", auth=(username, password), verify=not s_trust)
	r.raise_for_status()
	msg = r.json()

	license_text			= msg.get('license')
	license_authorization	= msg.get('license_authorization')
	license_acceptance		= msg.get('license_acceptance')
	license_error			= msg.get('license_error')

	if license_text is None or license_authorization is None or license_acceptance is None:
		if license_error:
			raise Exception(msg['license_error'])
		raise Exception('invalid msg received from server')

	# Show license text --------------------------------------------------------
	less(convert(license_text))

	options			= ["no, I am not", "yes, I am"]
	terminal_menu	= TerminalMenu(options, title=license_authorization)
	choice			= terminal_menu.show()
	if choice != 1:	raise Exception("License declined!")

	options			= ["decline license", "accept license"]
	terminal_menu	= TerminalMenu(options, title=license_acceptance)
	choice			= terminal_menu.show()
	if choice != 1:	raise Exception("License declined!")

#-------------------------------------------------------------------------------
def options():
	global s_local_repo, s_globally, s_trust

	selected = []
	if s_local_repo:	selected.append(0)
	if s_trust:			selected.append(1)

	options = ['install SOL from current folder', 'don\'t check SOL repo server certificates (not recommended)']
	if not is_virtualenv():
		options.append('install SOL globally')
		if s_globally:
			selected.append(2)

	terminal_menu = TerminalMenu(
		options,
		multi_select					= True,
		show_multi_select_hint			= True,
		multi_select_empty_ok			= True,
		multi_select_select_on_accept	= False,
		preselected_entries				= selected,
		title							= "SOL Installation Options:",
	)

	choices	= terminal_menu.show()

	if choices is None:
		choices = []
	
	s_local_repo	= 0 in choices
	s_trust			= 1 in choices
	s_globally		= 2 in choices

#-------------------------------------------------------------------------------
def upgrade(is_install):
	if is_install:
		to_remove	= []
		to_install	= []

		def requires_upgrade(p, v):
			for a in get_available().values():
				info = a.get(p)
				if info:
					if info.raw_version != v:
						to_remove.append(p)
						to_install.append(p)
					return
			to_remove.append(p) # rogue/obsolete plugins so we can removed it

		for p, v in get_plugins().items():
			requires_upgrade(p, v)

		if len(to_remove) or len(to_install):
			options			= ['decline upgrade', 'accept upgrade']
			terminal_menu	= TerminalMenu(options, title='SOL needs to upgrade some packages before you can continue:')
			choice			= terminal_menu.show()

			if choice != 1:
				raise Exception('Upgrade declined')

			if len(to_remove):
				uninstall(to_remove)

			to_install = lookup_modules(to_install)
			to_install.append('license') # license is ALWAYS needed
			if len(to_install):
				print('')
				print('Detected installed SOL modules: {}'.format(to_install))
				print('')
				install(get_plugin_list(to_install), True)

#-------------------------------------------------------------------------------
if __name__ == '__main__':
	print(L_EMPH + '## NEC-SOL Package Manager v0.5.0rc1' + L_RESET)

	while True:
		print('')
		terminal_menu	= TerminalMenu(['install/modify modules', 'download modules', 'list installed modules', 'uninstall all modules', 'options', 'exit installer'], title='Please choose an action:')
		choice			= terminal_menu.show()
		print('')

		if		choice == 0:	select_modules(True)
		elif	choice == 1:	select_modules(False)
		elif	choice == 2:	list_installed()
		elif	choice == 3:	uninstall()
		elif	choice == 4:	options()
		else:					break
