# Conditional build:
# --without	aa
# --without	alsa
# --without	arts
# --with	directfb
# --with	dxr3
# --without	esd
# --without	opengl
# --without	sdl
# --without	xvid

%define		_without_alsa	1

%ifarch alpha
%define		_without_arts	1
%define		_without_xvid	1
%endif
%ifarch sparc sparc64
%define		_without_alsa	1
%define		_without_xvid	1
%endif

Summary:	A Free Video Player
Summary(ko):	공개 동영상 플레이어
Summary(pl):	Odtwarzacz video
Summary(pt_BR):	Xine, um player de video
Name:		xine-lib
Version:	0.9.13
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://xine.sourceforge.net/files/%{name}-%{version}.tar.gz
Patch0:		%{name}-am17.patch
Patch1:		%{name}-lt14d.patch
Patch2:		%{name}-automake_as.patch
URL:		http://xine.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake >= 1.5
%{!?_without_aa:BuildRequires:		aalib-devel}
%{!?_without_aa:BuildRequires:		aalib-progs}
%{!?_without_arts:BuildRequires:	arts-devel}
%{!?_without_alsa:BuildRequires:	alsa-lib-devel >= 0.9.0}
%{!?_without_esd:BuildRequires:		esound-devel}
%{!?_without_opengl:BuildRequires:	OpenGL-devel}
%{!?_without_sdl:BuildRequires:		SDL-devel}
%{?_with_directfb:BuildRequires:	DirectFB-devel}
%ifarch %{ix86}
%{!?_without_xvid:BuildRequires:	xvid-devel}
%else
BuildRequires:	libdivxdecore-devel
%endif
BuildRequires:	gettext-devel
BuildRequires:	glut-devel
BuildRequires:	imlib-devel
BuildRequires:	libvorbis-devel
BuildRequires:	libtool >= 0:1.4.2-9
BuildRequires:	pkgconfig
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	xine
Obsoletes:	xine-libs

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

%package oss
Summary:	XINE - OSS/ALSA support
Summary(pl):	XINE - obs퀅ga OSS/ALSA
Summary(pt_BR):	XINE - suporte a oss
Group:		Libraries
Provides:	xine-plugin-audio
Requires:	%{name} = %{version}

%description oss
XINE audio plugins with OSS/ALSA support.

%description oss -l pl
Wtyczka audio do XINE z obs퀅g� OSS/ALSA.

%description oss -l pt_BR
Plugin de audio para o xine, com suporte a oss.

%package alsa
Summary:	XINE - alsa support
Summary(pl):	XINE - obs퀅ga alsa
Summary(pt_BR):	XINE - suporte a alsa
Group:		Libraries
Provides:	xine-plugin-audio
Requires:	%{name} = %{version}

%description alsa
XINE audio plugin with alsa support.

%description alsa -l pl
Wtyczka audio do XINE z obs퀅g� ALSA.

%description alsa -l pt_BR
Plugin de audio para o xine, com suporte a alsa.

%package arts
Summary:	XINE - arts support
Summary(pl):	XINE - obs퀅ga arts
Summary(pt_BR):	XINE - suporte a arts
Group:		Libraries
Provides:	xine-plugin-audio
Requires:	%{name} = %{version}

%description arts
XINE audio plugin with arts support.

%description arts -l pl
Wtyczka audio do XINE z obs퀅g� arts.

%package esd
Summary:	XINE - esd support
Summary(pl):	XINE - obs퀅ga esd
Summary(pt_BR):	XINE - suporte a esd
Group:		Libraries
Provides:	xine-plugin-audio
Requires:	%{name} = %{version}

%description esd
XINE audio plugin with esd support.

%description esd -l pl
Wtyczka audio do XINE z obs퀅g� esd.

%description esd -l pt_BR
Plugin de audio para o xine, com suporte a esd.

%package dxr3
Summary:	XINE - DXR3 support
Summary(pl):	XINE - obs퀅ga DXR3
Group:		Libraries
Requires:	%{name} = %{version}

%description dxr3
XINE video/decoder plugins for DXR3 card support.

%description dxr3 -l pl
Wtyczka odtwarzacza obrazu do XINE z obs퀅g� kart DXR3.

%package xvid
Summary:	XINE - xvid DIVX decoding support
Summary(pl):	XINE - obs퀅ga dekodera DIVX xvid
Group:		Libraries
Requires:	%{name} = %{version}

%description xvid
XINE decoder plugin for DIVX decoding with xvid library.

%description xvid -l pl
Wtyczka dla XINE do dekodowania DIVX poprzez bibliotek� xvid.

%package xv
Summary:	XINE - XFree XVideo support
Summary(pl):	XINE - obs퀅ga XFree XVideo
Summary(pt_BR):	XINE - suporte a XFree XVideo
Group:		Libraries
Requires:	%{name} = %{version}

%description xv
XINE video plugin using XFree XVideo extension.

%description xv -l pl
Wtyczka video do XINE u퓓waj켧a rozszerzenia XVideo.

%description xv -l pt_BR
Plugin de video para o xine, utilizando a extens�o XVideo do XFree.

%package aa
Summary:	XINE - Ascii Art support
Summary(pl):	XINE - obs퀅ga Ascii Art
Summary(pt_BR):	XINE - suporte a aalib
Group:		Libraries
Requires:	%{name} = %{version}

%description aa
XINE video plugin using Ascii Art library.

%description aa -l pl
Wtyczka video do XINE z obs퀅g� Ascii Art.

%description aa -l pt_BR
Plugin de video para o xine, utilizando a aalib.

