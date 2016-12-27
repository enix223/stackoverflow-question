#!/bin/bash

if [ $1 == "start" ]
then
pg_ctl -D /usr/local/var/postgres -l /usr/local/var/postgres/server.log start
else
pg_ctl -D /usr/local/var/postgres stop -s -m fast
fi


