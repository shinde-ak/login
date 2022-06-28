from flask import Flask, jsonify, redirect, request, session
from passlib.hash import pbkdf2_sha256
from mongoo import db
import uuid


class User:

    def session_st(self, user):
        session['login'] = True
        session['user'] = user
        return jsonify(user), 200

    def user(self):
        return jsonify([doc for doc in db.users.find()])

    def signup(self):

        user = {
            "_id": uuid.uuid4().hex,
            "name": request.form.get('name'),
            "email": request.form.get('email'),
            "password": request.form.get("password")
        }

        user['password'] = pbkdf2_sha256.encrypt(user["password"])
        if(db.users.find_one({"email": user["email"]})):
            return jsonify({"error": " Email already exists"}), 400
        if db.users.insert_one(user):
            return self.session_st(user)
            # return jsonify(user),200
        return jsonify({"error": "sign up failed.."})

    def signout(self):
        session.clear()
        return redirect('/')

    def login(self):

        user = db.users.find_one({
        "email": request.form.get('email')
        })

        if user and pbkdf2_sha256.verify(request.form.get('password'), user['password']):
            return self.session_st(user)

        return jsonify({"error": "Invalid login credentials"}), 401
