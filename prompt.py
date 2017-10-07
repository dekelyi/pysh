from env import CWD

PROMPT = "{CWD}$"

def prompt():
    return PROMPT.format(CWD=CWD.get())
