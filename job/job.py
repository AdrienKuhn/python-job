import random
import sys
import time
import logging


class Job:
    def __init__(self):
        self._int_for_success = 1
        self._sleep_time = random.randrange(15)

    def run(self):
        logging.info("%s - Starting fake job" % time.ctime())
        rand = random.randrange(1, 5)

        logging.info("%s - Running..." % time.ctime())
        time.sleep(self._sleep_time)

        if rand == self._int_for_success:
            logging.info("%s - Job ran successfully" % time.ctime())
            sys.exit(0)
        else:
            logging.error("%s - Job failed" % time.ctime())
            sys.exit(1)
