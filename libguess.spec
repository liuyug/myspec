#
# spec file for package libguess
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
# Copyright (c) 2011 Scorpio IT, Deidesheim, Germany
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           libguess
%define         libsoname          %{name}
Summary:        A high-speed character set detection library
License:        Other
Group:          System/Libraries
Version:        1.0
Release:        0
Url:            http://www.atheme.org/project/libguess
Source0:        %{name}-%{version}.tgz
#Source1:        baselibs.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  libmowgli-devel >= 0.7.0

%description
A high-speed character set detection library

libguess has two functions:

libguess_determine_encoding(const char *inbuf, int length, const char *region);
This detects a character set. Returns an appropriate charset name that can be
passed to iconv_open(). Region is the name of the language or region that the
data is related to, e.g. 'Baltic' for the Baltic states, or 'Japanese' for
Japan.

libguess_validate_utf8(const char *inbuf, int length);
This employs libguess's DFA-based character set validation rules to ensure that
a string is pure UTF-8. GLib's UTF-8 validation functions are broken, for
example.

Just include libguess.h and link to libguess to get these functions in your
program. For your convenience, a pkg-config file is also supplied.
libguess employs discrete-finite automata to deduce the character set of the
input buffer. The advantage of this is that all character sets can be checked
in parallel, and quickly. Right now, libguess passes a byte to each DFA on the
same pass, meaning that the winning character set can be deduced as efficiently
as possible.
libguess is fully reentrant, using only local stack memory for DFA operations.

#%package -n %{libsoname}
#Summary:        Shared library for libguess
#Group:          System/Libraries

#%description -n %{libsoname}
#A high-speed character set detection library

#This package contains the shared libguess library.

%package devel
Summary:        Development package for libguess
Group:          Development/Libraries/C and C++
Requires:       %{libsoname} = %{version}
Requires:       libmowgli-devel

%description devel
A high-speed character set detection library

This package contains the files needed to compile programs that use the
libguess library.

%prep
%setup -q

%build
%configure
%{__make} %{?_smp_mflags}

%install
%makeinstall

%post   -n %{libsoname} -p /sbin/ldconfig
%postun -n %{libsoname} -p /sbin/ldconfig

%files -n %{libsoname}
%defattr(-,root,root)
%{_libdir}/%{name}.so.*

%files devel
%defattr(-,root,root)
%doc COPYING README
%{_libdir}/%{name}.so
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/%{name}.h
%{_libdir}/pkgconfig/%{name}.pc

%changelog

