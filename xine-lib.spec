#
# Conditional build:
%bcond_without	aalib		# don't build aalib video output plugin
%bcond_without	alsa		# don't build ALSA audio output plugin
%bcond_without	arts		# don't build aRts audio output plugin
%bcond_without	directfb	# don't build DirectFB video output plugin
%bcond_without	dxr3		# don't build dxr3 video output and decode plugins
%bcond_without	esd		# don't build EsounD audio output plugin
%bcond_without	gnome		# don't build gnome_vfs plugin
%bcond_without	opengl		# don't build OpenGL video output plugin
%bcond_without	sdl		# don't build SDL video output plugin
%bcond_without	stk		# don't build stk video output plugin
%bcond_with	xvid		# build xvid decode plugin [disabled in sources at the moment]
#
%ifnarch %{ix86}
%undefine	with_dxr3
%endif

%define		_rc		rc6a
%define		_version	1-%{_rc}

Summary:	A Free Video Player
Summary(ko):	°ø°³ µ¿¿µ»ó ÇÃ·¹ÀÌ¾î
Summary(pl):	Odtwarzacz filmów
Summary(pt_BR):	Xine, um player de video
Name:		xine-lib
Version:	1.0
Release:	0.%{_rc}.4
Epoch:		2
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/xine/%{name}-%{_version}.tar.gz
# Source0-md5:	32b231beb9b2194606a18ed7bcf2bcb3
Patch0:		%{name}-am17.patch
Patch1:		%{name}-automake_as.patch
Patch2:		%{name}-syncfb.patch
Patch3:		%{name}-nolibs.patch
Patch4:		%{name}-sparc.patch
Patch5:		%{name}-win32-path.patch
URL:		http://xine.sourceforge.net/
%{?with_directfb:BuildRequires:	DirectFB-devel >= 0.9.9}
%{?with_opengl:BuildRequires:	OpenGL-devel}
%{?with_sdl:BuildRequires:	SDL-devel}
%{?with_aalib:BuildRequires:	aalib-devel >= 1.3}
%{?with_alsa:BuildRequires:	alsa-lib-devel >= 0.9.0}
%{?with_arts:BuildRequires:	artsc-devel >= 0.9.5}
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1.8.1
%{?with_esd:BuildRequires:	esound-devel >= 0.2.8}
BuildRequires:	flac-devel
BuildRequires:	gettext-devel
%{?with_opengl:BuildRequires:	glut-devel}
%{?with_gnome:BuildRequires:	gnome-vfs2-devel}
BuildRequires:	libcaca-devel
BuildRequires:	libcdio-devel >= 0.64
BuildRequires:	libdvdnav-devel >= 0.1.9
%{?with_dxr3:BuildRequires:	libfame-devel}
BuildRequires:	libmng-devel
BuildRequires:	libmodplug-devel >= 0.7
BuildRequires:	libpng-devel
%{?with_stk:BuildRequires:	libstk-devel >= 0.2.0}
BuildRequires:	libvorbis-devel
BuildRequires:	libtheora-devel
BuildRequires:	libtool >= 0:1.4.2-9
BuildRequires:	pkgconfig
#%{?with_dxr3:BuildRequires:	rte-devel} # only 0.4 supported
BuildRequires:	speex-devel >= 1:1.1.6
BuildRequires:	vcdimager-devel >= 0.7.20-2
%{?with_xvid:BuildRequires:	xvid-devel}
BuildRequires:	zlib-devel
# libtool problem (up to 1.4e)
BuildConflicts:	xine-lib-devel < 1.0
Obsoletes:	xine
Obsoletes:	xine-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1

%define		_pluginsdir	%{_libdir}/xine/plugins/1.0.0

%description
xine is a free gpl-licensed video player for unix-like systems. We
support mpeg-2 and mpeg-1 system (audio + video multiplexed) streams,
eventually mpeg-4 and other formats might be added.

xine plays the video and audio data of mpeg-2 videos and synchronizes
the playback of both. Depending on the properties of the mpeg stream,
playback will need more or less processor power, 100% frame rate has
been seen on a 400 MHz P II system.

%description -l fr
xine est un lecteur vidéo libre sous license GPL pour les systèmes de
type unix. Nous supportons les flux mpeg-2 et mpeg-1 (audio + vidéo
multiplexés), éventuellement le mpeg-4 et d'autres formats peuvent
êtres ajoutés.

