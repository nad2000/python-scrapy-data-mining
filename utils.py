import dill

def backup_object(obj, file_name=None):
    if file_name is None:
        file_name = "{0}.pkl".format(id(obj))
        print "*** Object stored in:", file_name
    with open(file_name, "wb") as bf:
        dill.dump(obj, bf)

def restore_object(file_name):
    with open(file_name, "rb") as bf:
        return dill.load(bf)


def chunks(l, num):
    """
    splits list in num chunks
    for running in parallel
    """
    n = len(l) / num + 1
    return [l[i:i + n] for i in range(0, len(l), n)]

