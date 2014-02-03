
Name: codeblocks
Version: %{?version}
Release: 1%{?dist}
Summary: CodeBlocks is a free C++ IDE built to meet the most demanding needs of its users. It is designed to be very extensible and fully configurable.
Group: Programming
License: GPLv3
URL: http://www.codeblocks.org/
Source0: %name-%version.tar.bz2
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: wxGTK-devel
Requires: wxGTK-devel

%description
Code::Blocks is a free C++ IDE built to meet the most demanding needs of its users. It is designed to be very extensible and fully configurable.
Finally, an IDE with all the features you need, having a consistent look, feel and operation across platforms.
Built around a plugin framework, Code::Blocks can be extended with plugins. Any kind of functionality can be added by installing/coding a plugin. For instance, compiling and debugging functionality is already provided by plugins!

%prep
cp -r %{_sourcedir}/codeblocks %{name}
%setup -D -T -n %{name}

%build
./bootstrap
%configure --with-contrib-plugins=all
make %{?_smp_mflags}

%install
#make DESTDIR=%{buildroot} install
%make_install install

%files
%defattr(-,root,root,-)
#%doc README TODO COPYING ChangeLog
%{_bindir}/*
#%{_sbindir}/*
#%{_mandir}/*
%{_datadir}/*
%{_libdir}/*
%{_includedir}/*

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_DIR/%{name}

%changelog

