Name:		smplayer
Version:	0.8.4
Release:	1%{?dist}
Summary:	SMPlayer is a graphical user interface (GUI) for the award-winning MPlayer

Group:		Applications/Multimedia
License:	GPL
URL:	    http://smplayer.sourceforge.net
Source0:	%{name}-%{version}.tar.bz2
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

#BuildRequires:	
#Requires:	

%description
SMPlayer is a free media player for Windows and Linux with built-in codecs that can play virtually all video and audio formats. It doesn't need any external codecs. Just install SMPlayer and you'll be able to play all formats without the hassle to find and install codec packs.

One of the most interesting features of SMPlayer: it remembers the settings of all files you play. So you start to watch a movie but you have to leave... don't worry, when you open that movie again it will be resumed at the same point you left it, and with the same settings: audio track, subtitles, volume...

SMPlayer is a graphical user interface (GUI) for the award-winning MPlayer, which is capable of playing almost all known video and audio formats. But apart from providing access for the most common and useful options of MPlayer, SMPlayer adds other interesting features like the possibility to play Youtube videos or download subtitles.

%prep
%setup -q


%build
make QMAKE=qmake-qt4 LRELEASE=lrelease-qt4 PREFIX=/usr %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install QMAKE=qmake-qt4 LRELEASE=lrelease-qt4 PREFIX=/usr DESTDIR=%{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc
%{_bindir}
%{_datadir}



%changelog

