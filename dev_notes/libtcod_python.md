

# Libtcode

## Install 

```bash
brew install autoconf automake pkg-config sdl2
wget https://bitbucket.org/libtcod/libtcod/downloads/20170226-libtcod-1.6.3.tbz2
tar xf 20170226-libtcod-1.6.3.tbz2 
cd 20170226-libtcod-1.6.3

cd build/autotools/
autoreconf -i
./configure

make
cd ../..
```

## Make your project 

Now you're ready to make a directory for your new project, copy the compiled library and links, plus the python library and a font into it:


```bash
mkdir -p /Volumes/WORK/WORK/tcod_tutorial
cp -R build/autotools/.libs/libtcod.* python/libtcodpy data/fonts/arial10x10.png  /Volumes/WORK/WORK/tcod_tutorial
cd /Volumes/WORK/WORK/tcod_tutorial
```


