Name:		webkitgtk
Version:1.3.4	
Release:	1%{?dist}
Summary:WebKitGTK+ is the GNOME platform port of the WebKit rendering engine	

Group:	System	
License:GPL	
URL:	http://www.webkitgtk.org/	
Source0:	webkit-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

#BuildRequires:	
#Requires:	

%description
WebKitGTK+ is the GNOME platform port of the WebKit rendering engine. Offering WebKit’s full functionality through a set of GObject-based APIs, it is suitable for projects requiring any kind of web integration, from hybrid HTML/CSS applications to full-fledged web browsers, like Epiphany and Midori. It’s useful in a wide range of systems from desktop computers to embedded systems like phones, tablets, and televisions. WebKitGTk+ is made by a lively community of developers and designers, who hope to bring the web platform to everyone.

%prep
%setup -q -n webkit-%{version}


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
%{_includedir}
%{_libdir}
%{_datadir}



%changelog

