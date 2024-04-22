# Local ACME Certificate authority

This repo builds a container that can be used in a docker-compose environment to create a disposable CA and issue/update certificates using certbot.

It is heavily informed by the smallstep authors via https://github.com/smallstep/certificates/blob/master/docker/entrypoint.sh

## Accessing the root cert

The easiest way to obtain the cert for use validating other certs within the environment is to download the pem from the smallstep ca at the well known url: `https://step-ca:9000/roots.pem`.

The next easiest way to obtain the cert is through mounting a docker volume which contains the certificate.  See the docker-compose example below or follow the OpenCHAMI quickstart.


## Docker Compose Usage

This container can be used with docker compose following this example:

```
  step-ca:
    container_name: step-ca
    hostname: step-ca
    image: ghcr.io/openchami/local-ca:v0.1.0
    ports: 
      - "9000:9000"
    networks:
      - openchami-certs
    volumes:
      - ./configs/step-ca/:/home/step
      # Keeping the database in a volume improves performance.  I don't understand why.
      - step-ca-db:/home/step/db
      # Keeping the root CA in a volume allows us to back it up and restore it.
      - step-root-ca:/root_ca/
    environment:
      # To initialize your CA, modify these environment variables
      - STEPPATH=/home/step
      - DOCKER_STEPCA_INIT_NAME=OpenCHAMI
      - DOCKER_STEPCA_INIT_DNS_NAMES=localhost,step-ca
      - DOCKER_STEPCA_INIT_ACME=true
    healthcheck:
      test: ["CMD", "step", "ca", "health", "--ca-url", "https://step-ca:9000", "--root", "/root_ca/root_ca.crt"]
      interval: 10s
      timeout: 10s
      retries: 5
  certbot-issue-cert:
    container_name: certbot
    hostname: certbot
    image: certbot/certbot:v2.10.0
    depends_on:
      step-ca:
        condition: service_healthy
    environment:
      - REQUESTS_CA_BUNDLE=/root_ca/root_ca.crt # This is the root CA certificate that we use to verify the local CA.
    command: [ "certonly", "--webroot", "--server", "https://step-ca:9000/acme/acme/directory", "--webroot-path", "/var/www/html", "--agree-tos", "--email", "docker-compose@example.com", "-d", "openchami.bikeshack.dev", "-n" ]
    networks:
      - openchami-certs
    volumes:
      - local-certs:/etc/letsencrypt
      - certbot-challenges:/var/www/html/
      - step-root-ca:/root_ca:ro
```

Build Status: [![build and publish containers](https://github.com/OpenCHAMI/local-ca/actions/workflows/build_containers.yml/badge.svg)](https://github.com/OpenCHAMI/local-ca/actions/workflows/build_containers.yml)