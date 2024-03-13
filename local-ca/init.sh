if ! [ -f /mnt/password1 -a -f /mnt/config/ca.json ]
then
  echo $(tr -dc 'A-Za-z0-9!"#$%&'\''()*+,-./:;<=>?@[\]^_`{|}~' </dev/urandom | head -c 30;) > /mnt/password1
  echo $(tr -dc 'A-Za-z0-9!"#$%&'\''()*+,-./:;<=>?@[\]^_`{|}~' </dev/urandom | head -c 30;) > /mnt/password2
  step ca init --name="SI" --deployment-type standalone --password-file=/mnt/password1 --provisioner-password-file=/mnt/password2 --dns="SI.ca" --address=":443" --provisioner="admin"  --remote-management --acme
fi
step-ca --password-file=/mnt/password1 /mnt/config/ca.json

