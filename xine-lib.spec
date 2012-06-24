# Conditional build:
# --without	aa
# --with	alsa
# --without	arts
# --without	esd
# --without	oss
# --with	dxr3

Summary:	A Free Video Player
Summary(pl):	Odtwarzacz video
Summary(ko):	���� ������ �÷��̾�
Name:		xine-lib
Version:	0.5.3
Release:	1
License:	GPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	http://xine.sourceforge.net/files/%{name}-%{version}.tar.gz
Patch0:		%{name}-configure.patch
Patch1:		%{name}-stubs.patch
URL:		http://xine.sourceforge.net/
%{!?_without_aa:BuildRequires:	aalib-devel}
%{!?_without_aa:BuildRequires:	aalib-progs}
%{!?_without_esd:BuildRequires:	esound-devel}
%ifnarch alpha
%{!?_without_arts:BuildRequires:	arts-devel}
%endif
%ifnarch sparc sparc64
%{!?_without_alsa:BuildRequires:	alsa-lib-devel}
%endif
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
xine �� GPL���̼����� ������ UNIX�� ���� ������ �÷��̾��Դϴ�. ��
�÷��̾�� mpeg-2 �� mpeg 1 ��Ʈ���� �����ϸ�, ����� �������� ������
���߿��� mpeg-4 �� �ٸ� ������ ������ ������ �����Դϴ�.

%package oss
Summary:	XINE - OSS/ALSA support
Summary(pl):	XINE - obs�uga OSS/ALSA
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	xine-lib >= 0.5.0

%description oss
Audio plugins with OSS/ALSA support.

%description -l pl oss
Plugin audio z obs�ug� OSS/ALSA.

%package alsa
Summary:	XINE - alsa support
Summary(pl):	XINE - obs�uga alsa
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name} >= %{version}

%description alsa
audio plugin with alsa support.

%description -l pl alsa
Plugin audio z obs�ug� ALSA.

%package arts
Summary:	XINE - arts support
Summary(pl):	XINE - obs�uga arts
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name} >= %{version}

%description arts
audio plugin with arts support.

%description -l pl arts
Plugin audio z obs�ug� arts.

%package esd
Summary:	XINE - esd support
Summary(pl):	XINE - obs�uga esd
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name} >= %{version}

%description esd
audio plugin with esd support.

%description -l pl esd
plugin d�wi�kowy z obs�ug� esd.

%package dxr3
Summary:	XINE - DXR3 support
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name} >= %{version}

%description dxr3
video/decoder plugins for DXR3 card support.

%package xv
Summary:	XINE - XFree XVideo support
Summary(pl):	XINE - obs�uga XFree XVideo
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name} >= %{version}

%description xv
video plugin using XFree XVideo extension.

%description -l pl xv
Plugin video z obs�ug� XFree XVideo.

%package aa
Summary:	XINE - Ascii Art support
Summary(pl):	XINE - obs�uga Ascii Art
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name} >= %{version}

%description aa
Video plugin using Ascii Art library.
 
%description -l pl aa
Plugin video z obs�ug� Ascii Art.

%package xshm
Summary:	XINE - XFree XShm support
Summary(pl):	XINE - obs�uga XFree XShm
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	xine-lib >= 0.5.0

%description xshm
video plugin using XFree XShm extension.

%package w32dll
Summary:	XINE - win32dll decoder support.
Summary(pl):	XINE - obs�uga dekodera win32dll.
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name} >= %{version}
Requires:	w32codec

%description w32dll
win32dll decoder support.

%description -l pl w32dll
Obs�uga dekodera win32dll.

%package devel
Summary:	XINE - development files
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} >= %{version}

%description devel
HTML documentation of XINE API and development components.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
libtoolize -c -f
aclocal
autoconf
automake -a -c
autoheader
%configure \
	--with-aalib-prefix=/usr
	
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf doc/FAQ doc/README.*

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxine*.so*
%dir %{_datadir}/xine/skins
%{_datadir}/xine/skins/*.png
%dir %{_pluginsdir}
%doc doc/FAQ.gz
%doc doc/README.xinerc.gz

# input plugins
%attr(755,root,root) %{_pluginsdir}/xineplug_inp_dvd.so
%attr(755,root,root) %{_pluginsdir}/xineplug_inp_file.so
%attr(755,root,root) %{_pluginsdir}/xineplug_inp_net.so
%attr(755,root,root) %{_pluginsdir}/xineplug_inp_rtp.so
%attr(755,root,root) %{_pluginsdir}/xineplug_inp_stdin_fifo.so
%attr(755,root,root) %{_pluginsdir}/xineplug_inp_vcd.so
# demuxer plugins
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_avi.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_mpeg.so
%attr(755,root,root) %{_pluginsdir}/*mpeg_*.so
# decoder plugins
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_lpcm.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_ff.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_mad.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_a52.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_mpeg2.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_spu.so
# video driver plugins
%attr(755,root,root) %{_pluginsdir}/xineplug_vo_out_syncfb.so
%attr(755,root,root) %{_pluginsdir}/xineplug_vo_out_xshm.so

%if %{!?_without_oss:1}
%files oss
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/*oss.so
%endif

%if %{!?_without_alsa:1}
%ifnarch sparc sparc64
%files alsa
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/*alsa*.so
%endif
%endif

%ifnarch alpha
%if %{!?_without_arts:1}
%files arts
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/*arts.so
%endif
%endif

%if %{!?_without_esd:1}
%files esd
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/*esd.so
%endif

%if %{!?_with_dxr3:0}
%files dxr3
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/xine/plugins/xineplug_decode_dxr3.so
%attr(755,root,root) %{_libdir}/xine/plugins/xineplug_vo_out_dxr3.so
%doc doc/README.dxr3.gz
%endif

%files xv
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/*xv.so

%if %{!?_without_aa:1}
%files aa
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/*aa.so
%endif

%files xshm
%defattr(644,root,root,755)
%attr(644,root,root) %{_pluginsdir}/*xshm.so

%ifarch %{x86}
%files w32dll
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/*w32dll.so
%endif

%files devel
%defattr(644,root,root,755)
%doc doc/xine-lib-API/html/*.{html,png,gif,css}
%attr(755,root,root) %{_bindir}/xine-config
%attr(755,root,root) %{_includedir}/*
%attr(755,root,root) %{_libdir}/libxine*.la
%attr(755,root,root) %{_pluginsdir}/*.la
%{_mandir}/man3/*
