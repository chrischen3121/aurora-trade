#!/usr/bin/env sh
set -u -o pipefail
# install conan via pipx or pip
if [ -x "$(command -v pipx)" ]; then
    pipx install conan
else
    pip install --user conan
fi

# if conan "gnu20" profile does not exist, create one
if ! conan profile path gnu20 ; then
    conan profile detect --name=gnu20
    PROFILE_PATH=$(conan profile path gnu20)
    sed -i 's/compiler\.cppstd=[^ ]*/compiler.cppstd=gnu20/g' $PROFILE_PATH
fi
conan install . -pr gnu20 --output-folder=build --build=missing
