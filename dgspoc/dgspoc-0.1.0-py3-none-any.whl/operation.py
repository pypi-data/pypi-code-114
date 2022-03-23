"""Module containing the logic for describe-get-system operation"""

import sys
import re

from dgspoc.utils import File
from dgspoc.utils import Printer

from dgspoc.storage import TemplateStorage

from dgspoc.example import TemplateExample

from dgspoc.usage import validate_usage
from dgspoc.usage import show_usage

from templateapp import TemplateBuilder


def do_build_template(options):
    command, operands = options.command, list(options.operands)
    op_count = len(operands)
    feature = str(operands[0]).lower().strip() if op_count > 0 else ''
    if command == 'build' and feature == 'template':
        operands = operands[1:]
        validate_usage('{}_{}'.format(command, feature), operands)

        op_txt = ' '.join(operands).rstrip()

        if not op_txt:
            show_usage('{}_{}'.format(command, feature))
        elif op_txt.lower().startswith('example'):
            index = str(operands[-1]).strip()
            if op_count == 3 and re.match('[1-5]$', index):
                result = TemplateExample.get(index)
                print('\n\n{}\n'.format(result))
                sys.exit(0)
            else:
                show_usage('{}_{}'.format(command, feature), 'other')

        if File.is_exist(op_txt):
            with open(op_txt) as stream:
                user_data = stream.read()
        else:
            user_data = op_txt

        try:
            factory = TemplateBuilder(
                user_data=user_data, author=options.author, email=options.email,
                company=options.company
            )

            template_id = options.tmplid.strip()
            filename = options.filename.strip()

            fmt1 = '+++ Successfully uploaded generated template to "{}" template ID.'
            fmt2 = '+++ Successfully saved generated template to {}'
            fmt3 = 'CANT save generated template to existing {} file.  Use replaced flag accordingly.'

            if template_id or filename:
                is_ok = True
                lst = []
                if template_id:
                    is_uploaded = TemplateStorage.upload(
                        template_id, factory.template, replaced=options.replaced
                    )
                    is_ok &= is_uploaded
                    msg = fmt1.format(template_id) if is_uploaded else TemplateStorage.message
                    lst.append(msg)
                if filename:
                    filename = File.get_path(filename)
                    if File.is_exist(filename) and not options.replaced:
                        msg = fmt3.format(filename)
                        is_ok &= False
                    else:
                        is_saved = File.save(options.filename, factory.template)
                        is_ok &= is_saved
                        msg = fmt2.format(filename) if is_saved else File.message

                    lst and lst.append('=' * 20)
                    lst.append(msg)

                lst and Printer.print(lst)
                sys.exit(int(is_ok))
            else:
                print(factory.template)
                sys.exit(0)

        except Exception as ex:
            print('*** {}: {}'.format(type(ex).__name__, ex))
            sys.exit(1)

    elif command == 'build':
        if feature == 'script':
            return
        elif feature == 'usage' or feature == '':
            show_usage(command)
            sys.exit(0)
        else:
            show_usage(command)
            sys.exit(1)
