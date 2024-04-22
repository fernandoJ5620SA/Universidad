from flask import render_template, request, redirect, url_for, flash, session
from src.database.conexcionDB import *


def auth_user():
    print("login")
