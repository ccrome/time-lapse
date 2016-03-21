import os


def get_files(dir, ext):
    """Return a list of files with extension ext that exist within dir
    returns a list of 3-tuples:
    [ [ full-path-name, dirname-only, filename-only ],
    ...
    ]
    """
    nefs = list()
    for root, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith(ext):
                nefs.append([os.path.join(root, file), root, file])
    return nefs
