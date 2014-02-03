Name:		minidlna
Version:	1.1.1
Release:	1%{?dist}
Summary:	The MiniDLNA daemon is an UPnP-A/V and DLNA service.

Group:	Applications/Multimedia	
License:BSD	
URL:	http://sourceforge.net/projects/minidlna/
Source0:%{name}-%{version}.tar.gz	
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:libexif libjpeg libid3tag flac libvorbis sqlite ffmpeg	

%description
The MiniDLNA daemon is an UPnP-A/V and DLNA service.

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}%{_sysconfdir}
cp %{name}.conf %{buildroot}%{_sysconfdir}
mkdir -p %{buildroot}%{_mandir}/man5
cp %{name}.conf.5 %{buildroot}%{_mandir}/man5
gzip %{buildroot}%{_mandir}/man5/%{name}.conf.5
mkdir -p %{buildroot}%{_mandir}/man8
cp %{name}d.8 %{buildroot}%{_mandir}/man8
gzip %{buildroot}%{_mandir}/man8/%{name}d.8


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc
%{_sbindir}
%{_datadir}
%{_sysconfdir}



%changelog

