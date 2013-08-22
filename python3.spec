
Name: python3
Version: 3.3.2
Release: 2%{?dist}
Summary: An interpreted, interactive, object-oriented programming language.
Group: Programming
License: PSF
URL: http://www.python.org/
Source0: Python-%{version}.tar.bz2
Patch0 : python3.readline.set_pre_input_hook.diff
Patch1 : python3.no-static-library.diff
Patch2 : python3.x86_64.diff

BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

AutoReq : 0
#BuildRequires: 
#Requires: 

%description
Python is an interpreted, interactive, object-oriented programming
language.  It incorporates modules, exceptions, dynamic typing, very high
level dynamic data types, and classes. Python combines remarkable power
with very clear syntax. It has interfaces to many system calls and
libraries, as well as to various window systems, and is extensible in C or
C++. It is also usable as an extension language for applications that need
a programmable interface.  Finally, Python is portable: it runs on many
brands of UNIX, on PCs under Windows, MS-DOS, and OS/2, and on the
Mac.


%prep
%setup -n Python-%{version}
%patch0 -p1 
#%patch1 -p1 
if [ %{_arch} == 'x86_64' ] ; then 
%patch2 -p1
fi
sed -i '1s|^#.*/usr/local/bin/python|#!/usr/bin/python3|' Lib/cgi.py

%build
%configure \
    --with-threads \
    --enable-ipv6 \
    --enable-shared \
    --with-system-expat \
    --with-system-ffi \


make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make altinstall DESTDIR=%{buildroot} 
# Create a few useful symlinks.
( cd %{buildroot}/usr/bin
  ln -sf python3.3 python3
  ln -sf python3.3*-config python3.3-config
  ln -sf pydoc3.3 pydoc3
  ln -sf pyvenv-3.3 pyvenv
  ln -sf idle3.3 idle3
)

%files
%defattr(-,root,root,-)
#%doc README TODO COPYING ChangeLog
%{_bindir}/*
#%{_sbindir}/*
#%{_mandir}/*
%{_datadir}/*
%{_libdir}/*
%{_includedir}/*

%clean
rm -rf %{buildroot}

%changelog

