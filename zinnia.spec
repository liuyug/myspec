Name:	zinnia	
Version:0.6.0
Release:	1%{?dist}
Summary:	A hand recognition system 

Group:	System Environment/Libraries	
License:new BSD License	
URL:http://zinnia.sourceforge.net/		
Source0:%{name}-0.06.tar.gz	
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)


%description
Zinnia is a simple, customizable and portable online hand recognition system based on Support Vector Machines. Zinnia simply receives user pen strokes as a sequence of coordinate data and outputs n-best characters sorted by SVM confidence. To keep portability, Zinnia doesn't have any rendering functionality. In addition to recognition, Zinnia provides training module that allows us to create any hand-written recognition systems with low-cost.


%prep
%setup -n %{name}-0.06


%build
%configure --disable-static
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
%{_includedir}
%{_libdir}



%changelog

