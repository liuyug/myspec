%define debug_package %{nil}
Name:		leptonica
Version:	1.69
Release:	1%{?dist}
Summary:	Leptonica is image processing and image analysis 

Group:	System/Libraries	
License:	GPL
URL:	http://leptonica.org/
Source0:%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

#BuildRequires:	
#Requires:	

%description
Leptonica is a pedagogically-oriented open source site containing software that is broadly useful for image processing and image analysis applications.

%prep
%setup -q


%build
%configure --disable-static --bindir=%{_libexecdir}/%{name}/
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc
%{_includedir}
%{_libdir}
%{_libexecdir}/%{name}


%changelog

