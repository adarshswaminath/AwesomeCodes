#!/bin/bash
# this code will download all images present the url
clear
url=$1 #url of site
folder=$2 #folder name  
if [[ ! -n $1 ]]; then
	echo "Parameter Required! "
	echo "[Usage] ./downloader.sh <url> <foldername>"
else
	#grab all image links from the url
	link=$(curl -s $url |grep -Po '(?<=<img src=")[^"]+')
	for eachLink in $link
	do
		if [[ $eachLink == *"https"* || $eachLink == *"http"* ]]; then
			validLink=$eachLink
		else
			# create the full file url
			read -p "Provide the domain name: " dom
			validLink=$dom$eachLink
			echo $validLink
		fi
		wget $validLink --no-verbose -P $folder
	done
fi

