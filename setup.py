# Automatically created by: shub deploy
# https://app.scrapinghub.com/p/165180/jobs

from setuptools import setup, find_packages

setup(
    name         = 'project',
    version      = '1.0',
    packages     = find_packages(),
    entry_points = {'scrapy': ['settings = scrapy_axa.settings']},
)
