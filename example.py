#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

__author__ = "Davi Garcia"
__email__ = "davigar@cisco.com"
__version__ = "1.0"

import socket
from flask import Flask
from datetime import datetime

app = Flask(__name__)
instance_address = socket.gethostbyname(socket.gethostname())

@app.route('/')
def hello():
    "Function to handle root route."
    return """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Cisco Live Cancun 2015 - DEVNET-1019</title>
        </head>
        <body>
            <h1>Hello world, Cisco Live Cancun 2015!</h1>
            <p><b>Current date:</b> %s</p>
            <p><b>Host:</b> %s<p>
        </body>
    </html> """ % (datetime.now(), instance_address)
