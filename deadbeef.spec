Name:		deadbeef
Version:	0.5.6
Release:	1%{?dist}
Summary:DeaDBeeF - Ultimate Music Player For GNU/Linux	
Group:		MultiMedia
License:GPLv2	
URL:	http://deadbeef.sourceforge.net	
Source0:%{name}-%{version}.tar.bz2	
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

#BuildRequires:	
#Requires:	

%description
DeaDBeeF (as in 0xDEADBEEF) is an audio player for GNU/Linux, *BSD, OpenSolaris and other UNIX-like systems. There's also the Android version, which is a very different product. There are no Windows, OSX or iOS versions though, sorry for that.

%prep
%setup -q


%build
%configure
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
%{_datadir}
%{_libdir}
%{_includedir}



%changelog

