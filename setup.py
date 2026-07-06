from setuptools import find_packages, setup

setup(
    name="agentic-trading-bot",
    version="0.1.0",
    author="Rajib Saha",
    author_email="rajib.apd@gmail.com",
    packages=find_packages(),
    install_requires=[
        "lancedb",
        "langchain",
        "langgraph",
        "tavily-python",
        "polygon"
    ]
)
