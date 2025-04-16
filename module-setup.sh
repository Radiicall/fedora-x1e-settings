#!/bin/bash

check() {
    # Always include the module
    return 0
}

depends() {
    # No explicit dependencies
    return 0
}

install() {
    local basedir="/lib/firmware/qcom/x1e80100"

    if [ -d "$basedir" ]; then
        find "$basedir" -type f | while read -r fw; do
            # Get path relative to /lib/firmware
            relpath="${fw#/lib/firmware/}"
            inst_simple "$fw" "/lib/firmware/$relpath"
        done
    fi
}