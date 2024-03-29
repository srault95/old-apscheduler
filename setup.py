# coding: utf-8
import os.path

from setuptools import setup, find_packages

import apscheduler


here = os.path.dirname(__file__)
readme_path = os.path.join(here, 'README.rst')
readme = open(readme_path).read()

setup(
    name='APScheduler',
    version=apscheduler.release,
    description='In-process task scheduler with Cron-like capabilities',
    long_description=readme,
    author='Alex Gronholm',
    author_email='apscheduler@nextday.fi',
    url='http://pypi.python.org/pypi/APScheduler/',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ],
    keywords='scheduling cron',
    license='MIT',
    packages=find_packages(exclude=['tests']),
    install_requires=[
        'setuptools >= 0.7',
        'six >= 1.4.0',
        'pytz',
        'tzlocal'
    ],
    extras_require={
        ':python_version == "2.7"': ['futures', 'funcsigs']
    },
    zip_safe=False,
    entry_points={
        'apscheduler.triggers': [
            'date = apscheduler.triggers.date:DateTrigger',
            'interval = apscheduler.triggers.interval:IntervalTrigger',
            'cron = apscheduler.triggers.cron:CronTrigger'
        ],
        'apscheduler.executors': [
            'debug = apscheduler.executors.debug:DebugExecutor',
            'threadpool = apscheduler.executors.pool:ThreadPoolExecutor',
            'processpool = apscheduler.executors.pool:ProcessPoolExecutor',
            'asyncio = apscheduler.executors.asyncio:AsyncIOExecutor',
            'gevent = apscheduler.executors.gevent:GeventExecutor',
            'twisted = apscheduler.executors.twisted:TwistedExecutor'
        ],
        'apscheduler.jobstores': [
            'memory = apscheduler.jobstores.memory:MemoryJobStore',
            'sqlalchemy = apscheduler.jobstores.sqlalchemy:SQLAlchemyJobStore',
            'mongodb = apscheduler.jobstores.mongodb:MongoDBJobStore',
            'rethinkdb = apscheduler.jobstores.rethinkdb:RethinkDBJobStore',
            'redis = apscheduler.jobstores.redis:RedisJobStore'
        ]
    }
)
