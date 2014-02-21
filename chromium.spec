# failed to compile
Name:		chromium
Version:	31.0.1650.57
Release:	1%{?dist}
Summary:	A browser from google. A developing version of chrome.

Group:		Applications/Internet
License:	google
URL:		http://www.chromium.org/
Source0:	%{name}-%{version}.tar.xz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires: pciutils-devel
Requires:	pciutils

%description
Google Chromium is a browser that combines a minimal design with sophisticated technology to make the web faster, safer, and easier.

%prep
%setup -q


%build
# Google API keys (see http://www.chromium.org/developers/how-tos/api-keys)
# Here we following the same way of Arch Linux and Gentoo.
# Note: These are for this build use ONLY. For your own distribution, please
# get your own set of keys. Feel free to contact me for more information.
GOOGLE_API_KEY=AIzaSyBhWJ-j5RXyt5911BMuVen-WuS10mvOnrY
GOOGLE_DEFAULT_CLIENT_ID=952820686433-mbp5sv9scfj78siq96jlvrem47qgvbi3.apps.googleusercontent.com
GOOGLE_DEFAULT_CLIENT_SECRET=XU4b-j0Ssy-XkTvSVmiFMvNY

arch=$(uname -m)
if [ "x$arch" == "xx86_64" ]; then
    lib_arch="64"
else
    lib_arch=""
fi

build/gyp_chromium -f make build/all.gyp --depth=. \
 -Dgoogle_api_key=$GOOGLE_API_KEY \
 -Dgoogle_default_client_id=$GOOGLE_DEFAULT_CLIENT_ID \
 -Dgoogle_default_client_secret=$GOOGLE_DEFAULT_CLIENT_SECRET \
 -Dwerror= \
 -Dsystem_libdir=lib${lib_arch} \
 -Dlinux_link_gnome_keyring=0 \
 -Dlinux_sandbox_path=/usr/lib${lib_arch}/chromium/chrome-sandbox \
 -Dlinux_strip_binary=1 \
 -Dlinux_use_gold_binary=0 \
 -Dlinux_use_gold_flags=0 \
 -Dffmpeg_branding=Chrome \
 -Dno_strict_aliasing=1 \
 -Dproprietary_codecs=1 \
 -Duse_gconf=0 \
 -Duse_gnome_keyring=0 \
 -Duse_kerberos=0 \
 -Duse_pulseaudio=0 \
 -Duse_system_bzip2=1 \
 -Duse_system_ffmpeg=0 \
 -Duse_system_libevent=1 \
 -Duse_system_libpng=1 \
 -Duse_system_libjpeg=1 \
 -Duse_system_libxslt=1 \
 -Duse_system_libxml=1 \
 -Duse_system_ssl=0 \
 -Duse_system_zlib=1 \
 -Duse_system_yasm=1 \
 -Ddisable_nacl=1 \
 -Drelease_extra_cflags="-Wno-unused-local-typedefs" \
 -Ddisable_sse2=1


make %{?_smp_mflags} chrome chrome_sandbox BUILDTYPE=Release V=1

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

