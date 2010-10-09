import os
from subprocess import Popen, PIPE
from distutils.core import setup, Extension

if not os.path.isdir('http-parser'):
    Popen('git clone git://github.com/ry/http-parser'.split()).wait()

make = Popen(['make', 'print-env'], stdout=PIPE)
make.wait()

stdout = make.stdout.read().split('\n')
env = dict(line.split('=', 1) for line in stdout if len(line.split('=',1)) > 1)

source_files = env.pop('args').split()

os.environ.update(env)

setup(
    name        = 'bjoern',
    description = 'A screamingly fast Python WSGI server written in C.',
    version     = '0.3',
    ext_modules = [
        Extension('bjoern', sources=source_files, libraries=['ev'])
    ]
)