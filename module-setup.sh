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
    for base in /lib/firmware /lib/firmware/updates; do
        local basedir="$base/qcom/x1e80100"

        if [ -d "$basedir" ]; then
            find "$basedir" -type f | while read -r fw; do
                # Get path relative to the firmware root
                relpath="${fw#${base}/}"
                inst_simple "$fw" "$base/$relpath"
            done
        fi
    done
}