#
# Conditional build:
# _with_dxr3		- build dxr3 video output and decode plugins
# _without_aalib	- don't build aalib video output plugin
# _without_alsa		- don't build ALSA audio output plugin
# _without_arts		- don't build aRts audio output plugin
# _without_directfb	- don't build DirectFB video output plugin
# _without_esd		- don't build EsounD audio output plugin
# _without_gnome	- don't build gnome_vfs plugin
# _without_opengl	- don't build OpenGL video output plugin [useless at the moment]
# _without_sdl		- don't build SDL video output plugin
# _without_xvid		- don't build xvid decode plugin [useless at the moment]
#
%ifarch alpha
%define		_without_arts	1
%define		_without_xvid	1
%endif
%ifarch sparc sparc64
%define		_without_alsa	1
%define		_without_xvid	1
%endif

%define		_rc		rc1
%define		_version	1-%{_rc}

Summary:	A Free Video Player
Summary(ko):	공개 동영상 플레이어
Summary(pl):	Odtwarzacz video
Summary(pt_BR):	Xine, um player de video
Name:		xine-lib
Version:	1.0
Release:	0.%{_rc}.1
Epoch:		1
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/xine/%{name}-%{_version}.tar.gz
# Source0-md5:	6e4c65fa2a3677f9f761772703dd9477
Patch0:		%{name}-am17.patch
Patch1:		%{name}-automake_as.patch
URL:		http://xine.sourceforge.net/
%{!?_without_directfb:BuildRequires:	DirectFB-devel >= 0.9.9}
%{!?_without_opengl:BuildRequires:	OpenGL-devel}
%{!?_without_sdl:BuildRequires:		SDL-devel}
%{!?_without_aalib:BuildRequires:	aalib-devel >= 1.3}
%{!?_without_alsa:BuildRequires:	alsa-lib-devel >= 0.9.0}
%{!?_without_arts:BuildRequires:	arts-devel >= 0.9.5}
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1.5
%{!?_without_esd:BuildRequires:		esound-devel >= 0.2.8}
BuildRequires:	flac-devel
BuildRequires:	gettext-devel
BuildRequires:	glut-devel
%{!?_without_gnome:BuildRequires:	gnome-vfs2-devel}
BuildRequires:	libdvdnav-devel >= 0.1.9
BuildRequires:	libmng-devel
BuildRequires:	libpng-devel
BuildRequires:	libvorbis-devel
BuildRequires:	libtool >= 0:1.4.2-9
BuildRequires:	pkgconfig
BuildRequires:	speex-devel
%ifarch %{ix86}
%{!?_without_xvid:BuildRequires:	xvid-devel}
%else
BuildRequires:	libdivxdecore-devel
%endif
BuildRequires:	zlib-devel
# libtool problem (up to 1.4e)
BuildConflicts:	xine-lib-devel < 1.0
Obsoletes:	xine
Obsoletes:	xine-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	%{!?_without_opengl:libGL.so.1 libGLU.so.1}

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
xine est un lecteur vid�o libre sous license GPL pour les syst�mes de
type unix. Nous supportons les flux mpeg-2 et mpeg-1 (audio + vid�o
multiplex�s), �ventuellement le mpeg-4 et d'autres formats peuvent
�tres ajout�s.

xine joue les donn�es vid�o et audio de vid�o mpeg-2 et synchronise la
lecture des deux. En fonction des propri�tes du flux mpeg, la lecture
aura besoin de plus ou moins de puissance du processeur, 100% de
restitution de trame a �t� vus sur un syst�me PII 400MHz.

%description -l ko
xine 는 GPL라이선스를 따르는 UNIX용 공개 동영상 플레이어입니다. 이
플레이어는 mpeg-2 와 mpeg 1 스트림을 지원하며, 현재는 지원하지 않지만
나중에는 mpeg-4 와 다른 형식의 동영상도 지원할 예정입니다.

%description -l pl
xine jest wolnodost�pnym odtwarzaczem video dla system�w uniksowych.
Obs퀅guje strumienie MPEG-2 i MPEG-1 (d펧i�k oraz obraz), mo풽 by�
dodana obs퀅ga MPEG-4 i innych format�w.

