Name:mercurial
Version:1.8.4	
Release:	1%{?dist}
Summary:A fast, lightweight distributed source control management system	
Group:		Development
License:GNU GPLv2	
URL:	http://mercurial.selenic.com/wiki/Mercurial	
Source0:%{name}-%{version}.tar.gz  
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

#BuildRequires:	
#Requires:	

%description
A fast, lightweight distributed source control management system	

%prep
%setup -q


%build


%install
rm -rf %{buildroot}
make install PREFIX=/usr DESTDIR=%{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc
%{_bindir}
%{_libdir}
%{_datadir}



%changelog

