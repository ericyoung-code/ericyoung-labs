#!/bin/bash

if grep -q '^PermitRootLogin no' /etc/ssh/sshd_config; then
  echo 'PASS: Root login disabled'
else
  echo 'FAIL: Root login still enabled'
fi