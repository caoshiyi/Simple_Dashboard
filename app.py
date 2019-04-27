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


@app.route('/kk')
def index():
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
        return render_template("index.html", senddata=us_json, df=df, matric=matric, CountryCode=CountryCode)


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


@app.route('/radar')
def ajson():
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
        return render_template("radar.html", senddata=us_json, df=df, matric=matric, CountryCode=CountryCode)


@app.route('/map')
def bcsv():
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
        return render_template("index_map.html", senddata=us_json, df=df, matric=matric, CountryCode=CountryCode)


if __name__ == '__main__':
    app.run(debug=True)

'''@app.route('/user', methods=['POST'])
def sendjson():
	CountryName=request.form.get("countryName")
	SeriesName=request.form.get("seriesName")
	fyear=request.form.get("2010year")
	syear=request.form.get("2011year")
	tyear=request.form.get("2012year")
	lyear=request.form.get("2013year")	
	uyear=request.form.get("2014year")
	with open("countriesData.csv",'a+') as f:
		writer = csv.writer(f)
		writer.writerow([CountryName,'NAN',SeriesName,'NAN',fyear,syear,tyear,lyear,uyear])
	f.close()	
	return redirect(('/1'))

@app.route('/<int:page_num>')
def read_csv(page_num):
	restriction = 5
	def disp(reader,page_num=page_num,restriction=restriction):
		df=[]
		for row in reader:
			if (page_num*restriction>=reader.line_num)and(reader.line_num>(page_num-1)*restriction):
				df.append(row)
		return df
	with open("countriesData.csv",'r+') as f:
		row_length = len(f.readlines())
		if(row_length%restriction==0):
			pages=row_length/restriction
		else:
			pages = int(ceil(row_length/restriction))+1
	f.close()
	with open("countriesData.csv",'r+') as f:
		reader = csv.reader(f)
		df = disp(reader,page_num,restriction)
	f.close()
	#print "pages is",pages
	return render_template("index.html",df=df,pages=pages,page_num=page_num)'''
