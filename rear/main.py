#!/usr/bin/env python3
# coding=utf-8
# -*- coding: UTF-8 -*-
#uvicorn main:app --reload
from xmlrpc.client import boolean
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pymysql

app = FastAPI()

origins = ["*"]


db_settings = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "admin",
    "password": "",
    "db": "fcu",
    "charset": "utf8",
}

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=[""],
#     allow_headers=[""],
# )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Allows all origins
    allow_credentials=True,
    allow_methods=["*"], # Allows all methods
    allow_headers=["*"], # Allows all headers
)

c = pymysql.connect(**db_settings)
cursor = c.cursor(pymysql.cursors.DictCursor)
cursor2 = c.cursor()


def checkaccount(account):
    command = f"SELECT COUNT(*) FROM `user` WHERE `account` = \"{account}\""
    cursor2.execute(command)
    r1 = cursor2.fetchall()
    if(boolean(r1[0][0])):
        return False
    else:
        return True



@app.get('/')
def index():
    print("on")

@app.get("/signup/{account}/{password}/{email}/{phone}")
async def signup(account, password, email, phone):
    flag = checkaccount(account)
    print(flag)
    if(flag):
        command = f"INSERT INTO `user` (`account`, `password`, `email`, `phone`) VALUES (\"{account}\", \"{password}\", \"{email}\", \"{phone}\");"
        print(command)
        cursor2.execute(command)
        c.commit()
        return "S"
    else:
        return "F"

@app.get("/login/{account}/{password}")
def login(account, password):
    flag = checkaccount(account)
    if(flag):
        return "U"    
    else:
        command = f"SELECT password FROM user WHERE account=\"{account}\";"
        print(command)
        cursor2.execute(command)
        r = cursor2.fetchone()
        if(str(r[0]) != password):
            return "F" 
        else:
            return account

@app.get("/new/{name}/{price}/{detail}/{img_url}")
def new(name, price, detail, img_url):
    command = f"SELECT MAX(id) FROM products"
    cursor2.execute(command)
    r = cursor2.fetchone()
    print(r)
    print(type (r[0]))
    id=r[0]+1
    command = f"INSERT INTO `products` (`name`, `price`, `detail`,`img_url`, `id`) VALUES (\"{name}\", \"{price}\", \"{detail}\",\"{img_url}\", \"{id}\");"
    cursor2.execute(command)
    c.commit()
    return "newS"


@app.get("/products")
def getProducts():
    command = f"SELECT * FROM products"
    cursor.execute(command)
    r = cursor.fetchall()
    c.commit()
    print(type(r))
    return r
#getProducts()

@app.get("/del/{id}")
def delProducts(id):
    command = f"DELETE FROM products WHERE id = \"{id}\""
    cursor.execute(command)
    c.commit()
    return "DEL"

@app.get("/edit/{id}/{name}/{price}/{detail}")
def editProducts(id, name, price, detail):
    command = f"UPDATE products SET name=\"{name}\",price=\"{price}\",detail=\"{detail}\" WHERE id =\"{id}\""
    cursor.execute(command)
    c.commit()
    print("EDIT")
    return "EDIT"

@app.get("/search/{key}")
def editProducts(key):
    command = f"SELECT * FROM products WHERE name LIKE '%{key}%'"
    cursor.execute(command)
    r = cursor.fetchall()
    c.commit()
    print(r)
    return r

@app.get("/cartdata/{cartlist}")
def getcartdata(cartlist):
    command = f"SELECT * FROM products WHERE id IN({cartlist})"
    print(command)
    cursor.execute(command)
    r = cursor.fetchall()
    c.commit()
    print(r)
    return r

c.commit()
#'http://localhost:8000/cartdata'+'/'+ this.getId
#'http://localhost:8000/products/' + key
#'http://localhost:8000/edit/' + id +'/' + this.editedData.newName + '/' + this.editedData.img_url + '/' + this.editedData.price + '/' + this.editedData.detail
#'http://localhost:8000/del/' + delname
#'http://localhost:8000/products'
#'http://localhost:8000/new/' + this.arr.name + '/' + this.arr.img_url  + '/' + this.arr.price  + '/' + this.arr.detail
#'http://localhost:8000/login/' + this.account + '/' + this.password
#'http://localhost:8000/checkaccount/' + this.account