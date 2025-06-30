#!/bin/bash
grep "signature_" /var/log/nginx/access.log | awk '{print $1, $4, $7}'
