from flask import Flask
from appdef import app

if __name__ == "__main__":
    app.run('localhost', 5000, debug = True)