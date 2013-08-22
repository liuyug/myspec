Name: aMule		
Version: 2.3.1
Release:	1%{?dist}
Summary:	aMule is an eMule-like client for the eD2k and Kademlia networks, supporting multiple platforms. 

Group:		Internet
License:GPL	
URL:	http://www.amule.org/	
Source0:%{name}-%{version}.tar.bz2
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

#BuildRequires:	
#Requires:	

%description
aMule stands for all-platform Mule.

aMule is an eMule-like client for the eD2k and Kademlia networks, supporting multiple platforms.

Currently aMule (officially) supports a wide variety of platforms and operating systems, being compatible with more than 60 different hardware+OS configurations.

aMule is entirely free, its sourcecode released under the GPL just like eMule, and includes no adware or spyware as is often found in proprietary P2P applications.

aMule is built upon the wxWidgets (formerly wxWindows) toolkit, which enables it to support multiple platforms. 

%prep
%setup -q


%build
%configure --disable-debug --enable-optimize --enable-amule-daemon --enable-amulecmd --enable-webserver --enable-amule-gui --enable-alc --enable-alcc
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc
%{_bindir}/*
%{_datadir}/*


%changelog

