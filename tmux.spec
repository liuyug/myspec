Name:tmux
Version:1.7
Release:	2%{?dist}
Summary:mux is a terminal multiplexer: it enables a number of terminals (or windows), each running a separate program, to be created, accessed, and controlled from a single screen. tmux may be detached from a screen and continue running in the background, then later reattached.

Group:System, Tools
License:BSD	
URL:tmux.sourceforge.net	
Source0:%{name}-%{version}.tar.gz	
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

#BuildRequires:	
#Requires:	

%description
tmux uses a client-server model. The server holds multiple sessions and each window is an independent entity which may be freely linked to multiple sessions, moved between sessions and otherwise manipulated. Each session may be attached to (display and accept keyboard input from) multiple clients.

tmux is intended to be a modern, BSD-licensed alternative to programs such as GNU screen. Major features include:

    A powerful, consistent, well-documented and easily scriptable command interface.
    A window may be split horizontally and vertically into panes.
    Panes can be freely moved and resized, or arranged into preset layouts.
    Support for UTF-8 and 256-colour terminals.
    Copy and paste with multiple buffers.
    Interactive menus to select windows, sessions or clients.
    Change the current window by searching for text in the target.
    Terminal locking, manually or after a timeout.
    A clean, easily extended, BSD-licensed codebase, under active development.


%prep
%setup -q


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
%{_bindir}
%{_mandir}


%changelog

