# ===============LICENSE_START=======================================================
# Acumos Apache-2.0
# ===================================================================================
# Copyright (C) 2018 AT&T Intellectual Property. All rights reserved.
# ===================================================================================
# This Acumos software file is distributed by AT&T
# under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# This file is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ===============LICENSE_END=========================================================

from flask import abort
from http import HTTPStatus


def error_response(status_code, message):
    response = {}
    abort(status_code, message, **response)


def bad_request(message):
    status_code = HTTPStatus.BAD_REQUEST.value
    error_response(status_code, message)


def not_found(message=None):
    if message is None:
        message = HTTPStatus.NOT_FOUND.phrase
    status_code = HTTPStatus.NOT_FOUND.value
    error_response(status_code, message)


def created_response(body, additional_headers=None):
    if additional_headers:
        return body, HTTPStatus.CREATED.value, additional_headers
    return body, HTTPStatus.CREATED.value

def no_content_response():
    return '', HTTPStatus.NO_CONTENT.value
