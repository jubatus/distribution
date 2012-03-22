#!/bin/sh

git clone git://github.com/jubatus/jubatus.git

#./waf configure --disable-re2
#./waf --check
cd jubatus
./waf dist
tar xjf jubatus-0.2.1.tar.bz2
tar czf jubatus-orig.0.2.1.tar.gz jubatus-0.2.1
cp -r ../debian jubatus-0.2.1
cd jubatus-0.2.1
dh_make -f ../jubatus-orig.0.2.1.tar.gz -e uenishi.kota@lab.ntt.co.jp -c lgpl2 -m -a
dpkg-buildpackage -rfakeroot