%package xshm
Summary:	XINE - XFree XShm support
Summary(pl):	XINE - obs퀅ga XFree XShm
Group:		Libraries
Requires:	%{name} >= %{version}

%description xshm
XINE video plugin using XFree MIT shared memory.

%description xshm -l pl
Wtyczka video do XINE z obs퀅g� XFree MIT shared memory.

%package syncfb
Summary:	XINE - SyncFB (Matrox G200/G400) support
Summary(pl):	XINE - obs퀅ga SyncFB (Matrox G200/G400)
Group:		Libraries
Requires:	%{name} = %{version}

%description syncfb
SyncFB (for Matrox G200/G400 cards) interface for xine.

%description syncfb -l pl
Wtyczka video do XINE obs퀅guj켧a interfejs SyncFB (dla kart Matrox G200/G400).

%package fb
Summary:	XINE - framebuffer support
Summary(pl):	XINE - obs퀅ga framebuffera
Group:		Libraries
Requires:	%{name} = %{version}

%description fb
SyncFB (for Matrox G200/G400 cards) interface for xine.

%description fb -l pl
Wtyczka video do XINE dla framebuffera.

%package directfb
Summary:	XINE - accelereted framebuffer support
Summary(pl):	XINE - obs퀅ga akelereowanego framebuffera
Group:		Libraries
Requires:	%{name} = %{version}

%description directfb
XINE plugin for accelereted framebuffer support (with DirectFB
library).

%description directfb -l pl
Wtyczka video do XINE dla akcelerowanego framebuffera (przez
bibliotek� DirectFB).

%package sdl
Summary:	XINE - SDL output support
Summary(pl):	XINE - obs퀅ga wyj턢ia SDL
Group:		Libraries
Requires:	%{name} = %{version}

%description sdl
XINE plugin for output with SDL library.

%description sdl -l pl
Wtyczka video do XINE dla wy턻ieltania poprzez bibliotek� SDL.

%package opengl
Summary:	XINE - OpenGL video output
Summary(pl):	XINE - wy턻ietlanie OpenGL
Group:		Libraries
Requires:	%{name} = %{version}
Requires:	OpenGL

%description opengl
XINE plugin using OpenGL for video output.

%description opengl -l pl
Wtyczka video do XINE wykorzystuj켧a OpenGL do wy턻ietlania.

%package w32dll
Summary:	XINE - win32dll decoder support
Summary(pl):	XINE - obs퀅ga dekodera win32dll
Summary(pt_BR):	XINE - suporte a decoder win32dll
Group:		Libraries
Requires:	%{name} = %{version}
Requires:	w32codec

%description w32dll
XINE win32dll decoder support.

%description w32dll -l pl
Obs퀅ga dekodera win32dll do XINE.

%description w32dll -l pt_BR
Suporte a win32dll para o xine.

%package devel
Summary:	XINE - development files
Summary(pl):	Pliki dla programist�w XINE
Summary(pt_BR):	XINE - arquivos de desenvolvimento
Group:		Development/Libraries
Requires:	%{name} = %{version}
Obsoletes:	xine-devel

%description devel
HTML documentation of XINE API and development components.

%description devel -l pl
Pliki dla programist�w oraz dokumentacja HTML do API XINE.

%description devel -l pt_BR
Arquivos include a bibliotecas est�ticas necess�rias para compilar
plugins para o xine e o xine-ui.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
rm -f missing
%{__libtoolize}
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__automake}
autoheader

%configure \
%{!?_without_aa:	--with-aalib-prefix=/usr} \
%{!?_without_alsa:	--enable-alsa} \
%{?_without_alsa:	--disable-alsa} \
%{!?_without_dxr3:	--enable-dxr3} \
%{?_without_dxr3:	--disable-dxr3} \
			--disable-vidix

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_aclocaldir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

mv $RPM_BUILD_ROOT%{_datadir}/locale/pl_PL $RPM_BUILD_ROOT%{_datadir}/locale/pl

%find_lang %{name}

rm -f doc/xine-lib-API/{Makefile*,html/Makefile*}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxine*.so.*.*
%dir %{_datadir}/xine
%{_datadir}/xine/fonts
%{_datadir}/xine/skins
%dir %{_libdir}/xine
%dir %{_pluginsdir}
%doc AUTHORS ChangeLog TODO doc/xine-lib-API

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
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_film.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_mpeg*.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_ogg.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_qt.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_roq.so

# new
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_fli.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_idcin.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_smjpeg.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_wav.so

# decoder plugins
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_a52.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_adpcm.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_cinepak.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_cyuv.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_divx4.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_dts.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_ff.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_lpcm.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_mad.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_mpeg2.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_msvc.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_roqaudio.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_roqvideo.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_spu.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_spucc.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_sputext.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_svq1.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_vorbis.so

# new
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_faad.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_fli.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_msrle.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_rgb.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_yuv.so

%files oss
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/*oss.so

%if %{?_with_directfb:1}%{!?_with_directfb:0}
%files directfb
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/*_directfb.so
%endif

%if %{?_without_sdl:0}%{!?_without_sdl:1}
%files sdl
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/*_sdl.so
%endif

%if %{?_without_xvid:0}%{!?_without_xvid:1}
%files xvid
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_xvid.so
%endif

%if %{?_without_alsa:0}%{!?_without_alsa:1}
%files alsa
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/*alsa*.so
%endif

%if %{?_without_arts:0}%{!?_without_arts:1}
%files arts
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/*arts.so
%endif

%if %{?_without_esd:0}%{!?_without_esd:1}
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

%if %{?_without_aa:0}%{!?_without_aa:1}
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

%if %{?_without_opengl:0}%{!?_without_opengl:1}
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
%{_aclocaldir}/*.m4
