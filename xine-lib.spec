
Summary:	A Free Video Player.
Summary(pl):	Odtwarzacz video
Summary(ko):	공개 동영상 플레이어
Name:		xine-lib
Version:	0.5.0
Release:	1
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
BuildRequires:	aalib-devel
BuildRequires:	aalib-progs
BuildRequires:	esound-devel
BuildRequires:	arts-devel
%ifarch %{ix86}
BuildRequires:	alsa-lib-devel
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


%package oss
Summary:	XINE - OSS support.
Summary(pl):	XINE - obs퀅ga OSS.
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	xine-lib >= 0.5.0

%description oss
audio plugin with OSS support.

%description -l pl oss
Plugin audio z obs퀅g� OSS

%ifarch %{ix86}
%package alsa05
Summary:	XINE - alsa 0.5.x support.
Summary(pl):	XINE - obs퀅ga alsa 0.5.x.
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	xine-lib >= 0.5.0

%description alsa05
audio plugin with alsa 0.5.x support.

%description -l pl alsa05
Plugin audio z obs퀅g� Alsa 0.5.x .

# This may be as a bcond (there is support for that)
#%package alsa09
#Summary:	XINE - alsa >= 0.9.x support.
#Group:		Libraries
#Requires:	xine-lib >= 0.5.0

#%description alsa09
#audio plugin with alsa >= 0.9.x support.
%endif

%package arts
Summary:	XINE - arts support.
Summary(pl):	XINE - obs퀅ga arts.
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	xine-lib >= 0.5.0

%description arts
audio plugin with arts support.

%description -l pl arts
Plugin audio z obs퀅g� arts.

%package esd
Summary:	XINE - esd support.
Summary(pl):	XINE - obs퀅ga esd.
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	xine-lib >= 0.5.0, libesd

%description esd
audio plugin with esd support.

%description -l pl esd
plugin d펧i�kowy z obs퀅g� esd.

# does anyone need this??
#%package dxr3
#Summary:	XINE - DXR3 support.
#Group:		Libraries
#Requires:	xine-lib >= 0.5.0

#%description dxr3
#video/decoder plugins for DXR3 card support.

%package xv
Summary:	XINE - XFree XVideo support.
Summary(pl):	XINE - obs퀅ga XFree XVideo.
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	xine-lib >= 0.5.0

%description xv
video plugin using XFree XVideo extension.

%description -l pl xv
Plugin video z obs퀅g� XFree XVideo.

%package aa
Summary:	XINE - Ascii Art support.
Summary(pl):	XINE - obs퀅ga Ascii Art.
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	xine-lib >= 0.5.0, libaa

%description aa
video plugin using Ascii Art library.

%description -l pl aa
Plugin video z obs퀅g� Ascii Art.

%package w32dll
Summary:	XINE - win32dll decoder support.
Summary(pl):	XINE - obs퀅ga dekodera win32dll.
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
Obs퀅ga dekodera win32dll.

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
	--prefix=%{_prefix} \
	--with-aalib-prefix=/usr
	
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_datadir}/xine/skins
%{_mandir}/man3/*.3.*

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
%attr(644,root,root) %{_pluginsdir}/xineplug_vo_out_xshm.so

%files oss
%defattr(644,root,root,755)
%attr(644,root,root) %{_pluginsdir}/*oss.so

%files alsa05
%defattr(644,root,root,755)
%attr(644,root,root) %{_pluginsdir}/*alsa05.so

#%files alsa09
#%attr(644,root,root) %{_prefix}/lib/xine/plugins/xineplug_ao_out_alsa.so

%files arts
%defattr(644,root,root,755)
%attr(644,root,root) %{_pluginsdir}/*arts.so

%files esd
%defattr(644,root,root,755)
%attr(644,root,root) %{_pluginsdir}/*esd.so

#%files dxr3
#%attr(644,root,root) %{_prefix}/lib/xine/plugins/xineplug_decode_dxr3.so
#%attr(644,root,root) %{_prefix}/lib/xine/plugins/xineplug_vo_out_dxr3.so

%files xv
%defattr(644,root,root,755)
%attr(644,root,root) %{_pluginsdir}/*xv.so

%files aa
%defattr(644,root,root,755)
%attr(644,root,root) %{_pluginsdir}/*aa.so

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
%doc doc/xine/xine-lib-API/*.html
