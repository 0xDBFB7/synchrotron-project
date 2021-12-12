
# Debian 9.4

Got a 

```
Base class package "Module::Build" is empty.
```
error.

https://bruceravel.github.io/demeter/documents/SinglePage/demeter_nonroot.html 

is a better install guide.

```
wxwidgets minimums purtted is missing

you will need to re-run makefile.pl after it is installed
install wxsidgets using alien::wxwidgets

perliio:layers not installed

html::entities

Alien::wxWidgets

HTML::Entities
```

got a constant "set apache x.x" error.
unlike https://github.com/bruceravel/demeter/issues/63
installing apache2-dev didn't fix it.


# switched to a 14.04 chroot.

gnuplot needs the "universe" repo.
at some point in the future the chroot script will need the /etc/apt/sources.list to read "old-releases" instead of archive

got an ssl error, needed libssl-dev


now we need larch. Installed larch in the chroot via 'getlarch.sh', which sets up a conda env.

didn't work for some reason, can't be arsed to troubleshoot. Installed python 3.7 using deadsnake ppa


curl https://bootstrap.pypa.io/get-pip.py | sudo python3.7

got an ssl error with 3.7, downgraded to 3.6, this time pip bootstrap worked

then
git clone https://github.com/0xdbfb7/xraylarch.git
python3.6 setup.py install
pip3.6 numpy

no python.h, 
apt install python3.6-dev 
then scipy...
then cython

so, a few hours later, larch_server segfaults. darn!

# Back to the root desktop env.

hitting ctl-c at the apache error allows install to continue. Nice.

everything's brokenn

*oh, it was conda messing things up.* conda deactivate, then got a perl error
Can't locate DemeterBuilder.pm in @INC (you may need to install the DemeterBuilder module)

export PERL5LIB="$PERL5LIB:$PWD"
perl ./Build.PL


okay, that worked! fantastic.


Installed larch in a new conda env larch_env because it needed an updated numpy version.

python 