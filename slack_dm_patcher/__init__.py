from __future__ import print_function

from argparse import ArgumentParser


def main():
    parser = ArgumentParser(description="Patch Slack app with custom CSS")
    args = parser.parse_args()
    print(args)
