FROM cgr.dev/chainguard/wolfi-base
#install step dependencies
RUN apk add --no-cache wget step step-ca bash

ENV CONFIGPATH="/home/step/config/ca.json"
ENV PWDPATH="/home/step/secrets/password"
ENV STEPPATH="/home/step"

RUN mkdir /root-ca

VOLUME ["/home/step", "/root-ca"]

# The entrypoint script will generate the certificate and export the root cert to the /root-ca volume

STOPSIGNAL SIGTERM
HEALTHCHECK CMD step ca health 2>/dev/null | grep "^ok" >/dev/null

COPY entrypoint.sh /entrypoint.sh

EXPOSE 9000/TCP

ENTRYPOINT ["/bin/bash", "/entrypoint.sh"]
CMD exec /usr/bin/step-ca --password-file $PWDPATH $CONFIGPATH
