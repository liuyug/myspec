Name:		ffmpeg
Version:	0.8.15
Release:	1%{?dist}
Summary:FFmpeg is a complete, cross-platform solution to record, convert and stream audio and video	

Group:	System Environment/Libraries	
License:GPLv2	
URL:	http://www.ffmpeg.org
Source0:%{name}-%{version}.tar.bz2
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:libvpx >= 0.9.6 libx264 >= 0.115
#Requires:	

%description
FFmpeg is the leading multimedia framework, able to decode, encode, transcode, mux, demux, stream, filter and play pretty much anything that humans and machines have created. It supports the most obscure ancient formats up to the cutting edge. No matter if they were designed by some standards committee, the community or a corporation. It contains libavcodec, libavutil, libavformat, libavfilter, libavdevice, libswscale and libswresample which can be used by applications. As well as ffmpeg, ffserver, ffplay and ffprobe which can be used by end users for transcoding, streaming and playing 

%package devel
Requires: %{name} = %{version}-%{release}
Summary: ffmpeg for devel

%description devel
FFmpeg is the leading multimedia framework, able to decode, encode, transcode, mux, demux, stream, filter and play pretty much anything that humans and machines have created. It supports the most obscure ancient formats up to the cutting edge. No matter if they were designed by some standards committee, the community or a corporation. It contains libavcodec, libavutil, libavformat, libavfilter, libavdevice, libswscale and libswresample which can be used by applications. As well as ffmpeg, ffserver, ffplay and ffprobe which can be used by end users for transcoding, streaming and playing 


%prep
%setup -q


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
        --shlibdir=/usr/lib$lib_arch \
        --disable-static \
        --enable-shared \
        --enable-gpl \
        --enable-version3 \
        --enable-nonfree \
        --enable-postproc \
        --enable-swscale \
        --enable-avfilter \
        --enable-pthreads \
        --enable-x11grab \
        --disable-debug \
        --enable-runtime-cpudetect \
        --arch=x86_64 \
        --enable-libxvid \
        --enable-libx264 \
        --enable-vdpau \
        --enable-libvorbis \
        --enable-libtheora \
        --enable-libspeex \
        --enable-libopenjpeg \
        --enable-libmp3lame \
        --enable-libfaac \
        --enable-libvpx \
        --enable-librtmp


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
%{_libdir}/vhook
%{_datadir}

%files devel
%{_includedir}
%{_libdir}/pkgconfig

%changelog

