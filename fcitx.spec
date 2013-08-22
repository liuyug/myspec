Name:		fcitx
Version:	4.2.6.1
Release:	1%{?dist}
Summary:	Fcitx is an input method framework with extension support.
Group:		System Environment/Libraries
License:	GNU GPL v2
URL:	https://code.google.com/p/fcitx/	
Source0:%{name}-%{version}_dict.tar.xz	
Patch0:%{name}-%{version}_dict.diff
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

Requires: %{name}-libs = %{version}-%{release}
Requires: %{name}-gtk2 = %{version}-%{release}

%description
Fcitx [ˈfaɪtɪks] is an input method framework with extension support. Currently it supports linux and Unix system, like freebsd. It has three builtin Input Method Engine, Pinyin, QuWei and Table-based input methods. 

%package libs
Summary:	Fcitx is an input method framework with extension support.

%description libs
Fcitx libs 

%package qt4
Summary:	Fcitx is an input method framework with extension support.
Requires: %{name}-libs = %{version}-%{release}

%description qt4
Fcitx for qt4

%package gtk2
Summary:	Fcitx is an input method framework with extension support.
Requires: %{name}-libs = %{version}-%{release}

%description gtk2
Fcitx for gtk-2.0

%package devel
Summary:	Fcitx is an input method framework with extension support.
Requires: %{name}-libs = %{version}-%{release}

%description devel
Fcitx for development


%prep
%setup -q 
%patch0 -p1


%build
if [ %{_target_cpu} = 'x86_64' ] ; then
    rpm_flags="-m64"
else
    rpm_flags="-m32"
fi

 
cmake28 -DCMAKE_INSTALL_PREFIX=/usr \
    -DLIB_INSTALL_DIR=%{_libdir}    \
    -DENABLE_GTK2_IM_MODULE=On      \
    -DENABLE_QT_IM_MODULE=On        \
    -DENABLE_XDGAUTOSTART=Off       \
    -DCMAKE_C_FLAGS=$rpm_flags      \
    -DCMAKE_CXX_FLAGS=$rpm_flags    \
    -DCMAKE_SHARED_LINKER_FLAGS="-s"    \
    -DCMAKE_MODULE_LINKER_FLAGS="-s"
    
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}/etc/X11/xinit/xinput.d
cat <<EOF > %{buildroot}/etc/X11/xinit/xinput.d/fcitx.conf
XIM=fcitx
XIM_PROGRAM=/usr/bin/fcitx
ICON="fcitx"
XIM_ARGS="-r -D"
SHORT_DESC="Fcitx"
PREFERENCE_PROGRAM=/usr/bin/fcitx-configtool

XMODIFIERS=@im=fcitx
GTK_IM_MODULE=fcitx
if [ -f /usr/lib64/qt4/plugins/inputmethods/libqtim-fcitx.so ] ||\
       [ -f /usr/lib/qt4/plugins/inputmethods/libqtim-fcitx.so ] ; then
    QT_IM_MODULE=fcitx
fi
EOF

if [ %{_target_cpu} = 'i686' ] ; then
    mv $RPM_BUILD_ROOT/usr/lib64/qt4 $RPM_BUILD_ROOT/usr/lib/qt4
    rmdir $RPM_BUILD_ROOT/usr/lib64
fi

%post gtk2
update-gtk-immodules %{_target_platform}

%postun gtk2
update-gtk-immodules %{_target_platform}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc
%{_sysconfdir}
%{_bindir}
%{_datadir}

%files libs
%{_libdir}/fcitx
%{_libdir}/libfcitx-config.so
%{_libdir}/libfcitx-config.so.4
%{_libdir}/libfcitx-config.so.4.1
%{_libdir}/libfcitx-core.so
%{_libdir}/libfcitx-core.so.0
%{_libdir}/libfcitx-core.so.0.3
%{_libdir}/libfcitx-utils.so
%{_libdir}/libfcitx-utils.so.0
%{_libdir}/libfcitx-utils.so.0.1

%files qt4
%{_libdir}/qt4

%files gtk2
%{_libdir}/gtk-2.0

%files devel 
%{_includedir}
%{_libdir}/pkgconfig

%changelog