xine joue les données vidéo et audio de vidéo mpeg-2 et synchronise la
lecture des deux. En fonction des propriétes du flux mpeg, la lecture
aura besoin de plus ou moins de puissance du processeur, 100% de
restitution de trame a été vus sur un système PII 400MHz.

%description -l ko
xine ´Â GPL¶óÀÌ¼±½º¸¦ µû¸£´Â UNIX¿ë °ø°³ µ¿¿µ»ó ÇÃ·¹ÀÌ¾îÀÔ´Ï´Ù. ÀÌ
ÇÃ·¹ÀÌ¾î´Â mpeg-2 ¿Í mpeg 1 ½ºÆ®¸²À» Áö¿øÇÏ¸ç, ÇöÀç´Â Áö¿øÇÏÁö ¾ÊÁö¸¸
³ªÁß¿¡´Â mpeg-4 ¿Í ´Ù¸¥ Çü½ÄÀÇ µ¿¿µ»óµµ Áö¿øÇÒ ¿¹Á¤ÀÔ´Ï´Ù.

%description -l pl
xine jest wolnodostêpnym odtwarzaczem filmów dla systemów uniksowych.
Obs³uguje strumienie MPEG-2 i MPEG-1 (d¼wiêk oraz obraz), mo¿e byæ
dodana obs³uga MPEG-4 i innych formatów.

xine odczytuje obraz i d¼wiêk z filmów MPEG-2 i synchronizuje ich
odtwarzanie. Zale¿nie od w³a¶ciwo¶ci strumienia MPEG, odtwarzanie mo¿e
wymagaæ wiêcej lub mniej mocy procesora, 100% klatek mo¿e byæ widoczne
na P II 400MHz.

%description -l pt_BR
O xine é um video player GPL para sistemas unix. Lê arquivos MPEG-2 e
MPEG-1, além de AVIs MS MPEG4 / OpenDivX.

O xine lê o conteúdo vídeo e áudio e sincroniza-os em tempo-real. As
necessidades de processador dependem das propriedades de cada arquivo.

%package devel
Summary:	XINE - development files
Summary(pl):	Pliki dla programistów XINE
Summary(pt_BR):	XINE - arquivos de desenvolvimento
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	xine-devel

%description devel
HTML documentation of XINE API and development components.

%description devel -l pl
Pliki dla programistów oraz dokumentacja HTML do API XINE.

%description devel -l pt_BR
Arquivos include a bibliotecas estáticas necessárias para compilar
plugins para o xine e o xine-ui.

%package -n xine-decode-flac
Summary:	XINE - FLAC decoder plugin
Summary(pl):	XINE - wtyczka dekodera FLAC
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n xine-decode-flac
XINE - FLAC decoder/demuxer plugin.

%description -n xine-decode-flac -l pl
XINE - wtyczka dekodera i demuxera FLAC.

%package -n xine-decode-ogg
Summary:	XINE - Ogg/Vorbis, Ogg/Speex, Ogg/Theora decoder plugins
Summary(pl):	XINE - wtyczki dekoderów Ogg/Vorbis, Ogg/Speex, Ogg/Theora
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	xine-decode-vorbis

%description -n xine-decode-ogg
XINE Ogg/Vorbis, Ogg/Speex, Ogg/Theora decoding plugins: Ogg demuxer,
Vorbis, Speex and Theora decoders.

%description -n xine-decode-ogg -l pl
Wtyczki XINE dekoduj±ce Ogg/Vorbis, Ogg/Speex, Ogg/Theora: demuxer Ogg
oraz dekodery Vorbis, Speex, Theora.

%package -n xine-decode-w32dll
Summary:	XINE - win32dll decoder support
Summary(pl):	XINE - obs³uga dekodera win32dll
Summary(pt_BR):	XINE - suporte a decoder win32dll
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	w32codec
Obsoletes:	xine-lib-w32dll

%description -n xine-decode-w32dll
XINE win32dll decoder support.

%description -n xine-decode-w32dll -l pl
Obs³uga dekodera win32dll do XINE.

%description -n xine-decode-w32dll -l pt_BR
Suporte a win32dll para o xine.

