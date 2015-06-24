import os
import Commands.CommandABC

import importlib

def main():
    path = os.path.join(os.path.curdir, "Commands")
    files = os.listdir(path)
    files = [x for x in files if x.endswith('.py') and x != '__init__.py']
    module_names = [os.path.splitext(x)[0] for x in files]
    # print module_names

    modules = [importlib.import_module('.' + x, "Commands") for x in module_names]
    # print modules

    for c in Commands.CommandABC.CommandABC.__subclasses__():
        instance = c()
        print instance.run()


if __name__ == "__main__":
    main()
