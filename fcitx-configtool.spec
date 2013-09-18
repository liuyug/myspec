Name:		fcitx-configtool
Version:0.4.7	
Release:	1%{?dist}
Summary:config tool for fcitx	

Group:	System/Libraries
License:GPL v2
URL:	https://code.google.com/p/fcitx/  	
Source0:%{name}-%{version}.tar.xz	
Patch0:%{name}-%{version}.diff
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

#BuildRequires:	
Requires: fcitx

%description
config tool for fcitx

%prep
%setup -q
%patch0 -p1

%build
cmake   \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_BUILD_TYPE=Release  \
    -DENABLE_GTK2=On    \
    -DENABLE_GTK3=Off
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