%package -n xine-decode-xvid
Summary:	XINE - xvid DIVX decoding support
Summary(pl):	XINE - obs³uga dekodera DIVX xvid
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	xine-lib-xvid

%description -n xine-decode-xvid
XINE decoder plugin for DIVX decoding with xvid library.

%description -n xine-decode-xvid -l pl
Wtyczka dla XINE do dekodowania DIVX poprzez bibliotekê xvid.

%package -n xine-input-dvd
Summary:	XINE input plugin for DVD
Summary(pl):	Wtyczka wej¶ciowa XINE dla DVD
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n xine-input-dvd
XINE input plugin for DVD.

%description -n xine-input-dvd -l pl
Wtyczka wej¶ciowa XINE dla DVD.

%package -n xine-input-gnome-vfs
Summary:	GNOME VFS input driver for xine
Summary(pl):	Sterownik wej¶cia GNOME VFS dla xine
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	xine-lib-input-gnome-vfs

%description -n xine-input-gnome-vfs
GNOME VFS input driver for xine.

%description -n xine-input-gnome-vfs -l pl
Sterownik wej¶cia GNOME VFS dla xine.

%package -n xine-input-v4l
Summary:	Video4Linux input driver for xine
Summary(pl):	Sterownik wej¶cia Video4Linux dla xine
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n xine-input-v4l
Video4Linux input driver for xine.

%description -n xine-input-v4l -l pl
Sterownik wej¶cia Video4Linux dla xine.

%package -n xine-input-vcd
Summary:	VCD input driver for xine
Summary(pl):	Sterownik wej¶cia VCD dla xine
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n xine-input-vcd
VCD input driver for xine (for reading VideoCD).

%description -n xine-input-vcd -l pl
Sterownik wej¶cia VCD dla xine (do czytania VideoCD).

%package -n xine-output-audio-alsa
Summary:	XINE - alsa support
Summary(pl):	XINE - obs³uga alsa
Summary(pt_BR):	XINE - suporte a alsa
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	xine-plugin-audio = %{epoch}:%{version}-%{release}
Obsoletes:	xine-lib-alsa

%description -n xine-output-audio-alsa
XINE audio output plugin with alsa support.

%description -n xine-output-audio-alsa -l pl
Wtyczka wyj¶cia d¼wiêku do XINE z obs³ug± ALSA.

%description -n xine-output-audio-alsa -l pt_BR
Plugin de audio para o xine, com suporte a alsa.

%package -n xine-output-audio-arts
Summary:	XINE - arts support
Summary(pl):	XINE - obs³uga arts
Summary(pt_BR):	XINE - suporte a arts
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	xine-plugin-audio = %{epoch}:%{version}-%{release}
Obsoletes:	xine-lib-arts

%description -n xine-output-audio-arts
XINE audio output plugin with arts support.

%description -n xine-output-audio-arts -l pl
Wtyczka wyj¶cia d¼wiêku do XINE z obs³ug± arts.

%package -n xine-output-audio-esd
Summary:	XINE - esd support
Summary(pl):	XINE - obs³uga esd
Summary(pt_BR):	XINE - suporte a esd
Group:		Libraries
Provides:	xine-plugin-audio = %{epoch}:%{version}-%{release}
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	xine-lib-esd

%description -n xine-output-audio-esd
XINE audio output plugin with esd support.

%description -n xine-output-audio-esd -l pl
Wtyczka wyj¶cia d¼wiêku do XINE z obs³ug± esd.

%description -n xine-output-audio-esd -l pt_BR
Plugin de audio para o xine, com suporte a esd.

%package -n xine-output-audio-oss
Summary:	XINE - OSS/ALSA support
Summary(pl):	XINE - obs³uga OSS/ALSA
Summary(pt_BR):	XINE - suporte a oss
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	xine-plugin-audio = %{epoch}:%{version}-%{release}
Obsoletes:	xine-lib-oss

%description -n xine-output-audio-oss
XINE audio output plugins with OSS/ALSA support.

%description -n xine-output-audio-oss -l pl
Wtyczka wyj¶cia d¼wiêku do XINE z obs³ug± OSS/ALSA.

%description -n xine-output-audio-oss -l pt_BR
Plugin de audio para o xine, com suporte a oss.

%package -n xine-output-video-aa
Summary:	XINE - Ascii Art support
Summary(pl):	XINE - obs³uga Ascii Art
Summary(pt_BR):	XINE - suporte a aalib
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	xine-lib-aa

