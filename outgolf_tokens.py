#!/usr/bin/env python
########################################
# outgolf_tokens.py ####################
# The tokens for the Outgolf compiler. #
# ckjbgames 2017 #######################
########################################
import re
def tokenize(code):
    """
    Tokenize the code.
    """
    tokens=[]
    whitespace=r'\s
