#!/bin/bash
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 \$org \$activation_key"
    exit 1
fi
echo "{\"org\":\"$1\",\"key\":\"$2\"}" | base64
