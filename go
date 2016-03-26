#!/bin/bash
while true 
do
    make sync
    make -j4 encode
    sleep 100
done
