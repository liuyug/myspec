Name: osdlyrics
Version: 0.4.2
Release: 1%{?dist}
Summary: OSD Lyrics is a lyrics show compatible with various media players.
Group: Sound
License: GPLv3
URL: http://code.google.com/p/osd-lyrics
Source0: %{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

#BuildRequires:	
#Requires:	

%description
OSD Lyrics is a lyrics show compatible with various media players. It is not a plugin but a standalone program. OSD Lyrics shows lyrics on your desktop, in the style similar to KaraOK. It also provides another displaying style, in which lyrics scroll from bottom to top. OSD Lyrics can download lyrics from the network automatically.



%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc



%changelog

