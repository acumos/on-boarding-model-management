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

from setuptools import setup, find_packages

version = __import__('acumos_model_management').get_version()

with open("README.md") as fd:
    long_description = fd.read()

setup(
    author='Pavel Kazakov',
    author_email='pk9069@att.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: 6ython :: 3.7',
        'License :: OSI Approved :: Apache Software License',
    ],
    description='Acumos Model Management for maintaining persistent model files',
    install_requires=['Flask>=1.0.2',
                      'flask-restplus>=0.11.0',
                      'flask-mongoengine>=0.9.5',
                      'gunicorn>=19.9.0',
                      'flask-cors>=3.0.6',
                      'pytz>=2018.5'],
    keywords='acumos machine learning model model management server ml ai',
    license='Apache License 2.0',
    long_description=long_description,
    name='acumos_model_management',
    packages=find_packages(),
    python_requires='>=3.4',
    url='https://gerrit.acumos.org/r/gitweb?p=on-boarding/model-management.git',
    version=version,
)
