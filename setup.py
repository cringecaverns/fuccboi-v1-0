from setuptools import setup, find_packages

setup_info = dict(
    # Metadata
    name='pyglet',
    version='v1.0',
    author='cringecaverns',
    author_email='cringecaverns@cyber-wizard.com',
    url='https://github.com/cringecaverns/fuccboi-v1-0',
    download_url='https://github.com/cringecaverns/fuccboi-v1-0',
    description='A garbage bot for curl the yahoo',
    license='BSD',
    install_requires=[
        'disco-py'
    ],
    classifiers=[
        'Development Status :: 1 - Production/Stable',
    ],

    # Package info
    packages=find_packages(),
    zip_safe=True,
)