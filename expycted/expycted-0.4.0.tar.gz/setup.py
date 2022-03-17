# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['expycted', 'expycted.internals']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'expycted',
    'version': '0.4.0',
    'description': 'Because tests should be easy to read',
    'long_description': '# Overview\n\n__Expycted__ is yet another `expect` pattern implementation.\n\nIt is not dependent on any testing framework and can plug into any as it is just an abstraction over `assert`.\n\nExamples:\n```python\nfrom expycted import expect\n\nexpect(True).to_not.be_false()                                  # This will succeed\n\nexpect([]).to.be_empty()                                        # This will succeed\n\nexpect([1,2,3]).to.contain(3)                                   # This will succeed\n\nexpect(10).to.equal("10")                                       # This will raise AssertionError\n\nexpect(10).to.be("10")                                          # This will succeed\n\nexpect.function(int).to_raise(ValueError).when_called_with(\'a\') # This will also succeed\n\n```\n\n# Installation\n\n__Expycted__ can be installed from PyPi by using:\n```shell\npip install expycted\n```\n\nAlternatively, you can clone the repository and build your own distribution using poetry.\n```sh\ngit clone https://github.com/petereon/expycted.git\npoetry build\n```\nThen you can install it using:\n```sh\npip install ./dist/expycted-<version>-py3-none-any.whl\n```\n\n# Matchers\n\nMatchers are used to ensure some conditions are met.\n\n## Value Matchers\n\nValue matchers can be used in two equivalent ways demonstrated below:\n\n```python\nexpect.value(10).to.be_greater_than(1)\nexpect(10).to.be_greater_than(1)\n```\n\nCurrently available matchers are:\n\n- Eqality and similarity\n    - `equal(self, value)`: equivalent to "`==`". With alias `be_equal_to`\n    - `be(self, value)`:  will check if string representation of values is same or if two objects have the same attributes or are equal\n- Numeric\n    - `be_greater_than(self, value)`: equivalent to "`>`". With alias `be_greater`\n    - `be_lesser_than(self, value)`: equivalent to "`<`". With alias `be_lesser `, `be_less`, `be_less_than`\n    - `be_greater_or_equal_to(self, value)`: equivalent to "`>=`". With aliases `be_greater_or_equal`, `be_greater_than_or_equal_to`\n    - `be_lesser_or_equal_to(self, value)`: equivalent to "`<=`". With aliases `be_lesser_or_equal`, `be_less_or_equal`, `be_less_than_or_equal_to`, `be_lesser_than_or_equal_to`\n    - `be_numeric(self)`: checks if `self.value` is a number or string covertible to a number. With alias `be_a_number`\n- Containment and Emptiness\n    - `contain(self, value)`: equivalent to "`in`". With aliases `have`, `include`\n    - `be_contained_in(self, value)`: equivalent to "`in`". Qith aliases `be_in`, `be_included_in`\n    - `be_empty(self)`: checks if `self.value` is iterable and `False`\n- Truthiness\n    - `be_true(self)`: checks if `self.value` is `True`\n    - `be_false(self)`: checks if `self.value` is `False`\n    - `be_truthy(self)`: checks if `self.value` behaves _true_ in if statement. With aliases `be_truey`, `be_trueish `\n    - `be_falsey(self)`: checks if `self.value` behaves _false_ in if statement. With aliases `be_falsy`, `be_falsish`\n- Typing\n    - `be_of_type(self, value)`: checks if `self.value` is of specified type. With aliases `be_type`, `have_type`\n    - `inherit(self, value)`: checks if `self.value` inherits/is a specified type. `be_subclass_of`, `have_parent`\n\n\n## Function Matchers\n\nFunction matchers can be called as such:\n```python\nexpect.function(string.replace).to_return(\'strength\').when_called_with(\'ing\', \'ength\')\n```\n\nCurrently available matchers are:\n- `to_return(self, value=None, type_of_value=None)` - checks if function returns a specified value, or type, or both.\n- `to_raise(self, exception_type)` - checks if function raises a specified exception.\n\nIn each case we have to specify arguments with which function is called in `.when_called_with` method. Method has aliases `when_called_with_args`, `when_called_with_arguments`\n\n## Filesystem Matchers\n\nFilesystem matchers can be called as such:\n```python\nexpect.folder(\'/some/folder\').to.contain(\'subfolder\')\n```\nCurrently available matchers are:\n- `contain(self, name, type: Union[File, Folder, None, str] = None)` - checks if folder contains a specified file or folder. If type is specified, it will check if file is file or folder is folder.\n- `contain_file(self, name)` - checks if folder contains a specified file.\n- `contain_folder(self, name)` - checks if folder contains a specified folder.\n- `exist(self)` - checks if folder exists.\n- `be_empty(self)` - checks if folder is empty.\n\nThey can be used with both \'expect.folder(\'/some/folder\').to\' and \'expect.folder(\'/some/folder\').to_not\' to check both positive and negative expectations.',
    'author': 'Petereon',
    'author_email': 'pvyboch1@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/petereon/expycted',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
