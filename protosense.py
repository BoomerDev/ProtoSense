import os
import sys

import glob

class ProtoSense:
    def __init__(self):
        self.file_types = []
        self.files = []
        
        if not os.path.isfile(".protosense"):
            print("Please run protosense in the directory that contains the '.protonsense' file.")
            sys.exit(-1)
        
        with open(".protosense", 'r') as f:
            for line in f.readlines():
                line = line.strip()

                if line.startswith("#"):
                    pass
                
                elif line.startswith("*."):
                    self.file_types.append(line)

                else:
                    self.files.append(line)

    def run(self):
        ignores = []
        ignores.extend(self.files)

        for x in self.file_types:
            ignores.extend(glob.glob("**/%s" % x, recursive=True))
        
        for y in ignores:
            if os.path.exists(y):
                os.remove(y)
        