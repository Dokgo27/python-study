import time


def time1():

    now = time.localtime()

    return("%04d/%02d/%02d/%02d" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour))