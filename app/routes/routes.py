from flask import Blueprint
from app import app

from .indexBlueprint import indexBlueprint
from .downloadBlueprint import downloadBlueprint

#index page
app.register_blueprint(indexBlueprint)

#download controller
app.register_blueprint(downloadBlueprint)