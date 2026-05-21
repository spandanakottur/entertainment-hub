# Code to setup the project structure

from pathlib import Path


if __name__=="__main__":
    folders = ["src","db","tests","src/extract","src/transform","src/load","src/utils"]
    files =  ["README.md",".env",".gitignore",".env.example","config.yml","main.py",
              "db/schema.sql","src/__init__.py","src/extract/__init__.py","src/transform/__init__.py",
              "src/load/__init__.py","src/utils/__init__.py","src/exceptions.py"]