%description -n xine-output-video-aa
XINE video output plugin using Ascii Art library.

%description -n xine-output-video-aa -l pl
Wtyczka wyj¶cia obrazu do XINE z obs³ug± Ascii Art.

%description -n xine-output-video-aa -l pt_BR
Plugin de video para o xine, utilizando a aalib.

%package -n xine-output-video-directfb
Summary:	XINE - accelereted framebuffer support
Summary(pl):	XINE - obs³uga akcelerowanego framebuffera
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	xine-lib-directfb

%description -n xine-output-video-directfb
XINE video output plugin for accelereted framebuffer support (with
DirectFB library).

%description -n xine-output-video-directfb -l pl
Wtyczka wyj¶cia obrazu do XINE dla akcelerowanego framebuffera (przez
bibliotekê DirectFB).

%package -n xine-output-video-dxr3
Summary:	XINE - DXR3 support
Summary(pl):	XINE - obs³uga DXR3
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	xine-lib-dxr3

%description -n xine-output-video-dxr3
XINE video/decoder plugins for DXR3 card support.

%description -n xine-output-video-dxr3 -l pl
Wtyczka wyj¶cia i dekodera obrazu do XINE z obs³ug± kart DXR3.

%package -n xine-output-video-caca
Summary:	XINE - Color AsCii Art support
Summary(pl):	XINE - obs³uga Color AsCii Art
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n xine-output-video-caca
Color AsCii Art output plugin for xine.

%description -n xine-output-video-caca -l pl
Wtyczka wyj¶cia obrazu do XINE dla kolorowego wyj¶cia AsCii Art.

%package -n xine-output-video-fb
Summary:	XINE - framebuffer support
Summary(pl):	XINE - obs³uga framebuffera
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	xine-lib-fb

%description -n xine-output-video-fb
XINE video output plugin using Linux framebuffer.

%description -n xine-output-video-fb -l pl
Wtyczka wyj¶cia obrazu do XINE dla linuksowego framebuffera.

%package -n xine-output-video-opengl
Summary:	XINE - OpenGL video output
Summary(pl):	XINE - wy¶wietlanie przez OpenGL
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	OpenGL
Obsoletes:	xine-lib-opengl

%description -n xine-output-video-opengl
XINE video output plugin using OpenGL.

%description -n xine-output-video-opengl -l pl
Wtyczka wyj¶cia obrazu do XINE wykorzystuj±ca OpenGL do wy¶wietlania.

%package -n xine-output-video-sdl
Summary:	XINE - SDL output support
Summary(pl):	XINE - obs³uga wyj¶cia SDL
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	xine-lib-sdl

%description -n xine-output-video-sdl
XINE video output plugin using SDL library.

%description -n xine-output-video-sdl -l pl
Wtyczka wyj¶cia obrazu do XINE wy¶wietlaj±ca poprzez bibliotekê SDL.

%package -n xine-output-video-stk
Summary:	XINE - STK video output support
Summary(pl):	XINE - obs³uga wyj¶cia obrazu STK
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	libstk(xine) >= 0.2.0
Obsoletes:	xine-lib-sdl

%description -n xine-output-video-stk
XINE video output plugin using libstk library.

%description -n xine-output-video-sdl -l pl
Wtyczka wyj¶cia obrazu do XINE wy¶wietlaj±ca poprzez bibliotekê
libstk.

%package -n xine-output-video-syncfb
Summary:	XINE - SyncFB (Matrox G200/G400) support
Summary(pl):	XINE - obs³uga SyncFB (Matrox G200/G400)
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	xine-lib-syncfb

%description -n xine-output-video-syncfb
XINE video output plugin using SyncFB interface (for Matrox G200/G400
cards).

%description -n xine-output-video-syncfb -l pl
Wtyczka wyj¶cia obrazu do XINE obs³uguj±ca interfejs SyncFB (dla kart
Matrox G200/G400).

%package -n xine-output-video-vidix
Summary:	XINE - VIDIX video output plugin
Summary(pl):	XINE - wtyczka wyj¶cia obrazu VIDIX
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n xine-output-video-vidix
XINE video output plugin using VIDIX.

%description -n xine-output-video-vidix -l pl
Wtyczka wyj¶cia obrazu do XINE u¿ywaj±ca VIDIX.

