Name:		MPlayer
Version:1.1.1
Release:	1%{?dist}
Summary:MPlayer is a movie player which runs on many systems

Group:	Multimedia	
License:GPL	
URL:http://www.mplayerhq.hu		
Source0:%{name}-%{version}.tar.xz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

#BuildRequires:	
#Requires:

%description
MPlayer is a movie player which runs on many systems (see the documentation). It plays most MPEG/VOB, AVI, Ogg/OGM, VIVO, ASF/WMA/WMV, QT/MOV/MP4, RealMedia, Matroska, NUT, NuppelVideo, FLI, YUV4MPEG, FILM, RoQ, PVA files, supported by many native, XAnim, and Win32 DLL codecs. You can watch VideoCD, SVCD, DVD, 3ivx, DivX 3/4/5, WMV and even H.264 movies.

Another great feature of MPlayer is the wide range of supported output drivers. It works with X11, Xv, DGA, OpenGL, SVGAlib, fbdev, AAlib, DirectFB, but you can use GGI, SDL (and this way all their drivers), VESA (on every VESA compatible card, even without X11!) and some low level card-specific drivers (for Matrox, 3Dfx and ATI), too! Most of them support software or hardware scaling, so you can enjoy movies in fullscreen. MPlayer supports displaying through some hardware MPEG decoder boards, such as the Siemens DVB, DXR2 and DXR3/Hollywood+.

MPlayer has an onscreen display (OSD) for status information, nice big antialiased shaded subtitles and visual feedback for keyboard controls. European/ISO 8859-1,2 (Hungarian, English, Czech, etc), Cyrillic and Korean fonts are supported along with 12 subtitle formats (MicroDVD, SubRip, OGM, SubViewer, Sami, VPlayer, RT, SSA, AQTitle, JACOsub, PJS and our own: MPsub). DVD subtitles (SPU streams, VOBsub and Closed Captions) are supported as well.

%prep
#%setup -n mplayer-export-2013-09-03
%setup -q


%build
./configure \
    --prefix=/usr \
    --bindir=/usr/bin \
    --datadir=/usr/share \
    --mandir=/usr/share/man \
    --confdir=/etc/mplayer \
    --libdir=/usr/lib64
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc
%{_bindir}
%{_mandir}



%changelog

