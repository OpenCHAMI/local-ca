FROM rockylinux:8.9
RUN dnf install -y wget
#install step
RUN wget https://dl.smallstep.com/cli/docs-ca-install/latest/step-cli_amd64.rpm
RUN rpm -i step-cli_amd64.rpm
RUN wget https://dl.smallstep.com/certificates/docs-ca-install/latest/step-ca_amd64.rpm
RUN rpm -i step-ca_amd64.rpm
ENV STEPPATH=/mnt/

#dynamic stuff, testing manually for now. long term this should go in an init
#the ip address in this init should probably be dynamic from the env
#for now, you can change the entrypoint to the below command
#step ca init --name="SI" --deployment-type standalone --password-file=/mnt/password1 --provisioner-password-file=/mnt/password2 --dns="SI.ca,172.17.0.1" --address=":443" --admin"  --remote-management --acme

#need a mountpoint on /mnt, with files password1 and password2 within the base dir
ENTRYPOINT step-ca  --password-file=/mnt/test /mnt/config/ca.json 
