FROM cgr.dev/chainguard/wolfi-base
#install step dependencies
RUN apk add wget step step-ca
#need a mountpoint on /mnt, with files password1 and password2 within the base dir
ENV STEPPATH=/mnt/
COPY --chmod=555 init.sh /bin/init.sh
ENTRYPOINT init.sh 