xine odczytuje obraz i d펧i�k z film�w MPEG-2 i synchronizuje ich
odtwarzanie. Zale퓆ie od w쿪턢iwo턢i strumienia MPEG, odtwarzanie mo풽
wymaga� wi�cej lub mniej mocy procesora, 100% klatek mo풽 by� widoczne
na P II 400MHz.

%description -l pt_BR
O xine � um video player GPL para sistemas unix. L� arquivos MPEG-2 e
MPEG-1, al�m de AVIs MS MPEG4 / OpenDivX.

O xine l� o conte�do v�deo e �udio e sincroniza-os em tempo-real. As
necessidades de processador dependem das propriedades de cada arquivo.

%package devel
Summary:	XINE - development files
Summary(pl):	Pliki dla programist�w XINE
Summary(pt_BR):	XINE - arquivos de desenvolvimento
Group:		Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	xine-devel

%description devel
HTML documentation of XINE API and development components.

%description devel -l pl
Pliki dla programist�w oraz dokumentacja HTML do API XINE.

%description devel -l pt_BR
Arquivos include a bibliotecas est�ticas necess�rias para compilar
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
Summary:	XINE - Ogg/Vorbis and Ogg/Speex decoder plugins
Summary(pl):	XINE - wtyczki dekoder�w Ogg/Vorbis i Ogg/Speex
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	xine-decode-vorbis
# Ogg/Theora info to be added when plugin is ready

%description -n xine-decode-ogg
XINE Ogg/Vorbis and Ogg/Speex decoding plugins: Ogg demuxer, Vorbis
and Speex decoders.

%description -n xine-decode-ogg -l pl
Wtyczki XINE dekoduj켧e Ogg/Vorbis i Ogg/Speex: demuxer Ogg oraz
dekodery Vorbis i Speex.

%package -n xine-decode-w32dll
Summary:	XINE - win32dll decoder support
Summary(pl):	XINE - obs퀅ga dekodera win32dll
Summary(pt_BR):	XINE - suporte a decoder win32dll
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	w32codec
Obsoletes:	xine-lib-w32dll

%description -n xine-decode-w32dll
XINE win32dll decoder support.

%description -n xine-decode-w32dll -l pl
Obs퀅ga dekodera win32dll do XINE.

%description -n xine-decode-w32dll -l pt_BR
Suporte a win32dll para o xine.

%package -n xine-decode-xvid
Summary:	XINE - xvid DIVX decoding support
Summary(pl):	XINE - obs퀅ga dekodera DIVX xvid
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	xine-lib-xvid

%description -n xine-decode-xvid
XINE decoder plugin for DIVX decoding with xvid library.

%description -n xine-decode-xvid -l pl
Wtyczka dla XINE do dekodowania DIVX poprzez bibliotek� xvid.

%package -n xine-input-dvd
Summary:	XINE input plugin for DVD
Summary(pl):	Wtyczka wej턢iowa XINE dla DVD
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n xine-input-dvd
XINE input plugin for DVD.

%description -n xine-input-dvd -l pl
Wtyczka wej턢iowa XINE dla DVD.

%package -n xine-input-gnome-vfs
Summary:	GNOME VFS input driver for xine
Summary(pl):	Sterownik wej턢ia GNOME VFS dla xine
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	xine-lib-input-gnome-vfs

%description -n xine-input-gnome-vfs
GNOME VFS input driver for xine.

%description -n xine-input-gnome-vfs -l pl
Sterownik wej턢ia GNOME VFS dla xine.

%package -n xine-input-v4l
Summary:	Video4Linux input driver for xine
Summary(pl):	Sterownik wej턢ia Video4Linux dla xine
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n xine-input-v4l
Video4Linux input driver for xine.

%description -n xine-input-v4l -l pl
Sterownik wej턢ia Video4Linux dla xine.

%package -n xine-output-audio-alsa
Summary:	XINE - alsa support
Summary(pl):	XINE - obs퀅ga alsa
Summary(pt_BR):	XINE - suporte a alsa
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	xine-plugin-audio
Obsoletes:	xine-lib-alsa

