# Gnome-clocks-3.28.0-1.el8.x86_64.rpm

There is no official `gnome-clocks` for RHEL8 and thus the world clock is missing. This is repackaged version working on RHEL8.

## Before - screenshot
![alt text](https://github.com/luckylittle/GNOME-Clocks-for-RHEL8/blob/master/tmp/before.png?raw=true)

## After - screenshot
![alt text](https://github.com/[username]/GNOME-Clocks-for-RHEL8/blob/master/tmp/after.png?raw=true)


## Installation

```bash
sudo dnf install -y https://github.com/luckylittle/GNOME-Clocks-for-RHEL8/raw/master/RPMS/x86_64/gnome-clocks-3.28.0-1.el8.x86_64.rpm`
```

|Table                |       |
|---------------------|-------|
|Installed packages:  | 2     |
|Total size:          | 466 k |
|Total download size: | 35 k  |
|Installed size:      | 1.4 M |

## Checksum

```text
3f9444bcd054c4deaddd473a06437f2f *gnome-clocks-3.28.0-1.el8.x86_64.rpm
```

## RPM Specfile used to build these packages

https://github.com/luckylittle/GNOME-Clocks-for-RHEL8/raw/master/SPECS/gnome-clocks.spec

## To re-package this

```bash
sudo yum install git rpm-build rpmdevtools
git clone git@github.com:luckylittle/GNOME-Clocks-for-RHEL8.git ~/rpmbuild
echo -e "%_topdir %(echo $HOME)/Downloads/rpmbuild\n%_tmppath %(echo $HOME)/Downloads/rpmbuild/tmp\n" > ~/.rpmmacros
cd ~/rpmbuild
rpmbuild -ba -v SPECS/gnome-clocks.spec
```

## Packager

lmaly@redhat.com

---

_Last update: Mon May 17 11:49:40 UTC 2021_
