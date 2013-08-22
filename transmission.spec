Name:		transmission
Version:2.13	
Release:	1%{?dist}
Summary:Tnsmission is a cross-platform BitTorrent client

Group:	Applications/Internet	
License:MIT	
URL:	http://www.transmissionbt.com/	
Source0:%{name}-%{version}.tar.xz	
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

#BuildRequires:	
#Requires:	

%description
Transmission is a cross-platform BitTorrent client

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



%changelog

