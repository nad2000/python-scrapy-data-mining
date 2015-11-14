#!/bin/sh
## EXtract relevant product entries w/o duplicates:
sqlite3 db.db "SELECT id, title, url FROM product WHERE id IN (SELECT max(id) AS id FROM product WHERE url LIKE '%bukalapak%' AND title IS NOT NULL AND title != '' GROUP BY url)" -csv > corpus.csv
