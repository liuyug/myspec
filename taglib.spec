Name:		taglib
Version:1.8	
Release:	1%{?dist}
Summary:TagLib Audio Meta-Data Library	

Group:	System/Libraries	
License:LGPL MPL	
URL:	http://taglib.github.io/
Source0:%{name}-%{version}.tar.gz	
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

#BuildRequires:	
#Requires:	

%description
TagLib is a library for reading and editing the meta-data of several popular audio formats. Currently it supports both ID3v1 and ID3v2 for MP3 files, Ogg Vorbis comments and ID3 tags and Vorbis comments in FLAC, MPC, Speex, WavPack TrueAudio, WAV, AIFF, MP4 and ASF files.

%package devel
Requires: %{name} = %{version}-%{release}
Summary: taglib for devel

%description devel
TagLib is a library for reading and editing the meta-data of several popular audio formats. Currently it supports both ID3v1 and ID3v2 for MP3 files, Ogg Vorbis comments and ID3 tags and Vorbis comments in FLAC, MPC, Speex, WavPack TrueAudio, WAV, AIFF, MP4 and ASF files.


%prep
%setup -q


%build
arch=$(uname -m)
if [ "x$arch" == "xx86_64" ]; then
    lib_arch="64"
else
    lib_arch=""
fi
cmake -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_RELEASE_TYPE=Release -DLIB_SUFFIX=$lib_arch
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
%{_libdir}/libtag*

%files devel
%{_includedir}
%{_libdir}/pkgconfig


%changelog

