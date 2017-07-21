
from setuptools import setup
import xleditor


setup(
    name='xleditor',
    version=xleditor.VERSION,
    description='Easy to open xls/xlsx file and edit it (merge xlrd and xlutils)',
    long_description=open('README.md').read(),
    author='TaoJY',
    author_email='taojy123@163.com',
    maintainer='TaoJY',
    maintainer_email='taojy123@163.com',
    license='MIT License',
    install_requires=open('requirements.txt').read().strip().splitlines(),
    py_modules=['xleditor'],
    include_package_data=True,
    platforms=["all"],
    url='https://github.com/taojy123/xleditor',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],
)


