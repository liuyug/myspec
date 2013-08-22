Name: goldendict
Version: 1.5.0_rc20130811
Release: 1%{?dist}
Summary: Feature-rich dictionary lookup program
Group: Education
License: GPLv3
URL: http://www.goldendict.org
Source0: %{name}-%{version}.tar.bz2
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

#BuildRequires: qt-devel
#Requires: qt-devel, hunspell

%description
GoldenDict is feature-rich dictionary lookup program. Features:
* Use of WebKit for an accurate articles' representation, complete with
  all formatting, colors, images and links.
* Support of multiple dictionary file formats, namely:
  - Babylon .BGL files, complete with images and resources
  - StarDict .ifo/.dict./.idx/.syn dictionaries
  - Dictd .index/.dict(.dz) dictionary files
  - ABBYY Lingvo .dsl source files, together with abbreviations. The
    files can be optionally compressed with dictzip. Dictionary
    resources can be packed together into a .zip file.
  - ABBYY Lingvo .lsa/.dat audio archives. Those can be indexed
    separately, or be referred to from .dsl files.
* Support for Wikipedia, Wiktionary, or any other MediaWiki-based sites
  to perform lookups in.
* Ability to use arbitrary websites as dictionaries via templated Url
  patterns.
* Support for looking up and listening to pronunciations from forvo.com
* Hunspell-based morphology system, used for word stemming and spelling
  suggestions.
* Ability to index arbitrary directories with audio files for
  pronunciation lookups.
* Full Unicode case, diacritics, punctuation and whitespace folding.
  This means the ability to type in words without any accents, correct
  case, punctuation or spaces.
* Scan popup functionality. A small window pops up with the translation
  of a word chosen from another application.
* Support for global hotkeys. You can spawn the program window at any
  point, or directly translate a word from the clipboard.
* Tabbed browsing in a modern Qt 4 interface.

%prep
rm -rf %{name}-%{version}
cp -r %{_sourcedir}/%{name} %{name}-%{version}
#setup -q
#patch0 -p1

%build
cd %{name}-%{version}
#configure
PREFIX=%{_prefix} /usr/bin/qmake-qt4 "DISABLE_INTERNAL_PLAYER=1" 
make %{?_smp_mflags}

%install
cd %{name}-%{version}
rm -rf %{buildroot}
make install INSTALL_ROOT=%{buildroot}

%files
%defattr(-,root,root,-)
%doc
%{_bindir}
%{_datadir}

%clean
rm -rf %{buildroot}

%changelog

