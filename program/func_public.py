from func_utils import get_ISO_times
from constants import RESOLUTION
from pprint import pprint
import pandas as pd
import numpy as np
import time

# Get relevant time periods for ISO from and to
ISO_TIMES = get_ISO_times()
pprint(ISO_TIMES)

#Construct market prices
def construct_market_prices(client):
    pass