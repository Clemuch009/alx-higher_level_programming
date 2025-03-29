#!/bin/bash

# Run MySQL command with the database name as an argument
mysql -u root -p -D "$1" -e "SELECT * FROM first_table;"

