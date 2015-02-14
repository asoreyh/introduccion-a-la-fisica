# 
# vie jun 20 08:40:29 COT 2014
#

sudo apt-get -y update
sudo apt-get -y dist-upgrade

# virtualbox guest additions
sudo apt-get -y install virtualbox virtualbox-guest-additions-iso virtualbox-guest-utils virtualbox-guest-x11  virtualbox-guest-dkms

# basic stuff
sudo apt-get -y install vim rsync screen chromium-browser

# generic packages
sudo apt-get -y install xorg xorg-dev openssh-server dc libx11-dev tasksel aptitude emacs23 libreadline-gplv2-dev traceroute ntp mysql-client nfs-common

# science
sudo apt-get install -y cernlib python-scipy ipython python-matplotlib imagemagick gnuplot gnuplot-x11 astyle pdl fftw-dev libhdf4-alt-dev hdf4-tools python-numpy gsl-bin spyder

# Compiler
sudo apt-get -y install m4 automake autoconf autoconf2.13 autoconf2.59 autoconf2.64 gnu-standards autotools-dev autoconf-archive automake1.11 automake1.9 cvs subversion mercurial manpages-dev gfortran build-essential libgd2-xpm-dev fort77 cmake libboost-all-dev

sudo apt-get -y autoremove
sudo apt-get -y clean
sudo apt-get -y autoclean

# General
sudo apt-get -y install texmaker texlive-lang-spanish texlive-fonts-recommended pepperflashplugin-nonfree

sudo apt-get -y install texlive latex-beamer latex-xcolor texlive-base texlive-fonts-recommended texlive-lang-spanish perl-tk texlive-pstricks texlive-latex-extra texlive-latex-recommended texlive-bibtex-extra texlive-fonts-extra texlive-generic-extra texlive-publishers gv plotutils xpdf a2ps xpp libmikmod2 texlive-humanities lmodern texmaker pepperflashplugin-nonfree


sudo apt-get -y autoremove
sudo apt-get -y clean
sudo apt-get -y autoclean

# tracker
sudo apt-get -y install openjdk-7-jre icedtea-7-plugin
wget -c https://www.cabrillo.edu/~dbrown/tracker/installers/Tracker-4.85-linux-32bit-installer.run
chmod 755 Tracker-4.85-linux-32bit-installer.run
sudo ./Tracker-4.85-linux-32bit-installer.run

#cvs -d:pserver:anonymous@gnuplot.cvs.sourceforge.net:/cvsroot/gnuplot login
# cvs -z3 -d:pserver:anonymous@gnuplot.cvs.sourceforge.net:/cvsroot/gnuplot co -P gnuplot

wget -c ftp://root.cern.ch/root/root_v5.34.18.source.tar.gz
tar xfv root_v5.34.18.source.tar.gz
sudo mv root /opt

echo "Now install gnuplot, root, and download and  install google earth www.google.es/intl/es_es/earth/"

