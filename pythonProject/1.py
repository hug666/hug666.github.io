from flask import Flask, session, g
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from functools import wraps
from alembic import context
import logging
from logging.config import fileConfig
from flask import current_app
import wtforms
from wtforms.validators import length, email, EqualTo, InputRequired
from flask import Blueprint, render_template, request, g, redirect, url_for, flash
from sqlalchemy import or_
from flask import Blueprint, render_template, request, redirect, url_for, jsonify, session, flash
from flask_mail import Message
import string
import random
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime