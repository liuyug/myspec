Name: aircrack-ng
Version: %{?version}
Release: 1%{?dist}
Summary: Aircrack-ng is an 802.11 WEP and WPA-PSK keys cracking program
Group: Internet
License: GPLv3
URL: http://www.aircrack-ng.org/
Source0: %{name}-%{version}.tar.bz2
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: openssl sqlite >= 3.3
Requires: openssl sqlite >= 3.3

%description
Aircrack-ng is an 802.11 WEP and WPA-PSK keys cracking program that can recover keys once enough data packets have been captured. It implements the standard FMS attack along with some optimizations like KoreK attacks, as well as the all-new PTW attack, thus making the attack much faster compared to other WEP cracking tools.

%prep
%setup -n %{name}
#%patch0 -p1

%build
# no need configure
make %{?_smp_mflags}  sqlite=true

%install
#make DESTDIR=%{buildroot} install
%make_install install prefix=%{_prefix} sqlite=true

%files
%defattr(-,root,root,-)
%doc ChangeLog INSTALLING README LICENSE AUTHORS VERSION
%{_bindir}/*
%{_sbindir}/*
%{_mandir}/*
#%{_datadir}/*
#%{_libdir}/*
#%{_includedir}/*

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_DIR/%{name}

%changelog

