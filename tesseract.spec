%define debug_package %{nil}
Name:	tesseract
Version:	3.02
Release:	1%{?dist}
Summary:Tesseract is the accurate open source OCR engine	

Group:	Application/System	
License:Apache 2.0	
URL:	https://code.google.com/p/tesseract-ocr/	
Source0:%{name}-ocr-%{version}.02.tar.gz	
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:leptonica	
#Requires:	

%description
Tesseract is probably the most accurate open source OCR engine available. Combined with the Leptonica Image Processing Library it can read a wide variety of image formats and convert them to text in over 60 languages. It was one of the top 3 engines in the 1995 UNLV Accuracy test. Between 1995 and 2006 it had little work done on it, but since then it has been improved extensively by Google.

%prep
%setup -q -n %{name}-ocr


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
%{_libdir}
%{_datadir}
%{_includedir}

%changelog

