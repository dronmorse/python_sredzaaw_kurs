#!/usr/bin/env python3

import os
import functools
from datetime import datetime

filepath = r"C:\Users\Open-E\Desktop\dummy.txt"

def CreateWrapperWithPath(log_file_path):
    def CreateWrapper(func):
        def Wrapper(*args, **kwargs):
            with open(log_file_path, "a") as f:
                f.write("Action {} executed on {} on {} \n".format(func.__name__, filepath, datetime.now()))
            result = func(*args, **kwargs)
            return result
        return Wrapper
    return CreateWrapper

@CreateWrapperWithPath(r"C:\Users\Open-E\Desktop\dummy_log1.txt")
def FILE_DELETE(path):
    print("Deleting file {}".format(path))
    os.remove(path)

@CreateWrapperWithPath(r"C:\Users\Open-E\Desktop\dummy_log1.txt")
def FILE_CREATE(path):
    print("Creating file {}".format(path))
    open(path, "w+")


FILE_CREATE(filepath)

FILE_DELETE(filepath)