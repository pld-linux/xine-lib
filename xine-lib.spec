# Conditional build:
# --without	aa
# --with	alsa	(alsa support is currently broken)
# --without	arts
# --without	esd
# --without	oss
# --with	dxr3
# --without	opengl

Summary:	A Free Video Player
Summary(ko):	°ø°³ µ¿¿µ»ó ÇÃ·¹ÀÌ¾î
Summary(pl):	Odtwarzacz video
Summary(pt_BR):	Xine, um player de video
Name:		xine-lib
Version:	0.9.9
Release:	0.2
License:	GPL
Group:		Libraries
Source0:	http://xine.sourceforge.net/files/%{name}-%{version}.tar.gz
Patch0:		%{name}-configure_vfill.patch
Patch1:		%{name}-am_fixes.patch
Patch2:		%{name}-ac_fixes.patch
URL:		http://xine.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake >= 1.5
%{!?_without_aa:BuildRequires:		aalib-devel}
%{!?_without_aa:BuildRequires:		aalib-progs}
%ifnarch alpha
%{!?_without_arts:BuildRequires:	arts-devel}
%endif
%ifnarch sparc sparc64
%{!?_without_alsa:BuildRequires:	alsa-lib-devel}
%endif
%{!?_without_esd:BuildRequires:		esound-devel}
%{!?_without_opengl:BuildRequires:	OpenGL-devel}
%ifarch %{ix86}
BuildRequires:  divx4linux-devel
BuildRequires:	xvid-devel
%else
BuildRequires:	libdivxdecore-devel
%endif
BuildRequires:	gettext-devel
BuildRequires:	libvorbis-devel
BuildRequires:	libtool >= 1.4.2
BuildRequires:	zlib-devel
BuildRequires:	SDL-devel
BuildRequires:	pkgconfig
BuildRequires:	imlib-devel
BuildRequires:	glut-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	xine

%define 	_noautoreqdep	%{!?_without_opengl:libGL.so.1 libGLU.so.1}

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_pluginsdir	%{_libdir}/xine/plugins

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
xine jest wolnodostêpnym odtwarzaczem video dla systemów uniksowych.
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

%package oss
Summary:	XINE - OSS/ALSA support
Summary(pl):	XINE - obs³uga OSS/ALSA
Summary(pt_BR):	XINE - suporte a oss
Group:		Libraries
Requires:	%{name} = %{version}

%description oss
XINE audio plugins with OSS/ALSA support.

%description oss -l pl
Wtyczka audio do XINE z obs³ug± OSS/ALSA.

%description oss -l pt_BR
Plugin de audio para o xine, com suporte a oss.

%package alsa
Summary:	XINE - alsa support
Summary(pl):	XINE - obs³uga alsa
Summary(pt_BR):	XINE - suporte a alsa
Group:		Libraries
Requires:	%{name} = %{version}

%description alsa
XINE audio plugin with alsa support.

%description alsa -l pl
Wtyczka audio do XINE z obs³ug± ALSA.

%description alsa -l pt_BR
Plugin de audio para o xine, com suporte a alsa.

%package arts
Summary:	XINE - arts support
Summary(pl):	XINE - obs³uga arts
Summary(pt_BR):	XINE - suporte a arts
Group:		Libraries
Requires:	%{name} = %{version}

%description arts
XINE audio plugin with arts support.

%description arts -l pl
Wtyczka audio do XINE z obs³ug± arts.

%package esd
Summary:	XINE - esd support
Summary(pl):	XINE - obs³uga esd
Summary(pt_BR):	XINE - suporte a esd
Group:		Libraries
Requires:	%{name} = %{version}

%description esd
XINE audio plugin with esd support.

%description esd -l pl
Wtyczka audio do XINE z obs³ug± esd.

%description esd -l pt_BR
Plugin de audio para o xine, com suporte a esd.

%package dxr3
Summary:	XINE - DXR3 support
Summary(pl):	XINE - obs³uga DXR3
Group:		Libraries
Requires:	%{name} = %{version}

