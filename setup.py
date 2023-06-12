from setuptools import setup

setup(
    name='robo',
    version='0.1.0',
    description='A extension of selenium for robotization of web browsers.',
    url='https://github.com/4rfel/Robo-Selenium/',
    author='Arfel',
    author_email='arfomee@gmail.com',
    license='GNU General Public License v3.0',
    packages=['robo'],
    install_requires=['selenium',
                      'keyboard',
                      'pyautogui',
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)