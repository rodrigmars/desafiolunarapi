from flask import Flask, render_template, request
from desafiolunarapi.routes.resources_route import routes

app = Flask(__name__)

routes(app, render_template, request)