%description -n xine-output-audio-alsa
XINE audio output plugin with alsa support.

%description -n xine-output-audio-alsa -l pl
Wtyczka wyj턢ia d펧i�ku do XINE z obs퀅g� ALSA.

%description -n xine-output-audio-alsa -l pt_BR
Plugin de audio para o xine, com suporte a alsa.

%package -n xine-output-audio-arts
Summary:	XINE - arts support
Summary(pl):	XINE - obs퀅ga arts
Summary(pt_BR):	XINE - suporte a arts
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	xine-plugin-audio
Obsoletes:	xine-lib-arts

%description -n xine-output-audio-arts
XINE audio output plugin with arts support.

%description -n xine-output-audio-arts -l pl
Wtyczka wyj턢ia d펧i�ku do XINE z obs퀅g� arts.

%package -n xine-output-audio-esd
Summary:	XINE - esd support
Summary(pl):	XINE - obs퀅ga esd
Summary(pt_BR):	XINE - suporte a esd
Group:		Libraries
Provides:	xine-plugin-audio
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	xine-lib-esd

%description -n xine-output-audio-esd
XINE audio output plugin with esd support.

%description -n xine-output-audio-esd -l pl
Wtyczka wyj턢ia d펧i�ku do XINE z obs퀅g� esd.

%description -n xine-output-audio-esd -l pt_BR
Plugin de audio para o xine, com suporte a esd.

%package -n xine-output-audio-oss
Summary:	XINE - OSS/ALSA support
Summary(pl):	XINE - obs퀅ga OSS/ALSA
Summary(pt_BR):	XINE - suporte a oss
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	xine-plugin-audio
Obsoletes:	xine-lib-oss

%description -n xine-output-audio-oss
XINE audio output plugins with OSS/ALSA support.

%description -n xine-output-audio-oss -l pl
Wtyczka wyj턢ia d펧i�ku do XINE z obs퀅g� OSS/ALSA.

%description -n xine-output-audio-oss -l pt_BR
Plugin de audio para o xine, com suporte a oss.

%package -n xine-output-video-aa
Summary:	XINE - Ascii Art support
Summary(pl):	XINE - obs퀅ga Ascii Art
Summary(pt_BR):	XINE - suporte a aalib
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	xine-lib-aa

%description -n xine-output-video-aa
XINE video output plugin using Ascii Art library.

%description -n xine-output-video-aa -l pl
Wtyczka wyj턢ia obrazu do XINE z obs퀅g� Ascii Art.

%description -n xine-output-video-aa -l pt_BR
Plugin de video para o xine, utilizando a aalib.

%package -n xine-output-video-directfb
Summary:	XINE - accelereted framebuffer support
Summary(pl):	XINE - obs퀅ga akcelerowanego framebuffera
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	xine-lib-directfb

%description -n xine-output-video-directfb
XINE video output plugin for accelereted framebuffer support (with
DirectFB library).

%description -n xine-output-video-directfb -l pl
Wtyczka wyj턢ia obrazu do XINE dla akcelerowanego framebuffera (przez
bibliotek� DirectFB).

%package -n xine-output-video-dxr3
Summary:	XINE - DXR3 support
Summary(pl):	XINE - obs퀅ga DXR3
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	xine-lib-dxr3

%description -n xine-output-video-dxr3
XINE video/decoder plugins for DXR3 card support.

%description -n xine-output-video-dxr3 -l pl
Wtyczka wyj턢ia i dekodera obrazu do XINE z obs퀅g� kart DXR3.

%package -n xine-output-video-fb
Summary:	XINE - framebuffer support
Summary(pl):	XINE - obs퀅ga framebuffera
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	xine-lib-fb

%description -n xine-output-video-fb
XINE video output plugin using Linux framebuffer.

%description -n xine-output-video-fb -l pl
Wtyczka wyj턢ia obrazu do XINE dla linuksowego framebuffera.

%package -n xine-output-video-opengl
Summary:	XINE - OpenGL video output
Summary(pl):	XINE - wy턻ietlanie przez OpenGL
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	OpenGL
Obsoletes:	xine-lib-opengl

