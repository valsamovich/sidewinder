#!/usr/local/bin/python2.7

import argparse


def parse_arguments():
    """ Process the command line arguments.

    :return: arguments
    """
    # arguments
    parser = argparse.ArgumentParser()

    parser.add_argument('-s',
                        '--start',
                        help='The  start number - format <integer>.',
                        type=int,
                        default=0)
    parser.add_argument('-e',
                        '--end',
                        help='The end number - format <integer>.',
                        type=int,
                        default=100)
    parser.add_argument('-m',
                        '--message',
                        help='The end number - format <string>.',
                        default='Hello, World!')
    arguments, _ = parser.parse_known_args()
    return arguments

if __name__ == '__main__':
    try:
        args = parse_arguments()
        for i in range(args.start, args.end):
            if i == 9:
                print args.message
    except Exception, e:
        print('Exception: {arg}'.format(arg=e))
        raise
