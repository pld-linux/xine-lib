# Conditional build:
# --without	aa
# --without	alsa05
# --with	alsa09
# --without	arts
# --without	esd
# --without	oss
# --with	dxr3

Summary:	A Free Video Player.
Summary(pl):	Odtwarzacz video
Summary(ko):	°ø°³ µ¿¿µ»ó ÇÃ·¹ÀÌ¾î
Name:		xine-lib
Version:	0.5.0
Release:	2
License:	GPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	http://xine.sourceforge.net/files/%{name}-%{version}.tar.gz
URL:		http://xine.sourceforge.net
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libtool
%{!?_without_aa:BuildRequires: aalib-devel}
%{!?_without_aa:BuildRequires: aalib-progs}
%{!?_without_esd:BuildRequires: esound-devel}
%{!?_without_arts:BuildRequires: arts-devel}
%ifarch %{ix86}
%{!?_without_alsa05:BuildRequires: alsa-lib-devel}
%{?_with_alsa09:BuildRequires: alsa-lib-devel}
%endif
Obsoletes:	xine
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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


%package oss
Summary:	XINE - OSS support.
Summary(pl):	XINE - obs³uga OSS.
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	xine-lib >= 0.5.0

%description oss
audio plugin with OSS support.

%description -l pl oss
Plugin audio z obs³ug± OSS

%ifarch %{ix86}
%package alsa05
Summary:	XINE - alsa 0.5.x support.
Summary(pl):	XINE - obs³uga alsa 0.5.x.
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	xine-lib >= 0.5.0

%description alsa05
audio plugin with alsa 0.5.x support.

%description -l pl alsa05
Plugin audio z obs³ug± Alsa 0.5.x .

%package alsa09
Summary:	XINE - alsa >= 0.9.x support.
Group:		Libraries
Requires:	xine-lib >= 0.5.0

%description alsa09
audio plugin with alsa >= 0.9.x support.
%endif

%package arts
Summary:	XINE - arts support.
Summary(pl):	XINE - obs³uga arts.
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	xine-lib >= 0.5.0

%description arts
audio plugin with arts support.

%description -l pl arts
Plugin audio z obs³ug± arts.

%package esd
Summary:	XINE - esd support.
Summary(pl):	XINE - obs³uga esd.
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	xine-lib >= 0.5.0, libesd

%description esd
audio plugin with esd support.

%description -l pl esd
plugin d¼wiêkowy z obs³ug± esd.

%package dxr3
Summary:	XINE - DXR3 support.
Group:		Libraries
Requires:	xine-lib >= 0.5.0

%description dxr3
video/decoder plugins for DXR3 card support.

%package xv
Summary:	XINE - XFree XVideo support.
Summary(pl):	XINE - obs³uga XFree XVideo.
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	xine-lib >= 0.5.0

%description xv
video plugin using XFree XVideo extension.

%description -l pl xv
Plugin video z obs³ug± XFree XVideo.

%package xshm
Summary:	XINE - XFree XShm support.
Summary(pl):	XINE - obs³uga XFree XShm.
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	xine-lib >= 0.5.0

%description xshm
video plugin using XFree XShm extension.

%description -l pl xshm
Plugin video z obs³ug± XFree XShm.

%package aa
Summary:	XINE - Ascii Art support.
Summary(pl):	XINE - obs³uga Ascii Art.
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	xine-lib >= 0.5.0, libaa

%description aa
video plugin using Ascii Art library.

%description -l pl aa
Plugin video z obs³ug± Ascii Art.

%package w32dll
Summary:	XINE - win32dll decoder support.
Summary(pl):	XINE - obs³uga dekodera win32dll.
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	xine-lib >= 0.5.0
Requires:	w32codec

%description w32dll
win32dll decoder support.

%description -l pl w32dll
Obs³uga dekodera win32dll.

%package devel
Summary:	XINE - development files
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki

%description devel
HTML documentation of XINE API and development components.



%prep
%setup -q -n xine-lib-0.5.0

%build
aclocal -I m4
%configure2_13 \
	--exec-prefix=%{_prefix}
	
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_datadir}/xine/skins

%attr(755,root,root) %{_libdir}/libxine*.so*
# input plugins
%attr(644,root,root) %{_pluginsdir}/xineplug_inp_dvd.so
%attr(644,root,root) %{_pluginsdir}/xineplug_inp_file.so
%attr(644,root,root) %{_pluginsdir}/xineplug_inp_net.so
%attr(644,root,root) %{_pluginsdir}/xineplug_inp_rtp.so
%attr(644,root,root) %{_pluginsdir}/xineplug_inp_stdin_fifo.so
%attr(644,root,root) %{_pluginsdir}/xineplug_inp_vcd.so
# demuxer plugins
%attr(644,root,root) %{_pluginsdir}/xineplug_dmx_avi.so
%attr(644,root,root) %{_pluginsdir}/xineplug_dmx_mpeg.so
%attr(644,root,root) %{_pluginsdir}/*mpeg_*.so
# decoder plugins
%attr(644,root,root) %{_pluginsdir}/xineplug_decode_ac3.so
%attr(644,root,root) %{_pluginsdir}/xineplug_decode_mpeg2.so
%attr(644,root,root) %{_pluginsdir}/xineplug_decode_mpg123.so
%attr(644,root,root) %{_pluginsdir}/xineplug_decode_spu.so
# video driver plugins
%attr(644,root,root) %{_pluginsdir}/xineplug_vo_out_syncfb.so

%{!?_without_oss:%files oss}
%{!?_without_oss:%defattr(644,root,root,755)}
%{!?_without_oss:%attr(644,root,root) %{_pluginsdir}/*oss.so}

%{!?_without_alsa05:%files alsa05}
%{!?_without_alsa05:%defattr(644,root,root,755)}
%{!?_without_alsa05:%attr(644,root,root) %{_pluginsdir}/*alsa05.so}

%{?_with_alsa09:%files alsa09}
%{?_with_alsa09:%attr(644,root,root) %{_prefix}/lib/xine/plugins/xineplug_ao_out_alsa.so}

%{!?_without_arts:%files arts}
%{!?_without_arts:%defattr(644,root,root,755)}
%{!?_without_arts:%attr(644,root,root) %{_pluginsdir}/*arts.so}

%{!?_without_esd:%files esd}
%{!?_without_esd:%defattr(644,root,root,755)}
%{!?_without_esd:%attr(644,root,root) %{_pluginsdir}/*esd.so}

%{?_with_dxr3:%files dxr3}
%{?_with_dxr3:%attr(644,root,root) %{_prefix}/lib/xine/plugins/xineplug_decode_dxr3.so}
%{?_with_dxr3:%attr(644,root,root) %{_prefix}/lib/xine/plugins/xineplug_vo_out_dxr3.so}

%files xv
%defattr(644,root,root,755)
%attr(644,root,root) %{_pluginsdir}/*xv.so

%files xshm
%defattr(644,root,root,755)
%attr(644,root,root) %{_pluginsdir}/*xshm.so

%{!?_without_aa:%files aa}
%{!?_without_aa:%defattr(644,root,root,755)}
%{!?_without_aa:%attr(644,root,root) %{_pluginsdir}/*aa.so}

%files w32dll
%defattr(644,root,root,755)
%attr(644,root,root) %{_pluginsdir}/*w32dll.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xine-config
%{_includedir}/xine/*.h
%{_includedir}/xine.h
%{_pluginsdir}/*.la
%{_libdir}/libxine*.la
%doc %{_mandir}/man3/*.3.*
%doc doc/xine/xine-lib-API/*.html
