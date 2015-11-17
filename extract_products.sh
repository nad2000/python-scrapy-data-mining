#!/bin/sh
grep 'INSERT INTO `product`' | sed 's/INSERT INTO `product` VALUES //g; s/(//g; s/);//g; s/)\,/\n/g' 
