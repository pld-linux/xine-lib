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

%ifarch alpha
%define		_without_arts	1
%define		_without_xvid	1
%endif
%ifarch sparc sparc64
%define		_without_alsa	1
%define		_without_xvid	1
%endif

%define		_version	1-beta2

Summary:	A Free Video Player
Summary(ko.UTF-8):   공개 동영상 플레이어
Summary(pl.UTF-8):   Odtwarzacz video
Summary(pt_BR.UTF-8):   Xine, um player de video
Name:		xine-lib
Version:	1.0b2
Release:	2
License:	GPL
Group:		Libraries
Source0:	http://prdownloads.sourceforge.net/xine/%{name}-%{_version}.tar.gz
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
BuildRequires:	libvorbis-devel
BuildRequires:	libtool >= 0:1.4.2-9
BuildRequires:	pkgconfig
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	xine
Obsoletes:	xine-libs

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

%description -l fr.UTF-8
xine est un lecteur vidéo libre sous license GPL pour les systèmes de
type unix. Nous supportons les flux mpeg-2 et mpeg-1 (audio + vidéo
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
xine jest wolnodostępnym odtwarzaczem video dla systemów uniksowych.
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

%package oss
Summary:	XINE - OSS/ALSA support
Summary(pl.UTF-8):   XINE - obsługa OSS/ALSA
Summary(pt_BR.UTF-8):   XINE - suporte a oss
Group:		Libraries
Provides:	xine-plugin-audio
Requires:	%{name} = %{version}

%description oss
XINE audio plugins with OSS/ALSA support.

%description oss -l pl.UTF-8
Wtyczka audio do XINE z obsługą OSS/ALSA.

%description oss -l pt_BR.UTF-8
Plugin de audio para o xine, com suporte a oss.

%package alsa
Summary:	XINE - alsa support
Summary(pl.UTF-8):   XINE - obsługa alsa
Summary(pt_BR.UTF-8):   XINE - suporte a alsa
Group:		Libraries
Provides:	xine-plugin-audio
Requires:	%{name} = %{version}

%description alsa
XINE audio plugin with alsa support.

%description alsa -l pl.UTF-8
Wtyczka audio do XINE z obsługą ALSA.

%description alsa -l pt_BR.UTF-8
Plugin de audio para o xine, com suporte a alsa.

%package arts
Summary:	XINE - arts support
Summary(pl.UTF-8):   XINE - obsługa arts
Summary(pt_BR.UTF-8):   XINE - suporte a arts
Group:		Libraries
Provides:	xine-plugin-audio
Requires:	%{name} = %{version}

%description arts
XINE audio plugin with arts support.

%description arts -l pl.UTF-8
Wtyczka audio do XINE z obsługą arts.

%package esd
Summary:	XINE - esd support
Summary(pl.UTF-8):   XINE - obsługa esd
Summary(pt_BR.UTF-8):   XINE - suporte a esd
Group:		Libraries
Provides:	xine-plugin-audio
Requires:	%{name} = %{version}

%description esd
XINE audio plugin with esd support.

%description esd -l pl.UTF-8
Wtyczka audio do XINE z obsługą esd.

%description esd -l pt_BR.UTF-8
Plugin de audio para o xine, com suporte a esd.

%package dxr3
Summary:	XINE - DXR3 support
Summary(pl.UTF-8):   XINE - obsługa DXR3
Group:		Libraries
Requires:	%{name} = %{version}

%description dxr3
XINE video/decoder plugins for DXR3 card support.

%description dxr3 -l pl.UTF-8
Wtyczka odtwarzacza obrazu do XINE z obsługą kart DXR3.

%package xvid
Summary:	XINE - xvid DIVX decoding support
Summary(pl.UTF-8):   XINE - obsługa dekodera DIVX xvid
Group:		Libraries
Requires:	%{name} = %{version}

%description xvid
XINE decoder plugin for DIVX decoding with xvid library.

%description xvid -l pl.UTF-8
Wtyczka dla XINE do dekodowania DIVX poprzez bibliotekę xvid.

%package xv
Summary:	XINE - XFree XVideo support
Summary(pl.UTF-8):   XINE - obsługa XFree XVideo
Summary(pt_BR.UTF-8):   XINE - suporte a XFree XVideo
Group:		Libraries
Requires:	%{name} = %{version}

%description xv
XINE video plugin using XFree XVideo extension.

%description xv -l pl.UTF-8
Wtyczka video do XINE używająca rozszerzenia XVideo.

%description xv -l pt_BR.UTF-8
Plugin de video para o xine, utilizando a extensão XVideo do XFree.

%package aa
Summary:	XINE - Ascii Art support
Summary(pl.UTF-8):   XINE - obsługa Ascii Art
Summary(pt_BR.UTF-8):   XINE - suporte a aalib
Group:		Libraries
Requires:	%{name} = %{version}

%description aa
XINE video plugin using Ascii Art library.

%description aa -l pl.UTF-8
Wtyczka video do XINE z obsługą Ascii Art.

%description aa -l pt_BR.UTF-8
Plugin de video para o xine, utilizando a aalib.

%package xshm
Summary:	XINE - XFree XShm support
Summary(pl.UTF-8):   XINE - obsługa XFree XShm
Group:		Libraries
Requires:	%{name} >= %{version}

%description xshm
XINE video plugin using XFree MIT shared memory.

%description xshm -l pl.UTF-8
Wtyczka video do XINE z obsługą XFree MIT shared memory.

%package syncfb
Summary:	XINE - SyncFB (Matrox G200/G400) support
Summary(pl.UTF-8):   XINE - obsługa SyncFB (Matrox G200/G400)
Group:		Libraries
Requires:	%{name} = %{version}

%description syncfb
SyncFB (for Matrox G200/G400 cards) interface for xine.

%description syncfb -l pl.UTF-8
Wtyczka video do XINE obsługująca interfejs SyncFB (dla kart Matrox G200/G400).

%package fb
Summary:	XINE - framebuffer support
Summary(pl.UTF-8):   XINE - obsługa framebuffera
Group:		Libraries
Requires:	%{name} = %{version}

%description fb
SyncFB (for Matrox G200/G400 cards) interface for xine.

%description fb -l pl.UTF-8
Wtyczka video do XINE dla framebuffera.

%package directfb
Summary:	XINE - accelereted framebuffer support
Summary(pl.UTF-8):   XINE - obsługa akelereowanego framebuffera
Group:		Libraries
Requires:	%{name} = %{version}

%description directfb
XINE plugin for accelereted framebuffer support (with DirectFB
library).

%description directfb -l pl.UTF-8
Wtyczka video do XINE dla akcelerowanego framebuffera (przez
bibliotekę DirectFB).

%package sdl
Summary:	XINE - SDL output support
Summary(pl.UTF-8):   XINE - obsługa wyjścia SDL
Group:		Libraries
Requires:	%{name} = %{version}

%description sdl
XINE plugin for output with SDL library.

%description sdl -l pl.UTF-8
Wtyczka video do XINE dla wyświeltania poprzez bibliotekę SDL.

%package opengl
Summary:	XINE - OpenGL video output
Summary(pl.UTF-8):   XINE - wyświetlanie OpenGL
Group:		Libraries
Requires:	%{name} = %{version}
Requires:	OpenGL

%description opengl
XINE plugin using OpenGL for video output.

%description opengl -l pl.UTF-8
Wtyczka video do XINE wykorzystująca OpenGL do wyświetlania.

%package w32dll
Summary:	XINE - win32dll decoder support
Summary(pl.UTF-8):   XINE - obsługa dekodera win32dll
Summary(pt_BR.UTF-8):   XINE - suporte a decoder win32dll
Group:		Libraries
Requires:	%{name} = %{version}
Requires:	w32codec

%description w32dll
XINE win32dll decoder support.

%description w32dll -l pl.UTF-8
Obsługa dekodera win32dll do XINE.

%description w32dll -l pt_BR.UTF-8
Suporte a win32dll para o xine.

%package devel
Summary:	XINE - development files
Summary(pl.UTF-8):   Pliki dla programistów XINE
Summary(pt_BR.UTF-8):   XINE - arquivos de desenvolvimento
Group:		Development/Libraries
Requires:	%{name} = %{version}
Obsoletes:	xine-devel

%description devel
HTML documentation of XINE API and development components.

%description devel -l pl.UTF-8
Pliki dla programistów oraz dokumentacja HTML do API XINE.

%description devel -l pt_BR.UTF-8
Arquivos include a bibliotecas estáticas necessárias para compilar
plugins para o xine e o xine-ui.

%package	vidix-rage128
Summary:	VIDIX based video driver for Rage128 chips
Summary(pl.UTF-8):   Moduły video oparte na VIDIX dla chipsetow Rage128
Group:		Libraries
Requires:       %{name} = %{version}

%description	vidix-rage128
VIDIX based video driver for Rage128 chips.

%description 	vidix-rage128 -l pl.UTF-8
Moduły video oparte na VIDIX dla chipsetow Rage128.

%package        vidix-radeon
Summary:	VIDIX based video driver for Radeon chips
Summary(pl.UTF-8):   Moduły video oparte na VIDIX dla chipsetow Radeon
Group:          Libraries
Requires:       %{name} = %{version}

%description	vidix-radeon
VIDIX based video driver for Radeon chips.

%description 	vidix-radeon -l pl.UTF-8
Moduły video oparte na VIDIX dla chipsetow Radeon.

%package        vidix-nvidia
Summary:	VIDIX based video driver for Riva and Riva-derived chips
Summary(pl.UTF-8):   Moduły video oparte na VIDIX dla chipsetow Riva oraz pochodnych
Group:          Libraries
Requires:       %{name} = %{version}

%description	vidix-nvidia
VIDIX based video driver for Riva and Riva-derived chips, ex. riva tnt, geforce 2.

%description  	vidix-nvidia -l pl.UTF-8
Moduły video oparte na VIDIX dla chipsetow Riva oraz pochodnych.

%package        vidix-permedia
Summary:	VIDIX based video driver for 3Dlabs GLINT R3 and Permedia chips
Summary(pl.UTF-8):   Moduły video oparte na VIDIX dla chipsetow 3Dlabs GLINT R3 oraz Permedia
Group:          Libraries
Requires:       %{name} = %{version}

%description	vidix-permedia
VIDIX based video driver for 3Dlabs GLINT R3 and Permedia chips.

%description 	vidix-permedia -l pl.UTF-8
Moduły video oparte na VIDIX dla chipsetow 3Dlabs GLINT R3 oraz Permedia.

%package        vidix-matrox
Summary:	VIDIX based video driver for Matrox Mga chips
Summary(pl.UTF-8):   Moduły video oparte na VIDIX dla chipsetow Matrox Mga
Group:          Libraries
Requires:       %{name} = %{version}

%description	vidix-matrox
VIDIX based video driver for Matrox Mga chips.

%description 	vidix-matrox -l pl.UTF-8
Moduły video oparte na VIDIX dla chipsetow Matrox Mga.

%package        vidix-mach64
Summary:	VIDIX based video driver for Mach64 and 3Drage chips
Summary(pl.UTF-8):   Moduły video oparte na VIDIX dla chipsetow Mach64 oraz 3DRage
Group:          Libraries
Requires:       %{name} = %{version}

%description
VIDIX based video driver for Mach64 and 3Drage chips.

%description	vidix-mach64 -l pl.UTF-8
Moduły video oparte na VIDIX dla chipsetow Mach64 oraz 3DRage/

%prep
%setup -q -n %{name}-%{_version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
rm -f missing
#%%{__libtoolize}
#%%{__gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}

%configure \
CPPFLAGS=-I/usr/include/xvid \
%{!?_without_aa:	--with-aalib-prefix=/usr} \
%{!?_without_alsa:	--enable-alsa} \
%{?_without_alsa:	--disable-alsa} \
%{?_with_dxr3:		--enable-dxr3} \
%{!?_with_dxr3:		--disable-dxr3}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_aclocaldir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

mv $RPM_BUILD_ROOT%{_datadir}/locale/pl_PL $RPM_BUILD_ROOT%{_datadir}/locale/pl

%find_lang libxine1

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f libxine1.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog TODO
%attr(755,root,root) %{_libdir}/libxine*.so.*.*
#dir %{_datadir}/xine
%{_datadir}/xine/libxine1/fonts
#{_datadir}/xine/skins
#dir %{_libdir}/xine
#dir %{_pluginsdir}
#dir %{_pluginsdir}/post 
#attr(755,root,root) %{_pluginsdir}/post/*.so
#dir %{_pluginsdir}/vidix 
#attr(755,root,root) %{_pluginsdir}/vidix/*.so

# input plugins
#%attr(755,root,root) %{_pluginsdir}/xineplug_inp_cda.so
%attr(755,root,root) %{_pluginsdir}/xineplug_inp_dvd.so
%attr(755,root,root) %{_pluginsdir}/xineplug_inp_dvb.so
%attr(755,root,root) %{_pluginsdir}/xineplug_inp_net.so
%attr(755,root,root) %{_pluginsdir}/xineplug_inp_rtsp.so
%attr(755,root,root) %{_pluginsdir}/xineplug_inp_file.so
%attr(755,root,root) %{_pluginsdir}/xineplug_inp_http.so
%attr(755,root,root) %{_pluginsdir}/xineplug_inp_mms.so
#%attr(755,root,root) %{_pluginsdir}/xineplug_inp_net.so
#%attr(755,root,root) %{_pluginsdir}/xineplug_inp_rtp.so
%attr(755,root,root) %{_pluginsdir}/xineplug_inp_stdin_fifo.so
%attr(755,root,root) %{_pluginsdir}/xineplug_inp_vcd.so
# new
%attr(755,root,root) %{_pluginsdir}/xineplug_inp_pnm.so

# demuxer plugins
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_aiff.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_asf.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_avi.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_cda.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_film.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_fli.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_idcin.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_mpeg*.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_ogg.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_qt.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_roq.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_smjpeg.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_snd.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_voc.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_vqa.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_wav.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_wc3movie.so
# new
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_eawve.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_real.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_realaudio.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_yuv4mpeg2.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_ipmovie.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_mng.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_rawdv.so
%attr(755,root,root) %{_pluginsdir}/xineplug_dmx_sputext.so

# decoder plugins
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_a52.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_adpcm.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_cinepak.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_cyuv.so
#%attr(755,root,root) %{_pluginsdir}/xineplug_decode_divx4.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_dts.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_faad.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_ff.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_fli.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_idcinvideo.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_logpcm.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_lpcm.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_mad.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_mpeg2.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_msrle.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_msvc.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_qtrpza.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_qtsmc.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_rgb.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_roqaudio.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_roqvideo.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_spu.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_spucc.so
#%attr(755,root,root) %{_pluginsdir}/xineplug_decode_sputext.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_svq1.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_vorbis.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_yuv.so
# new
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_gsm610.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_qtrle.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_real.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_real_audio.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_wc3video.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_interplayaudio.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_interplayvideo.so
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_qt.so
%attr(755,root,root) %{_pluginsdir}/xineplug_vo_out_none.so
#attr(755,root,root) %{_pluginsdir}/xineplug_vo_out_sdl.so
#attr(755,root,root) %{_pluginsdir}/xineplug_vo_out_syncfb.so

%ifnarch ppc
# vidix vo plugin
%attr(755,root,root) %{_pluginsdir}/xineplug_vo_out_vidix.so
%endif

# new plugins
%attr(755,root,root) %{_pluginsdir}/post/xineplug_post_*.so


%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xine-config
%{_includedir}/*
%{_libdir}/libxine*.la
%attr(755,root,root) %{_libdir}/libxine*.so
%{_pluginsdir}/*.la
%{_pluginsdir}/post/*.la
%{_pluginsdir}/vidix/*.la
%{_mandir}/man[13]/*
%{_aclocaldir}/*.m4
%{_pkgconfigdir}/libxine.pc

%if %{?_without_aa:0}%{!?_without_aa:1}
%files aa
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/*aa.so
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

%if %{?_with_directfb:1}%{!?_with_directfb:0}
%files directfb
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/*_directfb.so
%endif

%if %{?_with_dxr3:1}%{!?_with_dxr3:0}
%files dxr3
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/xineplug_decode_dxr3.so
%attr(755,root,root) %{_pluginsdir}/xineplug_vo_out_dxr3.so
%endif

%if %{?_without_esd:0}%{!?_without_esd:1}
%files esd
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/*esd.so
%endif

%files fb
%defattr(644,root,root,755)
%attr(644,root,root) %{_pluginsdir}/*_fb.so

#if %{?_without_opengl:0}%{!?_without_opengl:1}
#files opengl
#defattr(644,root,root,755)
#attr(644,root,root) %{_pluginsdir}/*opengl.so
#endif

%files oss
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/*oss.so

%if %{?_without_sdl:0}%{!?_without_sdl:1}
%files sdl
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/*_sdl.so
%endif

%files syncfb
%defattr(644,root,root,755)
%attr(644,root,root) %{_pluginsdir}/*syncfb.so

%ifarch %{ix86}
%files w32dll
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/*w32dll.so
%endif

%files xshm
%defattr(644,root,root,755)
%attr(644,root,root) %{_pluginsdir}/*xshm.so

%files xv
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/*xv.so

%ifnarch ppc

%files vidix-rage128
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/vidix/rage128*.so

%files vidix-radeon
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/vidix/radeon*.so

%files vidix-nvidia
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/vidix/nvidia*.so

%files vidix-permedia
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/vidix/pm3*.so

%files vidix-mach64
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/vidix/mach64*.so

%files vidix-matrox
%defattr(644,root,root,755)
%attr(755,root,root) %{_pluginsdir}/vidix/mga*.so

# Please dont package vidix-genfb. genfb is just a sample driver.

%endif

#%if %{?_without_xvid:0}%{!?_without_xvid:1}
#%files xvid
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_pluginsdir}/xineplug_decode_xvid.so
#%endif
