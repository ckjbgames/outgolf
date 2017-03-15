#!/usr/bin/env python
########################################
# outgolf_tokens.py ####################
# The tokens for the Outgolf compiler. #
# ckjbgames 2017 #######################
########################################
def tokenize(code):
    """
    Tokenize the code.
    """
    tokens=[]
    for currentChar in code:
        if currentChar == '(':
            tokens.append({'paren' : 
