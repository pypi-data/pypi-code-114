from .argparser import arg_parser
from .key import get_encryption_key, generate_random_key
from .encryption import encrypt, decrypt


def main():
    options, args = arg_parser()
    input_filename = None
    encryption_key = None

    if options.gen_key:
        print(generate_random_key(b64_encoded=True))
        return

    if len(args) == 1:
        input_filename = args[0]

    if options.decrypt:
        encryption_key = get_encryption_key(options.key_env)
        decrypt(input_filename, options.output_filename, options.force, encryption_key)
    else:
        encryption_key = get_encryption_key(options.key_env)
        encrypt(input_filename, options.output_filename, options.force, encryption_key)


if __name__ == "__main__":
    main()
