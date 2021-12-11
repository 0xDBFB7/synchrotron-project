# run with sudo
MY_CHROOT=$PWD/chroot_root
debootstrap trusty $MY_CHROOT http://archive.ubuntu.com/ubuntu/

#https://askubuntu.com/questions/91815/how-to-install-software-or-upgrade-from-an-old-unsupported-release

#echo "proc $MY_CHROOT/proc proc defaults 0 0" >> /etc/fstab
#echo "sysfs $MY_CHROOT/sys sysfs defaults 0 0" >> /etc/fstab

cp /etc/hosts $MY_CHROOT/etc/hosts
cp /proc/mounts $MY_CHROOT/etc/mtab

chmod -R 777 $MY_CHROOT



#then 
# apt update 
# apt install bash-completion

#put alias sudo="" in .bashrc
#
