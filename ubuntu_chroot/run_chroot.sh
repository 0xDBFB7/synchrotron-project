MY_CHROOT=/home/arthurdent/chroots/$1

umount -lf $MY_CHROOT/proc
umount -lf $MY_CHROOT/sys
umount -lf $MY_CHROOT/tmp/

mount proc $MY_CHROOT/proc -t proc
mount sysfs $MY_CHROOT/sys -t sysfs
mount --bind $MY_CHROOT/tmp/ /tmp/


cat $1.folders | while read line
do
    [ -z "$line" ] && continue
    echo "$MY_CHROOT/$line"
    mkdir -p $MY_CHROOT/$line
    mount --bind $line $MY_CHROOT/$line
    # this binds the content in /some/where to /else/where.
    # that is, binds data *outside*  *into* the chroot.
    
done

xhost +local:

#mount --bind $MY_CHROOT/root/opt/openEMS/ /home/arthurdent/Programs/OpenEMS
#mount --bind $MY_CHROOT/openEMS-Project/ /home/arthurdent/Programs/OpenEMS-Project
# source /etc/profile
# source ~/.bashrc
# export PS1="(chroot) $PS1"

echo ". \"$HOME/.bashrc\"; ls" > initfile  # doesn't seem to be working.
# echo "export PS1=\"(chroot) $PS1\"" >> initfile 

chroot $MY_CHROOT /bin/bash --init-file initfile


umount -lf $MY_CHROOT/proc
umount -lf $MY_CHROOT/sys

#umount /home/arthurdent/Programs/OpenEMS



cat $1.folders | while read line 
do
    [ -z "$line" ] && continue
    umount $MY_CHROOT/$line
    # umount $line
done

umount -lf $MY_CHROOT/tmp/
#

