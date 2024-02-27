FROM rockylinux:8.9
RUN dnf install -y python3 python3-pip augeas-libs
RUN python3 -m venv /opt/certbot/
RUN /opt/certbot/bin/pip install --upgrade pip
RUN /opt/certbot/bin/pip install certbot certbot
RUN ln -s /opt/certbot/bin/certbot /usr/bin/certbot

#dynamic stuff, testing manually for now
#RUN step ca bootstrap --ca-url=https://172.17.0.1:8443 --fingerprint=yourfingerprinthere --install

