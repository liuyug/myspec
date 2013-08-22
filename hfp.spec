%define svnbuild %(date +%Y%m%d)
Name:hfp
Version:%{svnbuild}
Release:	1%{?dist}
Summary:A Bluetooth Hands Free Profile implementation for Linux/bluez	

Group:Communications
License:GPL	
URL:http://sourceforge.net/projects/nohands/	
Source0:%{name}-%{version}.tar.gz	
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

#BuildRequires:	
#Requires:	

%description
HFP for Linux is a Bluetooth Hands-Free Profile server.

It allows your Linux system to act as a speakerphone for your mobile phone. It aims to be a compliant Bluetooth HFP 1.5 Hands Free implementation, supporting all required commands and notifications, as well as streaming audio.

HFP for Linux was designed specifically for automotive computing applications, but it can be used just as well in a desktop environment.

%prep
#%setup -q
svn co https://nohands.svn.sourceforge.net/svnroot/nohands/trunk %{name}-%{version}

%build
cd %{name}-%{version}
./autogen.sh
%configure
make %{?_smp_mflags}


%install
cd %{name}-%{version}
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc
%{_bindir}
%{_datadir}




%changelog

