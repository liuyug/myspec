Name:	dropbox
Version:1.4.0	
Release:	1%{?dist}
Summary: Dropbox daemon

Group:	Internet	
License:GPL	
URL:https://www.dropbox.com/		
Source0:nautilus-%{name}-%{version}.tar.bz2
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

#BuildRequires:
#Requires:	

%description
The Dropbox daemon works fine on all 32-bit and 64-bit Linux servers.
If you're running Dropbox on your server for the first time, you'll be asked to copy and paste a link in a working browser to create a new account or add your server to an existing account. Once you do, your Dropbox folder will be created in your home directory. Download this CLI script to control Dropbox from the command line. For easy access, put a symlink to the script anywhere in your PATH.
~/.dropbox-dist/dropboxd

%prep
# manual unzip and configure
#%setup -n nautilus-%{name}-%{version}


%build
# rpmbuild don't set DISPLAY,
#% configure 
#make %{?_smp_mflags}


%install
#rm -rf %{buildroot}
cd nautilus-%{name}-%{version}
make install DESTDIR=%{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc
%{_bindir}/*
%{_libdir}/*
%{_datadir}/*



%changelog

