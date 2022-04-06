from flask import Flask, render_template, request
import controller
import numpy
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    pluckers = controller.get_all_pluckers()
    return render_template('all_pluckers.html', **locals())

@app.route('/<plucker_id>', methods=['GET'])
def plucker(plucker_id):
    plucker_id = plucker_id
    points = controller.read_points(plucker_id)
    return render_template('plucker.html', **locals())

@app.route('/<plucker_id>', methods=['POST'])
def update_plucker(plucker_id):

    deliver_points = float(request.form["amount"]) * float(request.form["distance"]) / 100
    points = float(controller.read_points(plucker_id)) + deliver_points
    print(points)
    controller.append_to_points(plucker_id, points)
    return plucker(plucker_id)