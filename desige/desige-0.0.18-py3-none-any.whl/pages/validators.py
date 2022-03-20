import os
import subprocess

class CliNuChecker:

    def validate(self, markup):
        '''
        Validate markup.
        Raises an exeption if validation fails.
        '''
        # XXX hack, need some modular system where base class can be constructed from mixins
        vnu = os.path.expanduser('~/vnu-runtime-image/bin/vnu')
        result = subprocess.run([vnu, '-'], capture_output=True, input=markup.encode('utf-8'))
        if result.returncode != 0:
            # XXX show error in context?
            raise Exception(f'Validation failed:\n{result.stderr.decode("utf-8")}')
