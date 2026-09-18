# SPDX-FileCopyrightText: 2026 OpenCHAMI Contributors
# SPDX-License-Identifier: MIT
#
# See `make rpm-build` for the tag-to-version mapping and how the packaged
# quadlet's image tag is pinned to it.

Name:           local-ca-quadlet
Version:        %{version}
Release:        %{rel}%{?dist}
Summary:        OpenCHAMI local-ca Quadlet units

License:        MIT
URL:            https://github.com/OpenCHAMI/local-ca
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires(post,preun,postun):  systemd

# podman 5.0.0 is the first release whose Quadlet generator enables
# systemd-style *.container.d drop-in directories
Requires:                     podman >= 5.0.0

# NOTE: openchami-acme-quadlet is the ACME client that requests certificates
# from this CA. It is a Suggests because the CA serves any ACME client, and a
# site may drive it with its own.
Suggests:                     openchami-acme-quadlet >= 0.0.1

%description
Podman Quadlet unit files (container + volumes) for running the OpenCHAMI
local step-ca certificate authority as part of an OpenCHAMI deployment.

%prep
%setup -q

%install

# systemd files
install -d %{buildroot}/usr/share/containers/systemd

if ! grep -q '@IMAGE_TAG@' step-ca.container; then
    echo "error: @IMAGE_TAG@ placeholder missing from step-ca.container" >&2
    exit 1
fi

sed "s|@IMAGE_TAG@|v%{version}|" step-ca.container \
    | install -m 644 /dev/stdin %{buildroot}/usr/share/containers/systemd/step-ca.container

install -d %{buildroot}/usr/share/containers/systemd/step-ca.container.d
install -m 644 step-ca.container.d/10-defaults.conf \
    %{buildroot}/usr/share/containers/systemd/step-ca.container.d/

for v in step-ca-home step-ca-db step-root-ca; do
    install -m 644 $v.volume %{buildroot}/usr/share/containers/systemd/$v.volume
done

%files
%license LICENSES/MIT.txt
/usr/share/containers/systemd/step-ca.container
/usr/share/containers/systemd/step-ca.container.d
/usr/share/containers/systemd/step-ca.container.d/10-defaults.conf
/usr/share/containers/systemd/step-ca-home.volume
/usr/share/containers/systemd/step-ca-db.volume
/usr/share/containers/systemd/step-root-ca.volume

%post
# reload systemd so the new Quadlet-generated unit is seen
systemctl daemon-reload || :
if [ $1 -ge 2 ]; then
    systemctl try-restart step-ca.service || :
fi

%preun
if [ $1 -eq 0 ]; then
    systemctl stop step-ca.service >/dev/null 2>&1 || :
fi

%postun
# reload systemd so the removed unit is dropped
systemctl daemon-reload || :
