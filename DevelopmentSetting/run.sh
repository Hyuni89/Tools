#!/bin/sh

OS=`uname`

if [ $OS = "Linux" ]; then
	echo "Only work in Debian Linux"
	sudo apt install update
	sudo apt install upgrade
	sudo apt install vim vim-gnome

	ln -s vimrc ~/.vimrc
elif [ $OS = "Dawin" ]; then
	echo "Mac"

	ln -s vimrc4mac ~/.vimrc
else
	exit
fi

