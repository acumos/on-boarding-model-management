FROM dockercentral.it.att.com:5100/com.att.cmlp.public/cmlppython:3.6
ADD properties /opt/app/microservice/properties
ADD acumos_model_management /opt/app/microservice/acumos_model_management
ADD wsgi.py README.md setup.py setup.cfg run.py start-apsc-server.sh /opt/app/microservice/
RUN chmod 777 -R /root
EXPOSE 8081
ENTRYPOINT /opt/app/microservice/start-apsc-server.sh
