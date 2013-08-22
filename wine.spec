Name:wine	
Version:1.5.21
Release:	1%{?dist}
Summary:Wine is a compatibility layer capable of running Windows applications on several POSIX-compliant operating systems.

Group:System
License:free software
URL:http://www.winehq.org/	
Source0:%{name}-%{version}.tar.bz2	
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

#BuildRequires:	
#Requires:	

%description
Wine (originally an acronym for "Wine Is Not an Emulator") is a compatibility layer capable of running Windows applications on several POSIX-compliant operating systems, such as Linux, Mac OSX, & BSD. Instead of simulating internal Windows logic like a virtual machine or emulator, Wine translates Windows API calls into POSIX calls on-the-fly, eliminating the performance and memory penalties of other methods and allowing you to cleanly integrate Windows applications into your desktop.

Wine will always be free software. Approximately half of Wine's source code is written by volunteers, with the remaining effort sponsored by commercial interests, especially CodeWeavers, which sells a supported version of Wine.

%prep
%setup -q


%build
%configure --enable-win64
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
%{_datadir}

%changelog

