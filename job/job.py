import random
import sys
import time


class Job:
    def __init__(self):
        self._int_for_success = 1
        self._sleep_time = random.randrange(15)

    def run(self):
        print("%s - Starting fake job" % time.ctime())
        rand = random.randrange(1, 5)

        print("%s - Running..." % time.ctime())
        time.sleep(self._sleep_time)

        if rand == self._int_for_success:
            print("%s - Job ran successfully" % time.ctime())
            sys.exit(0)
        else:
            print("%s - Job failed" % time.ctime())
            sys.exit(1)
