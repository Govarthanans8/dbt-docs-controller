from setuptools import setup, find_packages

setup(
    name='dbt-docs-controller',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'dbt-docs-controller=Custom_dbt:main',
        ],
    },
    install_requires=[],
    author='Govarthanan S',
    description='dbt-docs-controller streamlines dbt documentation by generating only the relevant models, sources, and components for concise, targeted user information.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Govarthanans8/dbt-docs-controller/tree/main',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
