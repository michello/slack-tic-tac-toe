from flask import Flask, render_template, request
import pymysql.cursors

app = Flask(__name__)

# database stuff here if needed