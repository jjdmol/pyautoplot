#!/bin/bash
# This cript is to be called from lfe001 and will launch msplots
# instances on all non-developer compute nodes. Any arguments are passed
# directly to the msplots instances.
# cexec1 is used because it allows us to address each lce node by the same
# number as in its name. The script assumes that msplots is in the PATH
# and that the pyautoplot module is in the PYTHONPATH.

HOSTNAME=`hostname -s`
if test "$HOSTNAME" == "lhn001"; then
    cexec locus: "bash -ilc \"msplots $@\""

    result=`create_html.csh $@ >& /dev/null; echo $?`
    if [ $result ]; then 
        echo "Problem creating HTML overview"
    fi
    echo "Done"
else
    cexec1 lce:1-54,64-72 "bash -ilc \"use LofIm;use Pythonlibs; use Pyautoplot; msplots $@\""
fi

