from setuptools import setup

setup(setup_requires='pypandoc')

packages = [
    'pilifana',
    'pilifana.clients',
    'pilifana.conversion'
]

dependencies = [
    'schedule',
    'pypandoc',
    'pyyaml',
    'daemonize'
]


def convert_markdown(file):
    try:
        import pypandoc
        long_description = pypandoc.convert(file, 'rst')
        long_description = long_description.replace("\r", "")

    except Exception as e:
        import io
        print("Cannot load package description: {0}.".format(e))
        print("Using raw content as fallback")
        with io.open('README.md', encoding="utf-8") as f:
            long_description = f.read()
    return long_description


setup(
    name='pilifana',
    version='0.2.dev1',
    license='MIT',
    description='Send values of pilight devices to KairosDB for use on Grafana dashboards',
    long_description=convert_markdown('README.md'),
    author='Damian Lippok',
    author_email='mail.dalee@gmail.com',
    packages=packages,
    install_requires=dependencies,
    data_files=[('/etc/pilifana', ['configuration/config.yaml'])],
    entry_points = {
        'console_scripts': [
            'pilifana = pilifana.main:main',
            'pilifanad = pilifana.daemon:start'
        ],
    },
)
