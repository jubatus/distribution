#!/bin/sh

git clone https://github.com/pfi/pficommon.git
# sh tools/deb.sh

cd pficommon
./waf configure
#./waf --check
./waf dist
mv pficommon-1.3.1.tar.bz2 ..
cd ..
tar xjf pficommon-1.3.1.tar.bz2
#tar czf pficommon-orig.1.3.1.tar.gz pficommon-1.3.1
#cp -r tools/debian jubatus-0.2.1
cd pficommon-1.3.1
mkdir debian/
cp ../rules ../control debian/
cp ../include-binaries debian/source/
dh_make -f ../pficommon-1.3.1.tar.bz2 -e uenishi.kota@lab.ntt.co.jp -c bsd -l -a
dpkg-buildpackage -rfakeroot
