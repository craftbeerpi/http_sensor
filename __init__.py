# -*- coding: utf-8 -*-
import os
from subprocess import Popen, PIPE, call

from modules import cbpi
from modules.core.hardware import ActorBase, SensorPassive, SensorActive
import json
from flask import Blueprint, render_template, jsonify, request
from modules.core.props import Property

blueprint = Blueprint('http_sensor1', __name__)
cache = {}

@cbpi.sensor
class HTTPSensor(SensorActive):
    key = Property.Text(label="Key", configurable=True)
    def execute(self):
        global cache
        while self.is_running():
            try:
                value = cache.pop(self.key, None)
                if value is not None:
                    self.data_received(value)
            except:
                pass
            self.api.socketio.sleep(1)

@blueprint.route('/<id>/<value>', methods=['GET'])
def set_temp(id, value):
    global cache
    cache[id] = value
    return ('', 204)

@cbpi.initalizer()
def init(cbpi):
    print "INITIALIZE HTTP SENSOR MODULE"
    cbpi.app.register_blueprint(blueprint, url_prefix='/api/httpsensor')
    print "READY"