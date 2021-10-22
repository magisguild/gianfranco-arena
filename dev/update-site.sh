#!/bin/zsh

rm ../style.*.css
rm ../main.*.js
rm ../main.*.js.map
cp dist/*.* ../
cp -r dist/images/* ../images
cp -r dist/images/favicons/* ../images/favicons
cp -r dist/fonts ../fonts
cp -r dist/filters/* ../filters
cd ..
git add .
git status
git commit -am "update site"
git push