%description dxr3
XINE video/decoder plugins for DXR3 card support.

%description dxr3 -l pl
Wtyczka odtwarzacza obrazu do XINE z obs³ug± kart DXR3.

%package xv
Summary:	XINE - XFree XVideo support
Summary(pl):	XINE - obs³uga XFree XVideo
Summary(pt_BR):	XINE - suporte a XFree XVideo
Group:		Libraries
Requires:	%{name} = %{version}

%description xv
XINE video plugin using XFree XVideo extension.

%description xv -l pl
Wtyczka video do XINE u¿ywaj±ca rozszerzenia XVideo.

%description xv -l pt_BR
Plugin de video para o xine, utilizando a extensão XVideo do XFree.

%package aa
Summary:	XINE - Ascii Art support
Summary(pl):	XINE - obs³uga Ascii Art
Summary(pt_BR):	XINE - suporte a aalib
Group:		Libraries
Requires:	%{name} = %{version}

%description aa
XINE video plugin using Ascii Art library.

%description aa -l pl
Wtyczka video do XINE z obs³ug± Ascii Art.

%description aa -l pt_BR
Plugin de video para o xine, utilizando a aalib.

%package xshm
Summary:	XINE - XFree XShm support
Summary(pl):	XINE - obs³uga XFree XShm
Group:		Libraries
Requires:	%{name} >= %{version}

%description xshm
XINE video plugin using XFree MIT shared memory.

%description xshm -l pl
Wtyczka video do XINE z obs³ug± XFree MIT shared memory.

%package syncfb
Summary:	XINE - SyncFB (Matrox G200/G400) support
Summary(pl):	XINE - obs³uga SyncFB (Matrox G200/G400)
Group:		Libraries
Requires:	%{name} = %{version}

%description syncfb
SyncFB (for Matrox G200/G400 cards) interface for xine.

%description syncfb -l pl
Wtyczka video do XINE obs³uguj±ca interfejs SyncFB (dla kart Matrox G200/G400).

%package fb
Summary:	XINE - framebuffer support
Summary(pl):	XINE - obs³uga framebuffera
Group:		Libraries
Requires:	%{name} = %{version}

%description fb
SyncFB (for Matrox G200/G400 cards) interface for xine.

%description fb -l pl
Wtyczka video do XINE dla framebuffera.

%package opengl
Summary:	XINE - OpenGL video output
Summary(pl):	XINE - wy¶wietlanie OpenGL
Group:		Libraries
Requires:	%{name} = %{version}

%description opengl
XINE plugin using OpenGL for video output.

%description opengl -l pl
Wtyczka video do XINE wykorzystuj±ca OpenGL do wy¶wietlania.

%package w32dll
Summary:	XINE - win32dll decoder support
Summary(pl):	XINE - obs³uga dekodera win32dll
Summary(pt_BR):	XINE - suporte a decoder win32dll
Group:		Libraries
Requires:	%{name} = %{version}
Requires:	w32codec

%description w32dll
XINE win32dll decoder support.

%description w32dll -l pl
Obs³uga dekodera win32dll do XINE.

%description w32dll -l pt_BR
Suporte a win32dll para o xine.

%package devel
Summary:	XINE - development files
Summary(pl):	Pliki dla programistów XINE
Summary(pt_BR):	XINE - arquivos de desenvolvimento
Group:		Development/Libraries
Requires:	%{name} = %{version}
Obsoletes:	xine-devel

%description devel
HTML documentation of XINE API and development components.

%description devel -l pl
Pliki dla programistów oraz dokumentacja HTML do API XINE.

%description devel -l pt_BR
Arquivos include a bibliotecas estáticas necessárias para compilar
plugins para o xine e o xine-ui.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
rm -f missing
libtoolize --copy --force
gettextize --copy --force
aclocal
%{__autoconf}
%{__automake}
autoheader

