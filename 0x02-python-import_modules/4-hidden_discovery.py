#!/usr/bin/python3
import dis

def print_hidden_4_names():
    code = open('hidden_4.pyc', 'rb').read()
    instructions = dis.get_instructions(code)
    
    names = set()
    for instr in instructions:
        if instr.opname == 'LOAD_NAME' and not instr.argrepr.startswith('__'):
            names.add(instr.argrepr)
    
    for name in sorted(names):
        print(name)

if __name__ == "__main__":
    print_hidden_4_names()
