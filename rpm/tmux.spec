Summary: tmux is a terminal multiplexer
Name: tmux
Version: 1.8
Release: 1
License: BSD
Group: Applications/System
URL: http://tmux.sourceforge.net/
Source0: %{name}-%{version}.tar.bz2
BuildRequires: pkgconfig(ncurses)
BuildRequires: libevent-devel
Requires: libevent

%description
tmux is a "terminal multiplexer", it enables a number of terminals (or windows)
to be accessed and controlled from a single terminal. tmux is intended to be a
simple, modern, BSD-licensed alternative to programs such as GNU screen.

%prep
%setup -q

%build
%{reconfigure}
%{__make} %{?jobs:-j%jobs}

%install
rm -rf $RPM_BUILD_ROOT
%{make_install}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)

%{_bindir}
%{_bindir}/tmux
%{_mandir}/man1/tmux.1.gz
%doc README
