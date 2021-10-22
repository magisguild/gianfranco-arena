#!/usr/bin/env bash

while read p; do
  $(cd images && curl -O "$p")
done <images.txt
