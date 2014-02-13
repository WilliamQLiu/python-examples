#! /usr/local/bin/python
""" Getting raw input """
# Run in shell with: python rawinput.py

def ask_ok(prompt, retries=4, complaint="Yes or no, please!"):
    while True:
        ok = raw_input(prompt)
        if ok.lower() in ('y', 'ye', 'yes'):
            return True
        if ok.lower() in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise IOError('refusenik user')
        print complaint

if __name__ == '__main__':
    ask_ok("Do you want to quit?")
