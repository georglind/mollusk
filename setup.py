import os
from setuptools import setup
from setuptools.config import read_configuration

cfg = read_configuration('./setup.cfg')
#print(cfg)
cfg["options"].update(cfg["metadata"])
cfg=cfg["options"]
setup(use_scm_version = True, **cfg)
