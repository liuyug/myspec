Name:	xbmc	
Version:git_20130914	
Release:	1%{?dist}
Summary:	XBMC is an award-winning free and open source (GPL) software media player and entertainment hub 

Group:	Multimedia
License:GPL	
URL:	http://xbmc.org/
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	swig, glew-devel, mysql-devel, libass-devel, libmpeg2-devel, yajl-devel, tinyxml-devel, pcre-devel, taglib-devel, SDL_image-devel, libbluray-devel, libmicrohttpd-devel, libXt-devel, libssh-devel, libsmbclient-devel, librtmp-devel, gperf, libudev-devel
#Requires:	

%description
XBMC is an award-winning free and open source (GPL) software media player and entertainment hub that can be installed on Linux, OSX, Windows, iOS, and Android, featuring a 10-foot user interface for use with televisions and remote controls. It allows users to play and view most videos, music, podcasts, and other digital media files from local and network storage media and the internet.

%prep
rm -rf %{name}-%{version}
cp -r %{_sourcedir}/%{name} %{name}-%{version}
%setup -q -T -D


%build
./bootstrap
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
%{_libdir}
%{_includedir}
%{_datadir}



%changelog