%description -n xine-output-video-opengl
XINE video output plugin using OpenGL.

%description -n xine-output-video-opengl -l pl
Wtyczka wyj턢ia obrazu do XINE wykorzystuj켧a OpenGL do wy턻ietlania.

%package -n xine-output-video-sdl
Summary:	XINE - SDL output support
Summary(pl):	XINE - obs퀅ga wyj턢ia SDL
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	xine-lib-sdl

%description -n xine-output-video-sdl
XINE video output plugin using SDL library.

%description -n xine-output-video-sdl -l pl
Wtyczka wyj턢ia obrazu do XINE wy턻ietlaj켧a poprzez bibliotek� SDL.

%package -n xine-output-video-syncfb
Summary:	XINE - SyncFB (Matrox G200/G400) support
Summary(pl):	XINE - obs퀅ga SyncFB (Matrox G200/G400)
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	xine-lib-syncfb

%description -n xine-output-video-syncfb
XINE video output plugin using SyncFB interface (for Matrox G200/G400
cards).

%description -n xine-output-video-syncfb -l pl
Wtyczka wyj턢ia obrazu do XINE obs퀅guj켧a interfejs SyncFB (dla kart
Matrox G200/G400).

%package -n xine-output-video-vidix
Summary:	XINE - VIDIX video output plugin
Summary(pl):	XINE - wtyczka wyj턢ia obrazu VIDIX
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description -n xine-output-video-vidix
XINE video output plugin using VIDIX.

%description -n xine-output-video-vidix -l pl
Wtyczka wyj턢ia obrazu do XINE u퓓waj켧a VIDIX.

%package -n xine-output-video-vidix-cyberblade
Summary:	VIDIX driver for Cyberblade/i1 chips
Summary(pl):	Sterownik VIDIX dla uk쿪d�w Cyberblade/i1
Group:		Libraries
Requires:	xine-output-video-vidix = %{epoch}:%{version}-%{release}
Obsoletes:	xine-lib-vidix-cyberblade

%description -n xine-output-video-vidix-cyberblade
VIDIX driver for Cyberblade/i1 chips.

%description -n xine-output-video-vidix-cyberblade -l pl
Sterownik VIDIX dla uk쿪d�w Cyberblade/i1.

%package -n xine-output-video-vidix-mach64
Summary:	VIDIX driver for Mach64 and 3Drage chips
Summary(pl):	Sterownik VIDIX dla uk쿪d�w Mach64 oraz 3DRage
Group:		Libraries
Requires:	xine-output-video-vidix = %{epoch}:%{version}-%{release}
Obsoletes:	xine-lib-vidix-mach64

%description -n xine-output-video-vidix-mach64
VIDIX driver for Mach64 and 3Drage chips.

%description -n xine-output-video-vidix-mach64 -l pl
Sterownik VIDIX dla uk쿪d�w Mach64 oraz 3DRage.

%package -n xine-output-video-vidix-matrox
Summary:	VIDIX drivers for Matrox Mga chips
Summary(pl):	Sterowniki VIDIX dla uk쿪d�w Matrox Mga
Group:		Libraries
Requires:	xine-output-video-vidix = %{epoch}:%{version}-%{release}
Obsoletes:	xine-lib-vidix-matrox

%description -n xine-output-video-vidix-matrox
VIDIX drivers for Matrox Mga chips.

%description -n xine-output-video-vidix-matrox -l pl
Sterowniki VIDIX dla uk쿪d�w Matrox Mga.

%package -n xine-output-video-vidix-nvidia
Summary:	VIDIX driver for Riva and Riva-derived chips
Summary(pl):	Sterownik VIDIX dla uk쿪d�w Riva oraz pochodnych
Group:		Libraries
Requires:	xine-output-video-vidix = %{epoch}:%{version}-%{release}
Obsoletes:	xine-lib-vidix-nvidia

%description -n xine-output-video-vidix-nvidia
VIDIX driver for Riva and Riva-derived chips, e.g. Riva TNT, GeForce
2.

