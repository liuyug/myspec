Name:		Sigil
Version:	823d60cf94bfeba5b7f1c0ab99e72fc0b37db2c2
Release:	1%{?dist}
Summary:Sigil is a free, open source, multi-platform ebook editor.

Group:		Applications/Editors
License:	GPLv3
URL:	http://code.google.com/p/sigil	
Source0:%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%description
Sigil is a free, open source, multi-platform ebook editor.
It is designed to edit books in ePub format.
This is the maximum version requiring Qt4.6


%prep
%setup -q


%build
arch=$(uname -m)
if [ "x$arch" == "xx86_64" ]; then
    lib_arch="64"
else
    lib_arch=""
fi

cmake ./ -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_RELEASE_TYPE=Release -DLIB_SUFFIX=$lib_arch
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



%changelog

