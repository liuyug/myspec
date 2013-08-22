
Name: wxcam
Version: 1.1
Release: 1%{?dist}
Summary: wxCam is a webcam application for linux
Group: Sound & Video
License: GPLv3
URL: http://wxcam.sourceforge.net/
Source0: %name-%version.tar.bz2
Source1: CImg-1.4.9.zip
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: wxGTK-devel
Requires: wxGTK xvidcore alsa-lib mjpegtools

%description
wxCam is a webcam application for linux. It supports video recording (in an avi uncompressed and Xvid format), snapshot taking, and some special commands for philips webcams, so you can also use the program for astronomy purposes. It supports both video4linux 1 and 2 drivers, so it should work on a very large number of devices. 

wxCam features:
-) Frame grabbing using video4linux 1 and 2 api;
-) Adjust resolution, brightness, contrast, gamma and saturation;
-) Support for some special controls for philips webcam: frame rate, gain and shutter speed;
-) Snapshot taking in various formats, including BMP, PNG, JPEG, TIF, PCX, XPM.
-) There are graphics effects such color correction, negative, edge, monochrome, upturned, laplacian, and mirror.
-) Video recording without audio in an avi uncompressed format: e.g., useful for astronomy purpose (lunar and planetary video recording) because it is totally lossless.
-) Video recording with audio, in the Xvid format: it is a lossy video format, but with great hard disk space saving.
-) Video recording on movement detection. 

%prep
%setup 
%__unzip %SOURCE1
#%patch0 -p1

%build
%configure CXXFLAGS="-DHAVE_CAMV4L -I%{_builddir}/%{name}-%{version}/CImg-1.4.9  -g -O2"
make %{?_smp_mflags}

%install
#make DESTDIR=%{buildroot} install
%make_install install
%find_lang %{name}

%files -f  %{name}.lang
%defattr(-,root,root,-)
%doc README COPYING ChangeLog INSTALL NEWS AUTHORS
%{_bindir}/*
#%{_sbindir}/*
#%{_mandir}/*
%exclude %{_exec_prefix}/doc/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
#%{_libdir}/*
#%{_includedir}/*

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_DIR/%{name}-%{version}

%changelog

