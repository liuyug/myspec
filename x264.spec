Name:		x264
Version:    20131101
Release:	1%{?dist}
Summary:	Encode video streams into the H.264/MPEG-4 AVC compression format.

Group:		System Environment/Libraries
License:	GPLv2
URL:	http://www.videolan.org/developers/x264.html	
Source0:	%{name}-snapshot-%{version}-2245-stable.tar.bz2
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

#BuildRequires:	
#Requires:	

%description
x264 is a free software library and application for encoding video streams into the H.264/MPEG-4 AVC compression format

%package devel
Requires: %{name} = %{version}-%{release}
Summary: x264 for devel

%description devel
x264 is a free software library and application for encoding video streams into the H.264/MPEG-4 AVC compression format

%prep
%setup -q -n %{name}-snapshot-%{version}-2245-stable


%build
arch=$(uname -m)
if [ "x$arch" == "xx86_64" ]; then
    lib_arch="64"
else
    lib_arch=""
fi

./configure \
    --prefix=/usr \
    --libdir=/usr/lib$lib_arch \
    --enable-shared \
    --enable-strip \
    --enable-pic


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
%{_libdir}/lib*

%files devel
%{_includedir}
%{_libdir}/pkgconfig

%changelog

