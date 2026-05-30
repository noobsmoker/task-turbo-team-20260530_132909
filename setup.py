from setuptools import setup, find_packages

setup(
    name="task-turbo-team-20260530_132909",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'task=task:main',
        ],
    },
)
