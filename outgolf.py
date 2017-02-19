#!/usr/bin/env python
# outgolf.py
#############
# Outgolf ###
# ckjbgames #
# 2017 ######
#############
try:
    import sys, re, math, string, random, time, parser
except ImportError:
    print 'There was an error importing a module.'
    print 'Sorry about that.'
    sys.exit()
global stack # stack is now global
stack=[]     # The stack is set to an empty list
