#!/bin/sh

# Simple script to check if current week has been installed.

weekly=`/usr/bin/date +"w_%Y_%U"`
echo "Searching for tag $weekly"
source /software/lsstsw/stack/loadLSST.bash
eups list lsst_distrib -t $weekly
estat=$?
if [ $estat == 0 ]; then
    echo "lsst_distrib -t $weekly exists"
    # Optional
    #echo "To set it up, run:"
    #echo "  source /software/lsstsw/stack/loadLSST.bash"
    #echo "  setup lsst_distrib -t $weekly"
else
    echo "lsst_distrib -t $weekly has NOT been installed yet"
fi
