from setuptools import setup

setup(
    name="ah_lite",
    version='1.0',
    py_modules=['ah_lite'],
    install_requires=[
        'click', 'requests', 'pytest', 'pytest-cov', 'coverage', 'coveralls',
    ],
    entry_points='''
        [console_scripts]
        ah=ah_lite:ah
    ''',
)
