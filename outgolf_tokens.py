#!/usr/bin/env python
########################################
# outgolf_tokens.py ####################
# The tokens for the Outgolf compiler. #
# ckjbgames 2017 #######################
########################################
import re, string
def tokenize(code):
    """
    Tokenize the code.
    """
    tokenized=[]
    whitespace=r'\s'
    for c in code:
