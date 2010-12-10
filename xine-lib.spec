# TODO
# - fix build --with-external-dvdnav
#
# Workaround for xine-lib.spec - libstk.spec updating:
# 	1. make-request -r --without stk xine-lib
#	2. make-request -r libstk
#	3. bump release of xine-lib
#	4. make-request -r xine-lib
#
# Conditional build:
%bcond_without	aalib		# don't build aalib video output plugin
%bcond_without	alsa		# don't build ALSA audio output plugin
%bcond_without	caca		# don't build libcaca video output plugin
%bcond_without	directfb	# don't build DirectFB video output plugin
%bcond_without	dxr3		# don't build dxr3 video output and decode plugins
%bcond_without	dvd		# don't build dvdnav stuff
%bcond_with	esd		# don't build EsounD audio output plugin
%bcond_without	fusionsound	# don't build FusionSound audio output plugin
%bcond_without	gdkpixbuf	# don't build gdk-pixbuf decode plugin
%bcond_without	gnome		# don't build gnome_vfs input plugin
%bcond_without	opengl		# don't build OpenGL video output plugin
%bcond_without	pulseaudio	# don't build pulseaudio output plugin
%bcond_without	smb		# don't build SMB input plugin
%bcond_without	sdl		# don't build SDL video output plugin
%bcond_without	stk		# don't build stk video output plugin
%bcond_without	wavpack		# don't build wavpack decode plugin
%bcond_with	xvid		# build xvid decode plugin [disabled in sources at the moment]
%bcond_with	vdr		# build with vdr support
%bcond_without	vis		# build without vis sparc extensions - with vis breaks compatibility
				# with v7 processors and enables vis optimization for sparc64 arch.
				# without vis is currently broken it fails on ffmpeg
#
%ifnarch %{ix86}
%undefine	with_dxr3
%endif

Summary:	A Free Video Player
Summary(ko.UTF-8):	공개 동영상 플레이어
Summary(pl.UTF-8):	Odtwarzacz filmów
Summary(pt_BR.UTF-8):	Xine, um player de video
Name:		xine-lib
Version:	1.1.19
Release:	6
Epoch:		2
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/xine/%{name}-%{version}.tar.bz2
# Source0-md5:	a410a0f0617e1d6309f0cbe907f73f8a
Patch0:		%{name}-nolibs.patch
Patch1:		%{name}-win32-path.patch
Patch2:		%{name}-am.patch
Patch3:		%{name}-sh.patch
Patch4:		%{name}-vdr.patch
Patch5:		%{name}-ac.patch
Patch6:		%{name}-xxmc.patch
URL:		http://xine.sourceforge.net/
%{?with_directfb:BuildRequires:	DirectFB-devel >= 0.9.22}
%{?with_fusionsound:BuildRequires:	FusionSound-devel >= 0.9.23}
BuildRequires:	ImageMagick-devel >= 1:6.0.0
%{?with_opengl:BuildRequires:	OpenGL-GLU-devel}
%{?with_opengl:BuildRequires:	OpenGL-glut-devel}
%{?with_sdl:BuildRequires:	SDL-devel >= 1.2.11}
%{?with_aalib:BuildRequires:	aalib-devel >= 1.4}
%{?with_alsa:BuildRequires:	alsa-lib-devel >= 0.9.0}
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.8.1
%{?with_esd:BuildRequires:	esound-devel >= 0.2.8}
BuildRequires:	faad2-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	flac-devel
BuildRequires:	gettext-devel
%{?with_gnome:BuildRequires:	gnome-vfs2-devel}
%{?with_gdkpixbuf:BuildRequires:	gtk+2-devel >= 1:2.0.0}
BuildRequires:	jack-audio-connection-kit-devel >= 0.100
%{?with_caca:BuildRequires:	libcaca-devel >= 0.99-0.beta14}
BuildRequires:	libcdio-devel >= 0.72
%{?with_dvd:BuildRequires:	libdvdnav-devel >= 0.1.9}
%{?with_dxr3:BuildRequires:	libfame-devel >= 0.8.10}
BuildRequires:	libmng-devel
BuildRequires:	libmodplug-devel >= 0.7
BuildRequires:	libmpcdec-devel
BuildRequires:	libpng-devel
%{?with_smb:BuildRequires:	libsmbclient-devel}
%{?with_stk:BuildRequires:	libstk-devel >= 0.2.0}
BuildRequires:	libtheora-devel
BuildRequires:	libtool >= 0:1.4.2-9
BuildRequires:	libvorbis-devel
BuildRequires:	libxcb-devel >= 1.0
BuildRequires:	pkgconfig
%{?with_pulseaudio:BuildRequires:	pulseaudio-devel >= 0.9}
#%{?with_dxr3:BuildRequires:	rte-devel} # only 0.4 supported
BuildRequires:	speex-devel >= 1:1.1.6
BuildRequires:	vcdimager-devel >= 0.7.21
%{?with_wavpack:BuildRequires:	wavpack-devel >= 4.40}
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXvMC-devel
%{?with_xvid:BuildRequires:	xvid-devel}
BuildRequires:	zlib-devel
# libtool problem (up to 1.4e)
BuildConflicts:	xine-lib-devel < 1.0
Obsoletes:	xine
Obsoletes:	xine-libs
Obsoletes:	xine-output-audio-arts
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1

# based on libtool numbers
%define		_pluginsdir	%{_libdir}/xine/plugins/1.29

%define		specflags	-fomit-frame-pointer

%description
xine is a free GPL-licensed video player for Unix-like systems. We
support mpeg-2 and mpeg-1 system (audio + video multiplexed) streams,
eventually mpeg-4 and other formats might be added.

xine plays the video and audio data of mpeg-2 videos and synchronizes
the playback of both. Depending on the properties of the mpeg stream,
playback will need more or less processor power, 100% frame rate has
been seen on a 400 MHz P II system.

%description -l fr.UTF-8
xine est un lecteur vidéo libre sous license GPL pour les systèmes de
type Unix. Nous supportons les flux mpeg-2 et mpeg-1 (audio + vidéo
multiplexés), éventuellement le mpeg-4 et d'autres formats peuvent
êtres ajoutés.

xine joue les données vidéo et audio de vidéo mpeg-2 et synchronise la
lecture des deux. En fonction des propriétes du flux mpeg, la lecture
aura besoin de plus ou moins de puissance du processeur, 100% de
restitution de trame a été vus sur un système PII 400MHz.

%description -l ko.UTF-8
xine 는 GPL라이선스를 따르는 UNIX용 공개 동영상 플레이어입니다. 이
플레이어는 mpeg-2 와 mpeg 1 스트림을 지원하며, 현재는 지원하지 않지만
나중에는 mpeg-4 와 다른 형식의 동영상도 지원할 예정입니다.

%description -l pl.UTF-8
xine jest wolnodostępnym odtwarzaczem filmów dla systemów uniksowych.
Obsługuje strumienie MPEG-2 i MPEG-1 (dźwięk oraz obraz), może być
dodana obsługa MPEG-4 i innych formatów.

xine odczytuje obraz i dźwięk z filmów MPEG-2 i synchronizuje ich
odtwarzanie. Zależnie od właściwości strumienia MPEG, odtwarzanie może
wymagać więcej lub mniej mocy procesora, 100% klatek może być widoczne
na P II 400MHz.

%description -l pt_BR.UTF-8
O xine é um video player GPL para sistemas unix. Lê arquivos MPEG-2 e
MPEG-1, além de AVIs MS MPEG4 / OpenDivX.

O xine lê o conteúdo vídeo e áudio e sincroniza-os em tempo-real. As
necessidades de processador dependem das propriedades de cada arquivo.

%package devel
Summary:	XINE - development files
Summary(pl.UTF-8):	Pliki dla programistów XINE
Summary(pt_BR.UTF-8):	XINE - arquivos de desenvolvimento
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	xine-devel

%description devel
HTML documentation of XINE API and development components.

%description devel -l pl.UTF-8
Pliki dla programistów oraz dokumentacja HTML do API XINE.

%description devel -l pt_BR.UTF-8
Arquivos include a bibliotecas estáticas necessárias para compilar
plugins para o xine e o xine-ui.

%package -n xine-decode-flac
Summary:	XINE - FLAC decoder plugin
Summary(pl.UTF-8):	XINE - wtyczka dekodera FLAC
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n xine-decode-flac
XINE - FLAC decoder/demuxer plugin.

%description -n xine-decode-flac -l pl.UTF-8
XINE - wtyczka dekodera i demuxera FLAC.

%package -n xine-decode-gdkpixbuf
Summary:	XINE - gdk-pixbuf decoder plugin
Summary(pl.UTF-8):	XINE - wtyczka dekodera gdk-pixbuf
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n xine-decode-gdkpixbuf
XINE - gdk-pixbuf decoder plugin.

%description -n xine-decode-gdkpixbuf -l pl.UTF-8
XINE - wtyczka dekodera gdk-pixbuf.

%package -n xine-decode-mpc
Summary:	XINE - MPC/MusePack decoder plugin
Summary(pl.UTF-8):	XINE - wtyczka dekodera MPC/MusePack
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	xine-decode-vorbis

%description -n xine-decode-mpc
XINE - MPC/MusePack decoder plugin.

%description -n xine-decode-mpc -l pl.UTF-8
XINE - wtyczka dekodera MPC/MusePack.

%package -n xine-decode-ogg
Summary:	XINE - Ogg/Vorbis, Ogg/Speex, Ogg/Theora decoder plugins
Summary(pl.UTF-8):	XINE - wtyczki dekoderów Ogg/Vorbis, Ogg/Speex, Ogg/Theora
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	xine-decode-vorbis

%description -n xine-decode-ogg
XINE Ogg/Vorbis, Ogg/Speex, Ogg/Theora decoding plugins: Ogg demuxer,
Vorbis, Speex and Theora decoders.

%description -n xine-decode-ogg -l pl.UTF-8
Wtyczki XINE dekodujące Ogg/Vorbis, Ogg/Speex, Ogg/Theora: demuxer Ogg
oraz dekodery Vorbis, Speex, Theora.

%package -n xine-decode-w32dll
Summary:	XINE - win32dll decoder support
Summary(pl.UTF-8):	XINE - obsługa dekodera win32dll
Summary(pt_BR.UTF-8):	XINE - suporte a decoder win32dll
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Suggests:	w32codec
Obsoletes:	xine-lib-w32dll

%description -n xine-decode-w32dll
XINE win32dll decoder support.

%description -n xine-decode-w32dll -l pl.UTF-8
Obsługa dekodera win32dll do XINE.

%description -n xine-decode-w32dll -l pt_BR.UTF-8
Suporte a win32dll para o xine.

%package -n xine-decode-wavpack
Summary:	XINE - wavpack decoder plugin
Summary(pl.UTF-8):	XINE - wtyczka dekodera wavpack
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n xine-decode-wavpack
XINE - wavpack decoder/demuxer plugin.

%description -n xine-decode-wavpack -l pl.UTF-8
XINE - wtyczka dekodera/demuxera wavpack.

%package -n xine-decode-xvid
Summary:	XINE - xvid DIVX decoding support
Summary(pl.UTF-8):	XINE - obsługa dekodera DIVX xvid
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	xine-lib-xvid

%description -n xine-decode-xvid
XINE decoder plugin for DIVX decoding with xvid library.

%description -n xine-decode-xvid -l pl.UTF-8
Wtyczka dla XINE do dekodowania DIVX poprzez bibliotekę xvid.

%package -n xine-input-dvd
Summary:	XINE input plugin for DVD
Summary(pl.UTF-8):	Wtyczka wejściowa XINE dla DVD
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n xine-input-dvd
XINE input plugin for DVD.

%description -n xine-input-dvd -l pl.UTF-8
Wtyczka wejściowa XINE dla DVD.

%package -n xine-input-gnome-vfs
Summary:	GNOME VFS input driver for xine
Summary(pl.UTF-8):	Sterownik wejścia GNOME VFS dla xine
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	xine-lib-input-gnome-vfs

%description -n xine-input-gnome-vfs
GNOME VFS input driver for xine.

%description -n xine-input-gnome-vfs -l pl.UTF-8
Sterownik wejścia GNOME VFS dla xine.

%package -n xine-input-smb
Summary:	SMB input driver for xine
Summary(pl.UTF-8):	Sterownik wejścia SMB dla xine
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n xine-input-smb
SMB input driver for xine.

%description -n xine-input-smb -l pl.UTF-8
Sterownik wejścia SMB dla xine.

%package -n xine-input-v4l
Summary:	Video4Linux input driver for xine
Summary(pl.UTF-8):	Sterownik wejścia Video4Linux dla xine
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n xine-input-v4l
Video4Linux input driver for xine.

%description -n xine-input-v4l -l pl.UTF-8
Sterownik wejścia Video4Linux dla xine.

%package -n xine-input-vcd
Summary:	VCD input driver for xine
Summary(pl.UTF-8):	Sterownik wejścia VCD dla xine
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n xine-input-vcd
VCD input driver for xine (for reading VideoCD).

%description -n xine-input-vcd -l pl.UTF-8
Sterownik wejścia VCD dla xine (do czytania VideoCD).

%package -n xine-output-audio-alsa
Summary:	XINE - alsa support
Summary(pl.UTF-8):	XINE - obsługa alsa
Summary(pt_BR.UTF-8):	XINE - suporte a alsa
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	xine-plugin-audio = %{epoch}:%{version}-%{release}
Obsoletes:	xine-lib-alsa

%description -n xine-output-audio-alsa
XINE audio output plugin with alsa support.

%description -n xine-output-audio-alsa -l pl.UTF-8
Wtyczka wyjścia dźwięku do XINE z obsługą ALSA.

%description -n xine-output-audio-alsa -l pt_BR.UTF-8
Plugin de audio para o xine, com suporte a alsa.

%package -n xine-output-audio-esd
Summary:	XINE - esd support
Summary(pl.UTF-8):	XINE - obsługa esd
Summary(pt_BR.UTF-8):	XINE - suporte a esd
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	xine-plugin-audio = %{epoch}:%{version}-%{release}
Obsoletes:	xine-lib-esd

%description -n xine-output-audio-esd
XINE audio output plugin with esd support.

%description -n xine-output-audio-esd -l pl.UTF-8
Wtyczka wyjścia dźwięku do XINE z obsługą esd.

%description -n xine-output-audio-esd -l pt_BR.UTF-8
Plugin de audio para o xine, com suporte a esd.

%package -n xine-output-audio-fusionsound
Summary:	XINE - FusionSound support
Summary(pl.UTF-8):	XINE - obsługa FusionSound
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	xine-plugin-audio = %{epoch}:%{version}-%{release}

%description -n xine-output-audio-fusionsound
XINE audio output plugin with FusionSound support.

%description -n xine-output-audio-fusionsound -l pl.UTF-8
Wtyczka wyjścia dźwięku do XINE z obsługą FusionSound.

%package -n xine-output-audio-jack
Summary:	XINE - JACK support
Summary(pl.UTF-8):	XINE - obsługa demona JACK
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	xine-plugin-audio = %{epoch}:%{version}-%{release}

%description -n xine-output-audio-jack
XINE audio output plugin with JACK support.

%description -n xine-output-audio-jack -l pl.UTF-8
Wtyczka wyjścia dźwięku do XINE z obsługa demona JACK.

%package -n xine-output-audio-oss
Summary:	XINE - OSS support
Summary(pl.UTF-8):	XINE - obsługa OSS
Summary(pt_BR.UTF-8):	XINE - suporte a oss
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	xine-plugin-audio = %{epoch}:%{version}-%{release}
Obsoletes:	xine-lib-oss

%description -n xine-output-audio-oss
XINE audio output plugin with OSS support.

%description -n xine-output-audio-oss -l pl.UTF-8
Wtyczka wyjścia dźwięku do XINE z obsługą OSS.

%description -n xine-output-audio-oss -l pt_BR.UTF-8
Plugin de audio para o xine, com suporte a oss.

%package -n xine-output-audio-pulseaudio
Summary:	XINE - pulseaudio support
Summary(pl.UTF-8):	XINE - obsługa pulseaudio
Summary(pt_BR.UTF-8):	XINE - suporte a pulseaudio
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	xine-plugin-audio = %{epoch}:%{version}-%{release}
Obsoletes:	xine-output-audio-polypaudio

%description -n xine-output-audio-pulseaudio
XINE audio output plugins with pulseaudio support.

%description -n xine-output-audio-pulseaudio -l pl.UTF-8
Wtyczka wyjścia dźwięku do XINE z obsługą pulseaudio.

%description -n xine-output-audio-pulseaudio -l pt_BR.UTF-8
Plugin de audio para o xine, com suporte a pulseaudio.

%package -n xine-output-video-aa
Summary:	XINE - Ascii Art support
Summary(pl.UTF-8):	XINE - obsługa Ascii Art
Summary(pt_BR.UTF-8):	XINE - suporte a aalib
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	xine-plugin-video = %{epoch}:%{version}-%{release}
Obsoletes:	xine-lib-aa

%description -n xine-output-video-aa
XINE video output plugin using Ascii Art library.

%description -n xine-output-video-aa -l pl.UTF-8
Wtyczka wyjścia obrazu do XINE z obsługą Ascii Art.

%description -n xine-output-video-aa -l pt_BR.UTF-8
Plugin de video para o xine, utilizando a aalib.

%package -n xine-output-video-directfb
Summary:	XINE - accelereted framebuffer support
Summary(pl.UTF-8):	XINE - obsługa akcelerowanego framebuffera
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	xine-plugin-video = %{epoch}:%{version}-%{release}
Obsoletes:	xine-lib-directfb

%description -n xine-output-video-directfb
XINE video output plugin for accelereted framebuffer support (with
DirectFB library).

%description -n xine-output-video-directfb -l pl.UTF-8
Wtyczka wyjścia obrazu do XINE dla akcelerowanego framebuffera (przez
bibliotekę DirectFB).

%package -n xine-output-video-dxr3
Summary:	XINE - DXR3 support
Summary(pl.UTF-8):	XINE - obsługa DXR3
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	xine-plugin-video = %{epoch}:%{version}-%{release}
Obsoletes:	xine-lib-dxr3

%description -n xine-output-video-dxr3
XINE video/decoder plugins for DXR3 card support.

%description -n xine-output-video-dxr3 -l pl.UTF-8
Wtyczka wyjścia i dekodera obrazu do XINE z obsługą kart DXR3.

%package -n xine-output-video-caca
Summary:	XINE - Color AsCii Art support
Summary(pl.UTF-8):	XINE - obsługa Color AsCii Art
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	xine-plugin-video = %{epoch}:%{version}-%{release}

%description -n xine-output-video-caca
Color AsCii Art output plugin for xine.

%description -n xine-output-video-caca -l pl.UTF-8
Wtyczka wyjścia obrazu do XINE dla kolorowego wyjścia AsCii Art.

%package -n xine-output-video-fb
Summary:	XINE - framebuffer support
Summary(pl.UTF-8):	XINE - obsługa framebuffera
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	xine-plugin-video = %{epoch}:%{version}-%{release}
Obsoletes:	xine-lib-fb

%description -n xine-output-video-fb
XINE video output plugin using Linux framebuffer.

%description -n xine-output-video-fb -l pl.UTF-8
Wtyczka wyjścia obrazu do XINE dla linuksowego framebuffera.

%package -n xine-output-video-opengl
Summary:	XINE - OpenGL video output
Summary(pl.UTF-8):	XINE - wyświetlanie przez OpenGL
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	xine-plugin-video = %{epoch}:%{version}-%{release}
Obsoletes:	xine-lib-opengl

%description -n xine-output-video-opengl
XINE video output plugin using OpenGL.

%description -n xine-output-video-opengl -l pl.UTF-8
Wtyczka wyjścia obrazu do XINE wykorzystująca OpenGL do wyświetlania.

%package -n xine-output-video-sdl
Summary:	XINE - SDL output support
Summary(pl.UTF-8):	XINE - obsługa wyjścia SDL
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	xine-plugin-video = %{epoch}:%{version}-%{release}
Obsoletes:	xine-lib-sdl

%description -n xine-output-video-sdl
XINE video output plugin using SDL library.

%description -n xine-output-video-sdl -l pl.UTF-8
Wtyczka wyjścia obrazu do XINE wyświetlająca poprzez bibliotekę SDL.

%package -n xine-output-video-stk
Summary:	XINE - STK video output support
Summary(pl.UTF-8):	XINE - obsługa wyjścia obrazu STK
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	libstk(xine) >= 0.2.0
Provides:	xine-plugin-video = %{epoch}:%{version}-%{release}
Obsoletes:	xine-lib-sdl

%description -n xine-output-video-stk
XINE video output plugin using libstk library.

%description -n xine-output-video-sdl -l pl.UTF-8
Wtyczka wyjścia obrazu do XINE wyświetlająca poprzez bibliotekę
libstk.

%package -n xine-output-video-syncfb
Summary:	XINE - SyncFB (Matrox G200/G400) support
Summary(pl.UTF-8):	XINE - obsługa SyncFB (Matrox G200/G400)
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	xine-plugin-video = %{epoch}:%{version}-%{release}
Obsoletes:	xine-lib-syncfb

%description -n xine-output-video-syncfb
XINE video output plugin using SyncFB interface (for Matrox G200/G400
cards).

%description -n xine-output-video-syncfb -l pl.UTF-8
Wtyczka wyjścia obrazu do XINE obsługująca interfejs SyncFB (dla kart
Matrox G200/G400).

%package -n xine-output-video-vidix
Summary:	XINE - VIDIX video output plugin
Summary(pl.UTF-8):	XINE - wtyczka wyjścia obrazu VIDIX
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	xine-plugin-video = %{epoch}:%{version}-%{release}

%description -n xine-output-video-vidix
XINE video output plugin using VIDIX.

%description -n xine-output-video-vidix -l pl.UTF-8
Wtyczka wyjścia obrazu do XINE używająca VIDIX.

%package -n xine-output-video-vidix-cyberblade
Summary:	VIDIX driver for Cyberblade/i1 chips
Summary(pl.UTF-8):	Sterownik VIDIX dla układów Cyberblade/i1
Group:		Libraries
Requires:	xine-output-video-vidix = %{epoch}:%{version}-%{release}
Provides:	xine-plugin-video = %{epoch}:%{version}-%{release}
Obsoletes:	xine-lib-vidix-cyberblade

%description -n xine-output-video-vidix-cyberblade
VIDIX driver for Cyberblade/i1 chips.

%description -n xine-output-video-vidix-cyberblade -l pl.UTF-8
Sterownik VIDIX dla układów Cyberblade/i1.

%package -n xine-output-video-vidix-mach64
Summary:	VIDIX driver for Mach64 and 3Drage chips
Summary(pl.UTF-8):	Sterownik VIDIX dla układów Mach64 oraz 3DRage
Group:		Libraries
Requires:	xine-output-video-vidix = %{epoch}:%{version}-%{release}
Provides:	xine-plugin-video = %{epoch}:%{version}-%{release}
Obsoletes:	xine-lib-vidix-mach64

%description -n xine-output-video-vidix-mach64
VIDIX driver for Mach64 and 3Drage chips.

%description -n xine-output-video-vidix-mach64 -l pl.UTF-8
Sterownik VIDIX dla układów Mach64 oraz 3DRage.

%package -n xine-output-video-vidix-matrox
Summary:	VIDIX drivers for Matrox Mga chips
Summary(pl.UTF-8):	Sterowniki VIDIX dla układów Matrox Mga
Group:		Libraries
Requires:	xine-output-video-vidix = %{epoch}:%{version}-%{release}
Provides:	xine-plugin-video = %{epoch}:%{version}-%{release}
Obsoletes:	xine-lib-vidix-matrox

%description -n xine-output-video-vidix-matrox
VIDIX drivers for Matrox Mga chips.

%description -n xine-output-video-vidix-matrox -l pl.UTF-8
Sterowniki VIDIX dla układów Matrox Mga.

%package -n xine-output-video-vidix-nvidia
Summary:	VIDIX driver for Riva and Riva-derived chips
Summary(pl.UTF-8):	Sterownik VIDIX dla układów Riva oraz pochodnych
Group:		Libraries
Requires:	xine-output-video-vidix = %{epoch}:%{version}-%{release}
Provides:	xine-plugin-video = %{epoch}:%{version}-%{release}
Obsoletes:	xine-lib-vidix-nvidia

%description -n xine-output-video-vidix-nvidia
VIDIX driver for Riva and Riva-derived chips, e.g. Riva TNT, GeForce
2.

%description -n xine-output-video-vidix-nvidia -l pl.UTF-8
Sterownik VIDIX dla układów Riva oraz pochodnych.

%package -n xine-output-video-vidix-permedia
Summary:	VIDIX drivers for 3Dlabs GLINT R3 and Permedia chips
Summary(pl.UTF-8):	Sterowniki VIDIX dla układów 3Dlabs GLINT R3 oraz Permedia
Group:		Libraries
Requires:	xine-output-video-vidix = %{epoch}:%{version}-%{release}
Provides:	xine-plugin-video = %{epoch}:%{version}-%{release}
Obsoletes:	xine-lib-vidix-permedia

%description -n xine-output-video-vidix-permedia
VIDIX drivers for 3Dlabs GLINT R3 and Permedia chips.

%description -n xine-output-video-vidix-permedia -l pl.UTF-8
Sterowniki VIDIX dla układów 3Dlabs GLINT R3 oraz Permedia.

%package -n xine-output-video-vidix-radeon
Summary:	VIDIX driver for Radeon chips
Summary(pl.UTF-8):	Sterownik VIDIX dla układów Radeon
Group:		Libraries
Requires:	xine-output-video-vidix = %{epoch}:%{version}-%{release}
Provides:	xine-plugin-video = %{epoch}:%{version}-%{release}
Obsoletes:	xine-lib-vidix-radeon

%description -n xine-output-video-vidix-radeon
VIDIX driver for Radeon chips.

%description -n xine-output-video-vidix-radeon -l pl.UTF-8
Sterownik VIDIX dla układów Radeon.

%package -n xine-output-video-vidix-rage128
Summary:	VIDIX driver for Rage128 chips
Summary(pl.UTF-8):	Sterownik VIDIX dla układów Rage128
Group:		Libraries
Requires:	xine-output-video-vidix = %{epoch}:%{version}-%{release}
Provides:	xine-plugin-video = %{epoch}:%{version}-%{release}
Obsoletes:	xine-lib-vidix-rage128

%description -n xine-output-video-vidix-rage128
VIDIX driver for Rage128 chips.

%description -n xine-output-video-vidix-rage128 -l pl.UTF-8
Sterownik VIDIX dla układów Rage128.

%package -n xine-output-video-vidix-savage
Summary:	VIDIX driver for S3 Savage chips
Summary(pl.UTF-8):	Sterownik VIDIX dla układów S3 Savage
Group:		Libraries
Requires:	xine-output-video-vidix = %{epoch}:%{version}-%{release}
Provides:	xine-plugin-video = %{epoch}:%{version}-%{release}

%description -n xine-output-video-vidix-savage
VIDIX driver for S3 Savage series chips.

%description -n xine-output-video-vidix-savage -l pl.UTF-8
Sterownik VIDIX dla układów S3 serii Savage.

%package -n xine-output-video-vidix-sis
Summary:	VIDIX driver for SiS chips
Summary(pl.UTF-8):	Sterownik VIDIX dla układów SiS
Group:		Libraries
Requires:	xine-output-video-vidix = %{epoch}:%{version}-%{release}
Provides:	xine-plugin-video = %{epoch}:%{version}-%{release}

%description -n xine-output-video-vidix-sis
VIDIX driver for SiS 300 and 310/325 series chips.

%description -n xine-output-video-vidix-sis -l pl.UTF-8
Sterownik VIDIX dla układów SiS serii 300 i 310/325.

%package -n xine-output-video-vidix-unichrome
Summary:	VIDIX driver for VIA CLE266 Unichrome chips
Summary(pl.UTF-8):	Sterownik VIDIX dla układów VIA CLE266 Unichrome
Group:		Libraries
Requires:	xine-output-video-vidix = %{epoch}:%{version}-%{release}
Provides:	xine-plugin-video = %{epoch}:%{version}-%{release}

%description -n xine-output-video-vidix-unichrome
VIDIX driver for VIA CLE266 Unichrome chips.

%description -n xine-output-video-vidix-unichrome -l pl.UTF-8
Sterownik VIDIX dla układów VIA CLE2666 Unichrome.

%package -n xine-output-video-xcb
Summary:	XINE - XCB support
Summary(pl.UTF-8):	XINE - obsługa XCB
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	xine-plugin-video = %{epoch}:%{version}-%{release}
Obsoletes:	xine-lib-xshm

%description -n xine-output-video-xcb
XINE video output plugin using XShm or Xv via XCB.

%description -n xine-output-video-xcb -l pl.UTF-8
Wtyczka wyjścia obrazu do XINE z obsługą XShm lub Xv poprzez XCB.

%package -n xine-output-video-xdirectfb
Summary:	XINE - accelereted DirectFB X11 support
Summary(pl.UTF-8):	XINE - obsługa DirectFB X11
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	xine-plugin-video = %{epoch}:%{version}-%{release}
Obsoletes:	xine-lib-directfb

%description -n xine-output-video-xdirectfb
XINE video output plugin for DirectFB X11.

%description -n xine-output-video-xdirectfb -l pl.UTF-8
Wtyczka wyjścia obrazu do XINE dla DirectFB X11.

%package -n xine-output-video-xshm
Summary:	XINE - XFree XShm support
Summary(pl.UTF-8):	XINE - obsługa XFree XShm
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	xine-plugin-video = %{epoch}:%{version}-%{release}
Obsoletes:	xine-lib-xshm

%description -n xine-output-video-xshm
XINE video output plugin using XFree MIT shared memory.

%description -n xine-output-video-xshm -l pl.UTF-8
Wtyczka wyjścia obrazu do XINE z obsługą XFree MIT shared memory.

%package -n xine-output-video-xv
Summary:	XINE - XFree XVideo support
Summary(pl.UTF-8):	XINE - obsługa XFree XVideo
Summary(pt_BR.UTF-8):	XINE - suporte a XFree XVideo
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	xine-plugin-video = %{epoch}:%{version}-%{release}
Obsoletes:	xine-lib-xv

%description -n xine-output-video-xv
XINE video output plugin using XFree XVideo extension.

%description -n xine-output-video-xv -l pl.UTF-8
Wtyczka wyjścia obrazu do XINE używająca rozszerzenia XVideo.

%description -n xine-output-video-xv -l pt_BR.UTF-8
Plugin de video para o xine, utilizando a extensão XVideo do XFree.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%{?with_vdr:%patch4 -p1}
%patch5 -p1
%patch6 -p0

# kill hack, it fails with recent automake
echo 'AC_DEFUN([AM_PROG_AS_MOD],[AM_PROG_AS])' > m4/as.m4
# use system libtool.m4
rm -f m4/libtool15.m4

%build
# breaks DOMAIN (modified Makefile.in.in?)
#%%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	%{!?with_aalib:--disable-aalib} \
	%{!?with_alsa:--without-alsa} \
	%{?with_directfb:--enable-directfb} \
	%{!?with_dxr3:--disable-dxr3} \
	%{!?with_esd:--without-esound} \
	%{!?with_gdkpixbuf:--disable-gdkpixbuf} \
	--enable-ipv6 \
	%{!?with_pulseaudio:--without-pulseaudio} \
	%{!?with_smb:--disable-samba} \
	%{?with_aalib:--with-aalib-prefix=/usr} \
	--with-external-dvdnav \
	--with-external-ffmpeg \
	--with-external-libmpcdec \
	%{?with_fusionsound:--with-fusionsound} \
	--with-libflac \
	%{?with_stk:--with-libstk} \
	--with-real-codecs-path=%{_libdir}/codecs \
	--with-w32-path=/usr/lib/codecs \
	%{?with_wavpack:--with-wavpack} \
%if %{with vis}
%ifarch sparc sparcv9 sparc64
	CFLAGS="%{rpmcflags} -mvis" \
%endif
%else
	--disable-vis \
%endif
	--disable-optimizations # we use own RPM_OPT_FLAGS optimalizations
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_aclocaldir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

