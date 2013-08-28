%define debug_package %{nil}
Name:	zinnia-tomoe
Version:0.6.0
Release:	1%{?dist}
Summary:zinnia model	

Group:	System Environment/Libraries	
License:new BSD License	
URL:http://zinnia.sourceforge.net/		
Source0:%{name}-%{version}-20080911.tar.bz2
BuildArch:noarch
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires:zinnia = %{version}-%{release}

%description
Zinnia is a simple, customizable and portable online hand recognition system based on Support Vector Machines. Zinnia simply receives user pen strokes as a sequence of coordinate data and outputs n-best characters sorted by SVM confidence. To keep portability, Zinnia doesn't have any rendering functionality. In addition to recognition, Zinnia provides training module that allows us to create any hand-written recognition systems with low-cost.


%prep
%setup -n %{name}-%{version}-20080911


%build
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
/usr/lib


%changelog

