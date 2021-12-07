#!/bin/bash
# by Nicola Leoni on SO
# extracts the timestamps of the commits to keep (the last of the day)
export TOKEEP=`mktemp`
DATE=
for time in `git log --date=raw --pretty=format:%cd|cut -d\  -f1` ; do
   CDATE=`date -d @$time +%Y%m%d`
   if [ "$DATE" != "$CDATE" ] ; then
       echo @$time >> $TOKEEP
       DATE=$CDATE
   fi
done

# scan the repository keeping only selected commits
git filter-branch -f --commit-filter '
    if grep -q ${GIT_COMMITTER_DATE% *} $TOKEEP ; then
        git commit-tree "$@"
    else
        skip_commit "$@"
    fi' HEAD
rm -f $TOKEEP

git add . 
git push origin main -f