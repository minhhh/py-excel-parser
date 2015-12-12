#!/usr/bin/env python

"""
"""
import sys, os, traceback

def print_last_exception():
    # sys.stderr.write("*** Exception occured:\n")
    traceback.print_exc()

def main():
    try:
        # print "Starting ...", sys.version_info[:2]
        import parse_with_python
        parse_with_python.parse()
    except Exception:
        print_last_exception()
    except SystemExit as e:
        print e