# flag for libmad
%ifarch %{ix86}
CPPFLAGS="-DFPM_INTEL"
%endif
%ifarch sparc
CPPFLAGS="-DFPM_SPARC"
%endif
%ifarch ppc
CPPFLAGS="-DFPM_PPC"
%endif
%ifarch ia64 alpha
CPPFLAGS="-DFPM_64BIT"
%endif
%ifnarch %{ix86} sparc ppc ia64 alpha
CPPFLAGS="-DFPM_DEFAULT"
%endif
export CPPFLAGS

%configure \
	--with-aalib-prefix=/usr \
%{?_with_alsa:	--enable-alsa} \
%{!?_with_alsa:	--disable-alsa}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS ChangeLog TODO

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxine*.so.*.*
%dir %{_datadir}/xine
%dir %{_datadir}/xine/skins
%{_datadir}/xine/skins/*.png
%dir %{_libdir}/xine
%dir %{_pluginsdir}
%doc *.gz

# input plugins
%attr(755,root,root) %{_pluginsdir}/xineplug_inp_cda.so
%attr(755,root,root) %{_pluginsdir}/xineplug_inp_dvd.so
%attr(755,root,root) %{_pluginsdir}/xineplug_inp_file.so
%attr(755,root,root) %{_pluginsdir}/xineplug_inp_http.so
%attr(755,root,root) %{_pluginsdir}/xineplug_inp_mms.so
%attr(755,root,root) %{_pluginsdir}/xineplug_inp_net.so
%attr(755,root,root) %{_pluginsdir}/xineplug_inp_rtp.so
%attr(755,root,root) %{_pluginsdir}/xineplug_inp_stdin_fifo.so
%attr(755,root,root) %{_pluginsdir}/xineplug_inp_vcd.so
# demuxer plugins
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_asf.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_avi.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_cda.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_mpeg*.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_ogg.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_qt.so
# decoder plugins
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_a52.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_divx4.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_dts.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_ff.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_lpcm.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_mad.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_mpeg2.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_spu.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_spucc.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_sputext.so
#%attr(755,root,root) %{_pluginsdir}/xineplug_decode_vfill.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_vorbis.so

%if %{!?_without_oss:1}%{?_without_oss:0}
%files oss
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/*oss.so
%endif

%if %{?_with_alsa:1}%{!?_with_alsa:0}
%ifnarch sparc sparc64
%files alsa
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/*alsa*.so
%endif
%endif

%ifnarch alpha
%if %{!?_without_arts:1}%{?_without_arts:0}
%files arts
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/*arts.so
%endif
%endif

%if %{!?_without_esd:1}%{?_without_esd:0}
%files esd
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/*esd.so
%endif

%if %{?_with_dxr3:1}%{!?_with_dxr3:0}
%files dxr3
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_dxr3.so
%attr(755,root,root) %{_pluginsdir}/xineplug_vo_out_dxr3.so
%endif

%files xv
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/*xv.so

%if %{!?_without_aa:1}%{?_without_aa:0}
%files aa
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/*aa.so
%endif

%files xshm
%defattr(644,root,root,755)
%attr(644,root,root) %{_pluginsdir}/*xshm.so

%files syncfb
%defattr(644,root,root,755)
%attr(644,root,root) %{_pluginsdir}/*syncfb.so

%files fb
%defattr(644,root,root,755)
%attr(644,root,root) %{_pluginsdir}/*_fb.so

%if %{!?_without_opengl:1}%{?_without_opengl:0}
%files opengl
%defattr(644,root,root,755)
%attr(644,root,root) %{_pluginsdir}/*opengl.so
%endif

%ifarch %{ix86}
%files w32dll
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/*w32dll.so
%endif

%files devel
%defattr(644,root,root,755)
%doc doc/xine-lib-API/html/*.{html,png,gif,css}
%attr(755,root,root) %{_bindir}/xine-config
%{_includedir}/*
%attr(755,root,root) %{_libdir}/libxine*.la
%attr(755,root,root) %{_libdir}/libxine*.so
%attr(755,root,root) %{_pluginsdir}/*.la
%{_mandir}/man[13]/*