%package -n xine-output-video-vidix-cyberblade
Summary:	VIDIX driver for Cyberblade/i1 chips
Summary(pl):	Sterownik VIDIX dla uk³adów Cyberblade/i1
Group:		Libraries
Requires:	xine-output-video-vidix = %{epoch}:%{version}-%{release}
Obsoletes:	xine-lib-vidix-cyberblade

%description -n xine-output-video-vidix-cyberblade
VIDIX driver for Cyberblade/i1 chips.

%description -n xine-output-video-vidix-cyberblade -l pl
Sterownik VIDIX dla uk³adów Cyberblade/i1.

%package -n xine-output-video-vidix-mach64
Summary:	VIDIX driver for Mach64 and 3Drage chips
Summary(pl):	Sterownik VIDIX dla uk³adów Mach64 oraz 3DRage
Group:		Libraries
Requires:	xine-output-video-vidix = %{epoch}:%{version}-%{release}
Obsoletes:	xine-lib-vidix-mach64

%description -n xine-output-video-vidix-mach64
VIDIX driver for Mach64 and 3Drage chips.

%description -n xine-output-video-vidix-mach64 -l pl
Sterownik VIDIX dla uk³adów Mach64 oraz 3DRage.

%package -n xine-output-video-vidix-matrox
Summary:	VIDIX drivers for Matrox Mga chips
Summary(pl):	Sterowniki VIDIX dla uk³adów Matrox Mga
Group:		Libraries
Requires:	xine-output-video-vidix = %{epoch}:%{version}-%{release}
Obsoletes:	xine-lib-vidix-matrox

%description -n xine-output-video-vidix-matrox
VIDIX drivers for Matrox Mga chips.

%description -n xine-output-video-vidix-matrox -l pl
Sterowniki VIDIX dla uk³adów Matrox Mga.

%package -n xine-output-video-vidix-nvidia
Summary:	VIDIX driver for Riva and Riva-derived chips
Summary(pl):	Sterownik VIDIX dla uk³adów Riva oraz pochodnych
Group:		Libraries
Requires:	xine-output-video-vidix = %{epoch}:%{version}-%{release}
Obsoletes:	xine-lib-vidix-nvidia

%description -n xine-output-video-vidix-nvidia
VIDIX driver for Riva and Riva-derived chips, e.g. Riva TNT, GeForce
2.

%description -n xine-output-video-vidix-nvidia -l pl
Sterownik VIDIX dla uk³adów Riva oraz pochodnych.

%package -n xine-output-video-vidix-permedia
Summary:	VIDIX drivers for 3Dlabs GLINT R3 and Permedia chips
Summary(pl):	Sterowniki VIDIX dla uk³adów 3Dlabs GLINT R3 oraz Permedia
Group:		Libraries
Requires:	xine-output-video-vidix = %{epoch}:%{version}-%{release}
Obsoletes:	xine-lib-vidix-permedia

%description -n xine-output-video-vidix-permedia
VIDIX drivers for 3Dlabs GLINT R3 and Permedia chips.

%description -n xine-output-video-vidix-permedia -l pl
Sterowniki VIDIX dla uk³adów 3Dlabs GLINT R3 oraz Permedia.

%package -n xine-output-video-vidix-radeon
Summary:	VIDIX driver for Radeon chips
Summary(pl):	Sterownik VIDIX dla uk³adów Radeon
Group:		Libraries
Requires:	xine-output-video-vidix = %{epoch}:%{version}-%{release}
Obsoletes:	xine-lib-vidix-radeon

%description -n xine-output-video-vidix-radeon
VIDIX driver for Radeon chips.

%description -n xine-output-video-vidix-radeon -l pl
Sterownik VIDIX dla uk³adów Radeon.

%package -n xine-output-video-vidix-rage128
Summary:	VIDIX driver for Rage128 chips
Summary(pl):	Sterownik VIDIX dla uk³adów Rage128
Group:		Libraries
Requires:	xine-output-video-vidix = %{epoch}:%{version}-%{release}
Obsoletes:	xine-lib-vidix-rage128

%description -n xine-output-video-vidix-rage128
VIDIX driver for Rage128 chips.

%description -n xine-output-video-vidix-rage128 -l pl
Sterownik VIDIX dla uk³adów Rage128.

