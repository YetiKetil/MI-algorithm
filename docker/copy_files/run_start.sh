#!/bin/bash

flask run --host=0.0.0.0 > /var/log/text-similiarity/flask.out

#postgresql-setup initdb
#systemctl start postgresql

#rm -f /local-git/logic/app.db
#sqlite3 /local-git/logic/app.db "CREATE TABLE test (id int, text1 varchar(1000), text2 varchar(1000), score real, timestamp datetime);"
