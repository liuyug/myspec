Name:		poedit
Version:	1.5.7
Release:	1%{?dist}
Summary:	Poedit is cross-platform gettext catalogs (.po files) editor.

Group:	Development	
License:MIT	
URL:	http://www.poedit.net/	
Source0:%{name}-%{version}.tar.gz	
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

#BuildRequires:
#Requires:	

%description
Poedit is cross-platform gettext catalogs (.po files) editor. It is built with wxWidgets toolkit and can run on any platform supported by it (although it was only tested on Unix with GTK+ and Windows). It aims to provide more convenient approach to editing catalogs than launching vi and editing the file by hand. 

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