%package -n xine-output-video-vidix-sis
Summary:	VIDIX driver for SiS chips
Summary(pl):	Sterownik VIDIX dla uk³adów SiS
Group:		Libraries
Requires:	xine-output-video-vidix = %{epoch}:%{version}-%{release}

%description -n xine-output-video-vidix-sis
VIDIX driver for SiS 300 and 310/325 series chips.

%description -n xine-output-video-vidix-sis -l pl
Sterownik VIDIX dla uk³adów SiS serii 300 i 310/325.

%package -n xine-output-video-xshm
Summary:	XINE - XFree XShm support
Summary(pl):	XINE - obs³uga XFree XShm
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	xine-lib-xshm

%description -n xine-output-video-xshm
XINE video output plugin using XFree MIT shared memory.

%description -n xine-output-video-xshm -l pl
Wtyczka wyj¶cia obrazu do XINE z obs³ug± XFree MIT shared memory.

%package -n xine-output-video-xv
Summary:	XINE - XFree XVideo support
Summary(pl):	XINE - obs³uga XFree XVideo
Summary(pt_BR):	XINE - suporte a XFree XVideo
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	xine-lib-xv

%description -n xine-output-video-xv
XINE video output plugin using XFree XVideo extension.

%description -n xine-output-video-xv -l pl
Wtyczka wyj¶cia obrazu do XINE u¿ywaj±ca rozszerzenia XVideo.

%description -n xine-output-video-xv -l pt_BR
Plugin de video para o xine, utilizando a extensão XVideo do XFree.