# remove useless *.la files
rm -f $RPM_BUILD_ROOT%{_pluginsdir}/{,vidix,post}/*.la

%find_lang libxine1

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f libxine1.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog TODO
%attr(755,root,root) %{_bindir}/xine-list-1.1
%attr(755,root,root) %{_libdir}/libxine.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libxine.so.1
%dir %{_datadir}/xine
%dir %{_datadir}/xine/libxine1
%{_datadir}/xine/libxine1/fonts
%dir %{_libdir}/xine
%dir %{_libdir}/xine/plugins
%dir %{_pluginsdir}
%{_pluginsdir}/mime.types
%dir %{_pluginsdir}/post
%attr(755,root,root) %{_pluginsdir}/post/*.so
%{_docdir}/xine-lib
%{_mandir}/man1/xine-list-1.1.1*
%{_mandir}/man5/xine.5*

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
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_rgb.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_spu.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_spucc.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_spucmml.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_spuhdmv.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_spudvb.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_sputext.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_yuv.so

# Others
%attr(755,root,root) %{_pluginsdir}/xineplug_ao_out_file.so
%attr(755,root,root) %{_pluginsdir}/xineplug_ao_out_none.so
%attr(755,root,root) %{_pluginsdir}/xineplug_vo_out_none.so
%attr(755,root,root) %{_pluginsdir}/xineplug_vo_out_raw.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xine-config
%attr(755,root,root) %{_libdir}/libxine.so
%{_libdir}/libxine.la
%{_includedir}/xine.h
%{_includedir}/xine
%{_aclocaldir}/xine.m4
%{_pkgconfigdir}/libxine.pc
%{_mandir}/man1/xine-config.1*

%files -n xine-decode-flac
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/xineplug_flac.so

%if %{with gdkpixbuf}
%files -n xine-decode-gdkpixbuf
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_gdk_pixbuf.so
%endif

%files -n xine-decode-mpc
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_mpc.so

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

%if %{with wavpack}
%files -n xine-decode-wavpack
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/xineplug_wavpack.so
%endif

%if %{with xvid}
%files -n xine-decode-xvid
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_xvid.so
%endif

%if %{with dvd}
%files -n xine-input-dvd
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/xineplug_inp_dvd.so
%endif

%if %{with gnome}
%files -n xine-input-gnome-vfs
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/xineplug_inp_gnome_vfs.so
%endif

%if %{with smb}
%files -n xine-input-smb
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/xineplug_inp_smb.so
%endif

%files -n xine-input-v4l
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/xineplug_inp_v4l.so
%attr(755,root,root) %{_pluginsdir}/xineplug_inp_v4l2.so

%files -n xine-input-vcd
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/xineplug_inp_vcd.so

%if %{with alsa}
%files -n xine-output-audio-alsa
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/xineplug_ao_out_alsa.so
%endif

%if %{with esd}
%files -n xine-output-audio-esd
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/xineplug_ao_out_esd.so
%endif

%if %{with fusionsound}
%files -n xine-output-audio-fusionsound
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/xineplug_ao_out_fusionsound.so
%endif

%files -n xine-output-audio-jack
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/xineplug_ao_out_jack.so

%files -n xine-output-audio-oss
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/xineplug_ao_out_oss.so

%if %{with pulseaudio}
%files -n xine-output-audio-pulseaudio
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/xineplug_ao_out_pulseaudio.so
%endif

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

%if %{with caca}
%files -n xine-output-video-caca
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/xineplug_vo_out_caca.so
%endif

%files -n xine-output-video-fb
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/xineplug_vo_out_fb.so

%if %{with opengl}
%files -n xine-output-video-opengl
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/xineplug_vo_out_opengl.so
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

%files -n xine-output-video-vidix-nvidia
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/vidix/nvidia*.so

%files -n xine-output-video-vidix-permedia
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/vidix/pm*.so

%files -n xine-output-video-vidix-radeon
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/vidix/radeon*.so

%files -n xine-output-video-vidix-rage128
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/vidix/rage128*.so

%files -n xine-output-video-vidix-savage
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/vidix/savage*.so

%files -n xine-output-video-vidix-sis
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/vidix/sis*.so

%files -n xine-output-video-vidix-unichrome
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/vidix/unichrome*.so
%endif

%files -n xine-output-video-xcb
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/xineplug_vo_out_xcbshm.so
%attr(755,root,root) %{_pluginsdir}/xineplug_vo_out_xcbxv.so

%if %{with directfb}
%files -n xine-output-video-xdirectfb
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/xineplug_vo_out_xdirectfb.so
%endif

%files -n xine-output-video-xshm
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/xineplug_vo_out_xshm.so

%files -n xine-output-video-xv
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/xineplug_vo_out_xv.so
%attr(755,root,root) %{_pluginsdir}/xineplug_vo_out_xvmc.so
%attr(755,root,root) %{_pluginsdir}/xineplug_vo_out_xxmc.so
