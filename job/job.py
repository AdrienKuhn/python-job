import random
import sys
import time
import logging


class Job:
    def __init__(self):
        self._int_for_success = 1
        self._sleep_time = random.randrange(10)

    def run(self):
        logging.info("%s - Starting fake job" % time.ctime())
        success = random.randrange(1, 4)

        logging.info("%s - Running..." % time.ctime())
        time.sleep(self._sleep_time)

        if success == self._int_for_success:
            logging.info("%s - Job ran successfully" % time.ctime())
            sys.exit(0)
        else:
            logging.error("%s - Job failed" % time.ctime())
            sys.exit(1)