%prep
%setup -q -n %{name}-%{_version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%ifarch sparc
%patch4 -p1
%endif
%patch5 -p1

%build
%{__libtoolize}
%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
CPPFLAGS=-I/usr/include/xvid
%configure \
	--with-external-dvdnav \
	--with-w32-path=%{_libdir}/codecs \
	--with-xv-path=/usr/X11R6/%{_lib} \
	%{?with_aalib:--with-aalib-prefix=/usr} \
	%{?with_alsa:--enable-alsa} \
	%{!?with_alsa:--disable-alsa} \
	%{?with_dxr3:--enable-dxr3} \
	%{!?with_dxr3:--disable-dxr3} \
	%{?with_directfb:--enable-directfb}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_aclocaldir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

# remove useless *.la files
rm -f $RPM_BUILD_ROOT%{_libdir}/xine/plugins/1.0.0/{,vidix,post}/*.la

%find_lang xine-lib

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f xine-lib.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog TODO
%attr(755,root,root) %{_libdir}/libxine*.so.*.*
%dir %{_datadir}/xine
%dir %{_datadir}/xine/libxine1
%{_datadir}/xine/libxine1/fonts
%dir %{_libdir}/xine
%dir %{_libdir}/xine/plugins
%dir %{_pluginsdir}
%dir %{_pluginsdir}/post
%attr(755,root,root) %{_pluginsdir}/post/*.so
%{_docdir}/xine

# input plugins
%attr(755,root,root) %{_pluginsdir}/xineplug_inp_cdda.so
%attr(755,root,root) %{_pluginsdir}/xineplug_inp_dvb.so
%attr(755,root,root) %{_pluginsdir}/xineplug_inp_file.so
%attr(755,root,root) %{_pluginsdir}/xineplug_inp_http.so
%attr(755,root,root) %{_pluginsdir}/xineplug_inp_mms.so
%attr(755,root,root) %{_pluginsdir}/xineplug_inp_net.so
%attr(755,root,root) %{_pluginsdir}/xineplug_inp_pnm.so
%attr(755,root,root) %{_pluginsdir}/xineplug_inp_pvr.so
%attr(755,root,root) %{_pluginsdir}/xineplug_inp_rtp.so
%attr(755,root,root) %{_pluginsdir}/xineplug_inp_rtsp.so
%attr(755,root,root) %{_pluginsdir}/xineplug_inp_stdin_fifo.so
%attr(755,root,root) %{_pluginsdir}/xineplug_inp_vcdo.so

# demuxer plugins
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_asf.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_audio.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_avi.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_fli.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_flv.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_games.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_iff.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_image.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_matroska.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_mng.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_mpeg*.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_nsv.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_pva.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_qt.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_rawdv.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_real.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_slave.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_sputext.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_yuv4mpeg2.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_yuv_frames.so

# decoder plugins
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_a52.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_bitplane.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_dts.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_dvaudio.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_faad.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_ff.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_gsm610.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_image.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_lpcm.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_mad.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_mpeg2.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_nsf.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_real.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_real_audio.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_rgb.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_spu.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_spucc.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_spucmml.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_sputext.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_yuv.so

# Others
%attr(755,root,root) %{_pluginsdir}/xineplug_ao_out_file.so
%attr(755,root,root) %{_pluginsdir}/xineplug_ao_out_none.so
%attr(755,root,root) %{_pluginsdir}/xineplug_vo_out_none.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xine-config
%attr(755,root,root) %{_libdir}/libxine*.so
%{_libdir}/libxine*.la
%{_includedir}/*
%{_aclocaldir}/*.m4
%{_pkgconfigdir}/libxine.pc
%{_mandir}/man[13]/*

%files -n xine-decode-flac
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/xineplug_flac.so

%files -n xine-decode-ogg
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_speex.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_theora.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_vorbis.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_ogg.so

%ifarch %{ix86}
%files -n xine-decode-w32dll
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_qt.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_w32dll.so
%endif

%if %{with xvid}
%files -n xine-decode-xvid
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_xvid.so
%endif

%files -n xine-input-dvd
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/xineplug_inp_dvd.so

%if %{with gnome}
%files -n xine-input-gnome-vfs
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/xineplug_inp_gnome_vfs.so
%endif

%files -n xine-input-v4l
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/xineplug_inp_v4l.so

%files -n xine-input-vcd
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/xineplug_inp_vcd.so

%if %{with alsa}
%files -n xine-output-audio-alsa
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/xineplug_ao_out_alsa.so
%endif

%if %{with arts}
%files -n xine-output-audio-arts
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/xineplug_ao_out_arts.so
%endif

%if %{with esd}
%files -n xine-output-audio-esd
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/xineplug_ao_out_esd.so
%endif

%files -n xine-output-audio-oss
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/xineplug_ao_out_oss.so

%if %{with aalib}
%files -n xine-output-video-aa
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/xineplug_vo_out_aa.so
%endif

%if %{with directfb}
%files -n xine-output-video-directfb
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/xineplug_vo_out_directfb.so
%endif

%if %{with dxr3}
%files -n xine-output-video-dxr3
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_dxr3_spu.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_dxr3_video.so
%attr(755,root,root) %{_pluginsdir}/xineplug_vo_out_dxr3.so
%endif

%files -n xine-output-video-caca
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/xineplug_vo_out_caca.so

%files -n xine-output-video-fb
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/xineplug_vo_out_fb.so

%if %{with opengl}
%files -n xine-output-video-opengl
%defattr(644,root,root,755)
%attr(644,root,root) %{_pluginsdir}/xineplug_vo_out_opengl.so
%endif

%if %{with sdl}
%files -n xine-output-video-sdl
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/xineplug_vo_out_sdl.so
%endif

%if %{with stk}
%files -n xine-output-video-stk
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/xineplug_vo_out_stk.so
%endif

%files -n xine-output-video-syncfb
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/xineplug_vo_out_syncfb.so

%ifarch %{ix86}
%files -n xine-output-video-vidix
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/xineplug_vo_out_vidix.so
%dir %{_pluginsdir}/vidix

%files -n xine-output-video-vidix-cyberblade
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/vidix/cyberblade*.so

# Please don't package vidix-genfb. genfb is just a sample driver.

%files -n xine-output-video-vidix-mach64
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/vidix/mach64*.so

%files -n xine-output-video-vidix-matrox
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/vidix/mga*.so

#%files vidix-nvidia
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_pluginsdir}/vidix/nvidia*.so

%files -n xine-output-video-vidix-permedia
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/vidix/pm*.so

%files -n xine-output-video-vidix-radeon
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/vidix/radeon*.so

%files -n xine-output-video-vidix-rage128
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/vidix/rage128*.so

%files -n xine-output-video-vidix-sis
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/vidix/sis*.so
%endif

%files -n xine-output-video-xshm
%defattr(644,root,root,755)
%attr(644,root,root) %{_pluginsdir}/xineplug_vo_out_xshm.so

%files -n xine-output-video-xv
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/xineplug_vo_out_xv.so
