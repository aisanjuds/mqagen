from setuptools import find_packages,setup
 setup(
    name="mqagenerator",
    version="0.0.1",
    author="sanjeev sanju",
    author_email="aisanjuds@gmail.com",
    install_requires={"openai","langchain","streamlit","python-dotenv","pyPDF2"},
    package=find_packages()
)