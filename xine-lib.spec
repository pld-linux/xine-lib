# Conditional build:
# --without	aa
# --with	alsa	(alsa support is currently broken)
# --without	arts
# --without	esd
# --without	oss
# --with	dxr3

Summary:	A Free Video Player
Summary(ko):	공개 동영상 플레이어
Summary(pl):	Odtwarzacz video
Name:		xine-lib
Version:	0.9.7
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://xine.sourceforge.net/files/%{name}-%{version}.tar.gz
Patch0:		%{name}-am15.patch
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
BuildRequires:	libvorbis-devel
BuildRequires:	divx4linux-devel
BuildRequires:	libtool >= 1.4.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	xine

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

%package oss
Summary:	XINE - OSS/ALSA support
Summary(pl):	XINE - obs퀅ga OSS/ALSA
Group:		Libraries
Requires:	%{name} = %{version}

%description oss
XINE audio plugins with OSS/ALSA support.

%description oss -l pl
Wtyczka audio do XINE z obs퀅g� OSS/ALSA.

%package alsa
Summary:	XINE - alsa support
Summary(pl):	XINE - obs퀅ga alsa
Group:		Libraries
Requires:	%{name} = %{version}

%description alsa
XINE audio plugin with alsa support.

%description alsa -l pl
Wtyczka audio do XINE z obs퀅g� ALSA.

%package arts
Summary:	XINE - arts support
Summary(pl):	XINE - obs퀅ga arts
Group:		Libraries
Requires:	%{name} = %{version}

%description arts
XINE audio plugin with arts support.

%description -l pl arts
Wtyczka audio do XINE z obs퀅g� arts.

%package esd
Summary:	XINE - esd support
Summary(pl):	XINE - obs퀅ga esd
Group:		Libraries
Requires:	%{name} = %{version}

%description esd
XINE audio plugin with esd support.

%description esd -l pl
Wtyczka audio do XINE z obs퀅g� esd.

%package dxr3
Summary:	XINE - DXR3 support
Summary(pl):	XINE - obs퀅ga DXR3
Group:		Libraries
Requires:	%{name} = %{version}

%description dxr3
XINE video/decoder plugins for DXR3 card support.

%description dxr3 -l pl
Wtyczka odtwarzacza obrazu do XINE z obs퀅g� kart DXR3.

%package xv
Summary:	XINE - XFree XVideo support
Summary(pl):	XINE - obs퀅ga XFree XVideo
Group:		Libraries
Requires:	%{name} = %{version}

%description xv
XINE video plugin using XFree XVideo extension.

%description xv -l pl
Wtyczka video do XINE u퓓waj켧a rozszerzenia XVideo.

%package aa
Summary:	XINE - Ascii Art support
Summary(pl):	XINE - obs퀅ga Ascii Art
Group:		Libraries
Requires:	%{name} = %{version}

%description aa
XINE video plugin using Ascii Art library.

%description aa -l pl
Wtyczka video do XINE z obs퀅g� Ascii Art.

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
Summary:	XINE - Framebuffer support
Summary(pl):	XINE - obs퀅ga framebuffera
Group:		Libraries
Requires:	%{name} = %{version}

%description syncfb
XINE video plugin using framebuffer.

%description syncfb -l pl
Wtyczka video do XINE z obs퀅g� framebuffera.

%package w32dll
Summary:	XINE - win32dll decoder support
Summary(pl):	XINE - obs퀅ga dekodera win32dll
Group:		Libraries
Requires:	%{name} = %{version}
Requires:	w32codec

%description w32dll
XINE win32dll decoder support.

%description w32dll -l pl
Obs퀅ga dekodera win32dll do XINE.

%package devel
Summary:	XINE - development files
Summary(pl):	Pliki dla programist�w XINE
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
HTML documentation of XINE API and development components.

%description devel -l pl
Pliki dla programist�w oraz dokumentacja HTML do API XINE.

%prep
%setup -q
#%patch0 -p1

%build
rm -f missing
libtoolize -c -f
aclocal
autoconf
automake -a -c
autoheader
%configure \
	--with-aalib-prefix=/usr \
%{?_with_alsa:	--enable-alsa} \
%{!?_with_alsa:	--disable-alsa}
	
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS ChangeLog

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxine*.so*
%dir %{_datadir}/xine
%dir %{_datadir}/xine/skins
%{_datadir}/xine/skins/*.png
%dir %{_libdir}/xine
%dir %{_pluginsdir}
%doc *.gz

# input plugins
%attr(755,root,root) %{_pluginsdir}/xineplug_inp_dvd.so
%attr(755,root,root) %{_pluginsdir}/xineplug_inp_file.so
%attr(755,root,root) %{_pluginsdir}/xineplug_inp_http.so
%attr(755,root,root) %{_pluginsdir}/xineplug_inp_net.so
%attr(755,root,root) %{_pluginsdir}/xineplug_inp_rtp.so
%attr(755,root,root) %{_pluginsdir}/xineplug_inp_stdin_fifo.so
%attr(755,root,root) %{_pluginsdir}/xineplug_inp_vcd.so
# demuxer plugins
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_asf.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_avi.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_mpeg.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_ogg.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_qt.so
%attr(755,root,root) %{_pluginsdir}/*mpeg_*.so
# decoder plugins
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_a52.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_divx4.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_dts.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_ff.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_lpcm.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_mad.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_mpeg2.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_spu.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_vfill.so
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
%attr(755,root,root) %{_pluginsdir}/*.la
%{_mandir}/man3/*
