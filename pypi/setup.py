from distutils.core import setup

setup(
    name='jubatus',
    packages=['jubatus'],
    version='0.2.1',
    description='online and parallel machine learning framework and library',
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Programming Language :: Python :: 2.7",
        #"Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering"
        ],
    keywords=[
        "machine learning"
        ],
    author="Preferred Infrastructure and NTT",
    author_email="uenishi.kota@lab.ntt.co.jp",
    install_requires=['msgpack-rpc-python'],
    url="http://jubat.us",
    license='LGPL'
    )
