#!/bin/sh
### Dump CSV from MySQL:
for t in {keywords,metrics,product,searchkey,shop,shopurl} ; do mysql -u root bukalapak <<<"SELECT * INTO OUTFILE '/tmp/$t.csv' FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '\"' LINES TERMINATED BY '\n' FROM $t" ; done
