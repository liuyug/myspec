Name:		qregexp-editor
Version:0.2.1	
Release:	1%{?dist}
Summary:test regular expression	in Qt

Group:	Development/Tools	
License:	GPLv3
URL:	https://sourceforge.net/projects/qregexp-editor	
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)


%description
QRegExp-Editor is a simple multi-platform application that allows you to easily test your regular expressions as used in Qt's QRegExp module. It runs on Windows, MacOSX and Linux. It shows you the captured strings and their respective substrings.



%prep
%setup -q


%build
cmake -DCMAKE_INSTALL_PREFIX=/usr ./
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
%{_datadir}



%changelog

