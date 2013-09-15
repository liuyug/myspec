%define debug_package %{nil}
Name:		tesseract-chi_sim
Version:	3.02
Release:	1%{?dist}
Summary:Tesseract OCR data for english	

Group:	System/Libraries	
License:	Apache 2.0
URL:	https://code.google.com/p/tesseract-ocr/
Source0:tesseract-ocr-%{version}.chi_sim.tar.gz	
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

#BuildRequires:	
Requires:	tesseract = %{version}-%{release}
BuildArch: noarch

%description
Tesseract is probably the most accurate open source OCR engine available. Combined with the Leptonica Image Processing Library it can read a wide variety of image formats and convert them to text in over 60 languages. It was one of the top 3 engines in the 1995 UNLV Accuracy test. Between 1995 and 2006 it had little work done on it, but since then it has been improved extensively by Google.


%prep
%setup -q -n tesseract-ocr


%build
exit 0

%install
rm -rf %{buildroot}
install -d %{buildroot}/usr/share/tessdata
install tessdata/*  %{buildroot}/usr/share/tessdata/


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc
%{_datadir}


%changelog

