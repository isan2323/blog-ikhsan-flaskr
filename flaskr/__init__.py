# import aplikasi flask untuk dipakai di web kita
import os

# import SQL utk akses databse
from cs50 import SQL 
# import flash utk notifikasi pada web
# import jsonify utk memformat data
# import redirect dan render_template untuk berpindah halaman web
# import request dan session untuk mengakses data
# from flask import Flask, flash, jsonify, redirect, render_template, request, session
@app.route("/login")
def login():
    return 'halaman login'