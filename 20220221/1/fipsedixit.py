#!/usr/bin/python3
# -*- coding: utf-8 -*-
import argparse
import re
import sys

from ipsedixit import Generator

if __name__ == '__main__':

    def parse_args():
        parser = argparse.ArgumentParser()
        parser.add_argument('num',
                            nargs='?',
                            default=4,
                            type=int,
                            help='number of paragraphs to generate (default: %(default)s)',
                            )
        parser.add_argument('source',
                            nargs='?',
                            default='caesar',
                            type=str,
                            help='source of paragraphs to generate (default: %(default)s)',
                            )
        parser.add_argument('--min',
                            default=2,
                            type=int,
                            help='min number of sentences per paragraph (default: %(default)s)',
                            )
        parser.add_argument('--max',
                            default=4,
                            type=int,
                            help='max number of sentences per paragraph (default: %(default)s)',
                            )
        return parser.parse_args()

    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    args = parse_args()

    if args.source == 'caesar' or args.source == 'tacitus':
        generator = Generator(args.source)
    else:
        with open(args.source) as input_file:
            generator = Generator(input_file.read())
    print('\n\n'.join(generator.paragraphs(args.num, args.min, args.max)))
