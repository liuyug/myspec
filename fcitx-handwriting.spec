Name:		fcitx-handwriting
Version:20110908	
Release:	1%{?dist}
Summary:handwriting for fcitx	

Group:		System Environment/Libraries
License:GPL v2	
URL:	https://github.com/fcitx/fcitx-handwriting	

BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

Requires:fcitx zinnia zinnia-tomoe	

%description
handwriting for fcitx

%prep
rm -rf %{name}-%{version}
cp -r %{_sourcedir}/%{name} %{name}-%{version}
%setup -T -D


%build
cmake28 -DCMAKE_INSTALL_PREFIX=/usr
 
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


%changelog

