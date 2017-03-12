"""
Check the current version of the Python and, depending on the version, displays a text message.
"""


def check_ver():
    import sys
    current_python_version = sys.version_info.major
    if current_python_version == 2:
        print ("You are using the appropriate version of the Python.")
    else:
        print("Please, use Python version 2.")


check_ver()