%description -n xine-output-video-vidix-nvidia -l pl
Sterownik VIDIX dla uk쿪d�w Riva oraz pochodnych.

%package -n xine-output-video-vidix-permedia
Summary:	VIDIX drivers for 3Dlabs GLINT R3 and Permedia chips
Summary(pl):	Sterowniki VIDIX dla uk쿪d�w 3Dlabs GLINT R3 oraz Permedia
Group:		Libraries
Requires:	xine-output-video-vidix = %{epoch}:%{version}-%{release}
Obsoletes:	xine-lib-vidix-permedia

%description -n xine-output-video-vidix-permedia
VIDIX drivers for 3Dlabs GLINT R3 and Permedia chips.

%description -n xine-output-video-vidix-permedia -l pl
Sterowniki VIDIX dla uk쿪d�w 3Dlabs GLINT R3 oraz Permedia.

%package -n xine-output-video-vidix-radeon
Summary:	VIDIX driver for Radeon chips
Summary(pl):	Sterownik VIDIX dla uk쿪d�w Radeon
Group:		Libraries
Requires:	xine-output-video-vidix = %{epoch}:%{version}-%{release}
Obsoletes:	xine-lib-vidix-radeon

%description -n xine-output-video-vidix-radeon
VIDIX driver for Radeon chips.

%description -n xine-output-video-vidix-radeon -l pl
Sterownik VIDIX dla uk쿪d�w Radeon.

%package -n xine-output-video-vidix-rage128
Summary:	VIDIX driver for Rage128 chips
Summary(pl):	Sterownik VIDIX dla uk쿪d�w Rage128
Group:		Libraries
Requires:	xine-output-video-vidix = %{epoch}:%{version}-%{release}
Obsoletes:	xine-lib-vidix-rage128

%description -n xine-output-video-vidix-rage128
VIDIX driver for Rage128 chips.

%description -n xine-output-video-vidix-rage128 -l pl
Sterownik VIDIX dla uk쿪d�w Rage128.

%package -n xine-output-video-xshm
Summary:	XINE - XFree XShm support
Summary(pl):	XINE - obs퀅ga XFree XShm
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	xine-lib-xshm

%description -n xine-output-video-xshm
XINE video output plugin using XFree MIT shared memory.

%description -n xine-output-video-xshm -l pl
Wtyczka wyj턢ia obrazu do XINE z obs퀅g� XFree MIT shared memory.

%package -n xine-output-video-xv
Summary:	XINE - XFree XVideo support
Summary(pl):	XINE - obs퀅ga XFree XVideo
Summary(pt_BR):	XINE - suporte a XFree XVideo
Group:		Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Obsoletes:	xine-lib-xv

%description -n xine-output-video-xv
XINE video output plugin using XFree XVideo extension.

%description -n xine-output-video-xv -l pl
Wtyczka wyj턢ia obrazu do XINE u퓓waj켧a rozszerzenia XVideo.

%description -n xine-output-video-xv -l pt_BR
Plugin de video para o xine, utilizando a extens�o XVideo do XFree.

%prep
%setup -q -n %{name}-%{_version}
%patch0 -p1
%patch1 -p1

%build
%{__libtoolize}
%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	CPPFLAGS=-I/usr/include/xvid \
	--with-external-dvdnav \
	%{!?_without_aalib:--with-aalib-prefix=/usr} \
	%{!?_without_alsa:--enable-alsa} \
	%{?_without_alsa:--disable-alsa} \
	%{?_with_dxr3:--enable-dxr3} \
	%{!?_with_dxr3:--disable-dxr3}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_aclocaldir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

mv $RPM_BUILD_ROOT%{_datadir}/locale/pl_PL $RPM_BUILD_ROOT%{_datadir}/locale/pl

#Remove useless *.la files
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
#%attr(755,root,root) %{_pluginsdir}/xineplug_inp_cda.so
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
%attr(755,root,root) %{_pluginsdir}/xineplug_inp_vcd.so

