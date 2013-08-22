Name: audacious-plugins
Version: 3.2.4
Release: 1%{?dist}
Summary: Audacious is an open source audio player. This is a audacious plugins
Group: Sound
License: GPLv3
URL: http://audacious-media-player.org/
Source0: %{name}-%{version}.tar.bz2
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

#BuildRequires: audacious = 3.2.3
#Requires: audacious = 3.2.3

%description
Audacious is an open source audio player. A descendant of XMMS, Audacious plays your music how you want it, without stealing away your computer’s resources from other tasks. Drag and drop folders and individual song files, search for artists and albums in your entire music library, or create and edit your own custom playlists. Listen to CD’s or stream music from the Internet. Tweak the sound with the graphical equalizer or experiment with LADSPA effects. Enjoy the modern GTK-themed interface or change things up with Winamp classic skins. Use the plugins included with Audacious to fetch lyrics for your music, to set an alarm in the morning, and more.

%prep
%setup 
#%patch0 -p1

%build
%configure 
make %{?_smp_mflags}  

%install
#make DESTDIR=%{buildroot} install
%make_install install 

%files
%defattr(-,root,root,-)
#%doc ChangeLog INSTALLING README LICENSE AUTHORS VERSION
#%{_bindir}/*
#%{_sbindir}/*
#%{_mandir}/*
%{_datadir}/*
%{_libdir}/*
#%{_includedir}/*

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_DIR/%{name}-%{version}

%changelog

