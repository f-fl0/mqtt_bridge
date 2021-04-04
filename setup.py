from catkin_pkg.python_setup import generate_distutils_setup
from setuptools import setup

setup_args = generate_distutils_setup(
    packages=['mqtt_bridge'],
    package_dir={'': 'src'},
    install_requires=['inject>=4.0', 'msgpack>=1.0.2', 'paho-mqtt>=1.5.1']
)

setup(**setup_args)
