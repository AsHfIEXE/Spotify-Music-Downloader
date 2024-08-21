from setuptools import setup, find_packages

setup(
    name='spotify-music-downloader',
    version='1.2.0',  # Update version as needed
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'click'
        'pybase62'
        'pywidevine'
        'pyyaml'
        'yt-dlp'
    ],
    entry_points={
        'console_scripts': [
            'spotify-downloader=your_module.your_script:main',  # Update with your module and function names
        ],
    },
    url='https://github.com/AsHfIEXE/Spotify-Music-Downloader',
    license='MIT',
    author='AsHfIEXE',
    author_email='salahin0ashfi@gmail.com',
    description='This is a Spotify song downloader made with python.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)