#!/bin/sh
# SPDX-FileCopyrightText: © 2024 Triad National Security, LLC.
# SPDX-FileCopyrightText: © 2026 OpenCHAMI a Series of LF Projects, LLC
#
# SPDX-License-Identifier: MIT
PWDPATH="${PWDPATH:-/home/step/secrets/password}"
CONFIGPATH="${CONFIGPATH:-/home/step/config/ca.json}"

export STEPPATH="${STEPPATH:-/home/step}"

/usr/bin/step-ca --password-file "$PWDPATH" "$CONFIGPATH"
