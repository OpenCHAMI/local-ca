FROM rockylinux:8.9
RUN dnf install -y wget
#install step
RUN wget https://dl.smallstep.com/cli/docs-ca-install/latest/step-cli_amd64.rpm
RUN rpm -i step-cli_amd64.rpm
RUN wget https://dl.smallstep.com/certificates/docs-ca-install/latest/step-ca_amd64.rpm
RUN rpm -i step-ca_amd64.rpm
#create PKI/root+intermediate certs
RUN export STEPPATH=/mnt/
#generate CA
step ca init --name="SI" --deployment-type standalone --password-file=/mnt/test --provisioner-password-file=/mnt/test2 --dns="SI.ca,1.2.3.4" --address=":443" --provisioner="njones@lanl.gov"  --remote-management
#need a mountpoint on /mnt
ENTRYPOINT step-ca  --password-file=/mnt/test /mnt/config/ca.json 
