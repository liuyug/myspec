Name:		privoxy
Version:3.0.21
Release:	1%{?dist}
Summary:Privoxy is a non-caching web proxy

Group:	Applications/Internet
License:GPLv2
URL:http://www.privoxy.org/
Source0:%{name}-%{version}-stable-src.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

#BuildRequires:	
#Requires:	

%description
Privoxy is a non-caching web proxy with advanced filtering capabilities for
enhancing privacy, modifying web page data and HTTP headers, controlling
access, and removing ads and other obnoxious Internet junk. Privoxy has a
flexible configuration and can be customized to suit individual needs and
tastes. It has application for both stand-alone systems and multi-user
networks.


%prep
%setup -q -n %{name}-%{version}-stable


%build
autoheader
autoconf
%configure --disable-toggle  --disable-editor  --disable-force
make %{?_smp_mflags}

%pre
if grep ^privoxy: /etc/group >> /dev/null ; then
 : # group already exists
else
 groupadd privoxy -g 7777
fi

if ! id privoxy >& /dev/null; then 
 adduser privoxy -g privoxy -u 7777 -s /sbin/nologin
fi

%postun
userdel privoxy
groupdel privoxy

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_sysconfdir}
%{_sbindir}
%{_docdir}
%{_mandir}
%{_var}/log/privoxy



%changelog

