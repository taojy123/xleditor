
from setuptools import setup

""" 
从 xleditor import VERSION 可能因为其他代码导致错误, 比如因为安装顺序的关系, xlrd 还没有安装好, 
这时候 xleditor 还不能正常使用但是 setup 应该不被影响
VERSION 应该在这里定义
"""

VERSION = '1.0.3'

setup(
    name='xleditor',
    version=VERSION,
    description='Easy to open xls file and edit it (merge xlrd and xlutils)',
    long_description=open('README.md', encoding='utf8').read(),
    long_description_content_type="text/markdown",
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


