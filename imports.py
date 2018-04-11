import requests
from time import sleep
import argparse
import logging
import subprocess

from PIL import Image
from os import walk, listdir
from os.path import join, getsize