# demuxer plugins
#%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_aiff.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_asf.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_audio.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_avi.so
#%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_cda.so
#%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_eawve.so
#%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_film.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_fli.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_games.so
#%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_idcin.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_image.so
#%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_ipmovie.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_mng.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_mpeg*.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_pva.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_qt.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_rawdv.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_real.so
#%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_realaudio.so
#%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_roq.so
#%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_smjpeg.so
#%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_snd.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_sputext.so
#%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_voc.so
#%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_vqa.so
#%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_wav.so
#%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_wc3movie.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_yuv4mpeg2.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_yuv_frames.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_nsv.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_slave.so

# decoder plugins
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_28k8.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_a52.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_adpcm.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_cinepak.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_cyuv.so
#%attr(755,root,root) %{_pluginsdir}/xineplug_decode_divx4.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_dts.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_faad.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_ff.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_fli.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_gsm610.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_idcinvideo.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_image.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_interplayaudio.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_interplayvideo.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_logpcm.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_lpcm.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_mad.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_mpeg2.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_msrle.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_msvc.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_nsf.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_qtrle.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_qtrpza.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_qtsmc.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_real.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_real_audio.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_rgb.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_roqaudio.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_roqvideo.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_spu.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_spucc.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_spuogm.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_sputext.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_svq1.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_wc3video.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_yuv.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_yuv_frames.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_pcm.so

# Others
%attr(755,root,root) %{_pluginsdir}/xineplug_vo_out_none.so
%attr(755,root,root) %{_pluginsdir}/xineplug_ao_out_none.so

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
#%attr(755,root,root) %{_pluginsdir}/xineplug_decode_theora.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_vorbis.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_ogg.so

%ifarch %{ix86}
%files -n xine-decode-w32dll
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_qt.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_w32dll.so
%endif

#%if 0%{!?_without_xvid:1}
#%files -n xine-decode-xvid
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_pluginsdir}/xineplug_decode_xvid.so
#%endif

%files -n xine-input-dvd
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/xineplug_inp_dvd.so

%if 0%{!?_without_gnome:1}
%files -n xine-input-gnome-vfs
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/xineplug_inp_gnome_vfs.so
%endif

%files -n xine-input-v4l
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/xineplug_inp_v4l.so

%if 0%{!?_without_alsa:1}
%files -n xine-output-audio-alsa
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/xineplug_ao_out_alsa.so
%endif

%if 0%{!?_without_arts:1}
%files -n xine-output-audio-arts
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/xineplug_ao_out_arts.so
%endif

%if 0%{!?_without_esd:1}
%files -n xine-output-audio-esd
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/xineplug_ao_out_esd.so
%endif

%files -n xine-output-audio-oss
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/xineplug_ao_out_oss.so

%if 0%{!?_without_aalib:1}
%files -n xine-output-video-aa
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/xineplug_vo_out_aa.so
%endif

%if 0%{!?_without_directfb:1}
%files -n xine-output-video-directfb
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/xineplug_vo_out_directfb.so
%endif

%if 0%{?_with_dxr3:1}
%files -n xine-output-video-dxr3
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_dxr3.so
%attr(755,root,root) %{_pluginsdir}/xineplug_vo_out_dxr3.so
%endif

%files -n xine-output-video-fb
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/xineplug_vo_out_fb.so

#%if 0%{?_without_opengl:0}
#%files opengl
#%defattr(644,root,root,755)
#%attr(644,root,root) %{_pluginsdir}/xineplug_vo_out_opengl.so
#%endif

%if 0%{!?_without_sdl:1}
%files -n xine-output-video-sdl
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/xineplug_vo_out_sdl.so
%endif

%files -n xine-output-video-syncfb
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/xineplug_vo_out_syncfb.so

%ifnarch ppc
%files -n xine-output-video-vidix
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/xineplug_vo_out_vidix.so
%dir %{_pluginsdir}/vidix

%files -n xine-output-video-vidix-cyberblade
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/vidix/cyberblade*.so

# Please dont package vidix-genfb. genfb is just a sample driver.

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
%endif

%files -n xine-output-video-xshm
%defattr(644,root,root,755)
%attr(644,root,root) %{_pluginsdir}/xineplug_vo_out_xshm.so

%files -n xine-output-video-xv
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/xineplug_vo_out_xv.so
