import re


def censor(input):
    pattern = re.compile(r'\bfrack\w*\b', re.IGNORECASE)
    return pattern.sub("CENSORED", input)


censor('Frack you')
censor('I hope you fracking die')
censor('you fracking Frack')
