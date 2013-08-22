Name: libev
Version:4.11
Release:	1%{?dist}
Summary:A full-featured and high-performance event loop
Group:Libraries	
License:3-clause BSD
URL:http://software.schmorp.de/pkg/libev
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

#BuildRequires:	
#Requires:	

%description
A full-featured and high-performance (see benchmark) event loop that is loosely modelled after libevent, but without its limitations and bugs. It is used in GNU Virtual Private Ethernet, rxvt-unicode, auditd, the Deliantra MORPG Server and Client, and many other programs.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}/usr/include/libev
mv %{buildroot}/usr/include/*.h %{buildroot}/usr/include/libev/

%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc
#%{_bindir}
%{_includedir}
%{_libdir}
%{_mandir}


%changelog

