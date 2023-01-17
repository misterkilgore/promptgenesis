import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='Prompt Genesis',
    version='0.0.1',
    author='Michele Cantoni',
    author_email='mcantoni81@gmail.com',
    description='Class for prompt generation',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/misterkilgore/promptgenesis',
    project_urls = {
        "Bug Tracker": "https://github.com/misterkilgore/promptgenesis/issues"
    },
    license='MIT',
    packages=['promptgenesis'],
    install_requires=[],
)
