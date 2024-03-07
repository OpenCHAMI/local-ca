FROM rockylinux:8.9
RUN dnf install -y python3 python3-pip augeas-libs
RUN python3 -m venv /opt/certbot/
RUN /opt/certbot/bin/pip install --upgrade pip
RUN /opt/certbot/bin/pip install certbot certbot
RUN ln -s /opt/certbot/bin/certbot /usr/bin/certbot
RUN dnf install -y wget 
RUN wget https://dl.smallstep.com/cli/docs-ca-install/latest/step-cli_amd64.rpm
RUN rpm -i step-cli_amd64.rpm
#this sed is needed to make certbot actually function with step-ca
RUN sed -i 's/csr.set_version(2)/csr.set_version(0)/' /opt/certbot/lib/python3.6/site-packages/acme/crypto_util.py

#dynamic stuff, testing manually for now. long term this should go in an init
#step ca bootstrap --ca-url=https://172.17.0.1:8443 --fingerprint=yourfingerprinthere --install
#REQUESTS_CA_BUNDLE=$(step path)/certs/root_ca.crt certbot certonly --register-unsafely-without-email --agree-tos -n --standalone -d certbot.local --server https://SI.ca/acme/acme/directory
