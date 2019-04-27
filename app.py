#!flask/bin/python
from flask import Flask, jsonify, render_template, request, redirect
import pandas as pd
import numpy as np
import os, sys
import json
import csv
from math import *

with open('map.json') as data_file:
    us_json = json.load(data_file)

app = Flask(__name__)


@app.route('/')
def cjson():
    def disp(reader):
        df = []
        for row in reader:
            df.append(row)
        return df

    with open("countriesData.csv", 'r+') as f:
        reader = csv.reader(f)
        df = disp(reader)
        matric = [df[1][2], df[2][2], df[3][2], df[4][2], df[5][2], df[6][2], df[7][2], df[8][2], df[9][2], df[10][2],
                  df[11][2], df[12][2], df[13][2], df[14][2], df[15][2], df[16][2], df[17][2]]
        CountryCode = []
        for i in range(1, len(df) - 17, 17):
            CountryCode.append(df[i][1])
        return render_template("test.html", senddata=us_json, df=df, matric=matric, CountryCode=CountryCode)




if __name__ == '__main__':
    app.run(debug=True)
