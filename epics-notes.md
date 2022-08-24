https://epics-controls.org/resources-and-support/modules/soft-support/
https://epics.anl.gov/modules/manufacturer.php

```
arthurdent@T42-Debian:~$ lsb_release -a
No LSB modules are available.
Distributor ID:	Debian
Description:	Debian GNU/Linux 8.10 (jessie)
Release:	8.10
Codename:	jessie
arthurdent@T42-Debian:~$ 

```

USPAS accelerator virtualbox 13
https://controlssoftware.sns.ornl.gov/training/2019_USPAS/#prep


followed Getting Started instructions on 
https://epics.nsls2.bnl.gov/debian/#starting

<gpg key expired error, ignored and installed anyhow>

using qemu would be one option
(sudo usermod -aG vboxsf $USER) for vbox shared folder


---- 

Installed EPICS R3.14.12.4 from https://epics.anl.gov/base/R3-14/12.php - easy; wget, tar, make.

Followed https://www.aps.anl.gov/BCDA/synApps to install synapps. Edited the SUPPORT and BASE dirs in support/configure/RELEASE.

Got an error compiling synapps 5_7 with 12.4:

> **make[3]: *** No rule to make target `../../lib/linux-x86_64/librecIoc.a', needed by `libdevIocStats.a'.  Stop.
**

Upgraded to sunapps 7_8, compiling yielded a different error:

> make[4]: re2c: Command not found
make[4]: Leaving directory `/home/arthurdent/EPICS/synApps_5_8/support/seq-2-2-1/src/snc/O.linux-x86_64'
make[4]: Entering directory `/home/arthurdent/EPICS/synApps_5_8/support/seq-2-2-1/src/snc/O.linux-x86_64'
re2c -s -b -o lexer.c ../snl.re
make[4]: re2c: Command not found

Installed re2c with wget http://dl.fedoraproject.org/pub/epel/7/x86_64/Packages/r/re2c-0.14.3-2.el7.x86_64.rpm 
tar -Uvh

And then again we get

> make[4]: *** No rule to make target `../../../lib/linux-x86_64/librecIoc.a', needed by `snc'.  Stop.


According to https://epics.anl.gov/bcda/synApps/synApps.html I don't need to set EPICS_BASE.<arch<.

[This page](https://epics.anl.gov/base/R3-14/11-docs/README.html) describes what the different files (RELEASE, RULES) do. 




