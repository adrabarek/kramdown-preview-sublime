#! /usr/bin/env sh

zip KramdownRender * -x "res/*" "create_package.sh"
mv KramdownRender.zip KramdownRender.sublime-package