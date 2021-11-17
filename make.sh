# shellcheck disable=SC1113
#/bin/bash
./autogen.sh
./configure
make
cd src && chmod +x mentohust
sudo cp mentohust /usr/local/bin/
echo "已完成编译!"