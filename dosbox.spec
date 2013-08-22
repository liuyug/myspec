Name:dosbox
Version:0.74
Release:1%{?dist}
Summary:Free Open Source DOS emulator to run old DOS games 
Group:Games
License:GPLv2
URL:http://www.dosbox.com/
Source0:%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

#BuildRequires:	
#Requires:	

%description
DOSBox emulates a full x86 pc with sound and DOS. Its main use is to run old DOS games on platforms which don't have DOS (Windows 7 / Windows Vista / Windows 2000 / Windows XP / Linux / FreeBSD / Mac OS X)

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

