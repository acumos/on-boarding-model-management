# ===============LICENSE_START=======================================================
# Acumos Apache-2.0
# ===================================================================================
# Copyright (C) 2017-2018 AT&T Intellectual Property. All rights reserved.
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

FROM dockercentral.it.att.com:5100/com.att.cmlp.public/cmlppython:3.6
ADD properties /opt/app/microservice/properties
ADD acumos_model_management /opt/app/microservice/acumos_model_management
ADD wsgi.py README.md setup.py setup.cfg run.py start-apsc-server.sh /opt/app/microservice/
RUN chmod 777 -R /root
EXPOSE 8081
ENTRYPOINT /opt/app/microservice/start-apsc-server.sh
