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

# brew install
# /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

# iterm2 install
# brew cask install iterm2

# sudo apt install zsh
# brew install zsh zsh-completions
# sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

# zsh plugin
# zsh-syntax-highlighting
# git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
# zsh-autosuggestions
# git clone git://github.com/zsh-users/zsh-autosuggestions $ZSH_CUSTOM/plugins/zsh-autosuggestions
# add ~/.zshrc
# plugins=(
#   git
#   zsh-syntax-highlighting
#   zsh-autosuggestions
# )

# SpaceVim
# curl -sLf https://spacevim.org/install.sh | bash

# Vundle
# git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim

