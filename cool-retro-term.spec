%define		gitver	08ade0eb6f36379a62a5b68f965e70fe55aa7199

Summary:	Terminal emulator with an old school look and feel
Name:		cool-retro-term
Version:	0.9
Release:	0.%{gitver}.1
License:	GPL v.3
Group:		Applications/System
Source0:	https://github.com/Swordfish90/cool-retro-term/archive/master.zip
# Source0-md5:	03cd98bd9af31e1f807507861b020a0d
URL:		https://github.com/Swordfish90/cool-retro-term
BuildRequires:	qt5-base-devel
BuildRequires:	qt5-declarative-devel
Requires:	qt5-base
Requires:	qt5-declarative
Requires:	qt5-graphicaleffects
Requires:	qt5-quickcontrols
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cool-retro-term is a terminal emulator which mimics the look and feel
of the old cathode tube screens. It has been designed to be eye-candy,
customizable, and reasonably lightweight.

%prep
%setup -qn %{name}-master

%{__sed} -i 's|Utility;||' cool-retro-term.desktop

%build
qmake
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -j1 install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/cool-retro-term
%dir %{_libdir}/qt5/qml/org
%dir %{_libdir}/qt5/qml/org/crt
%dir %{_libdir}/qt5/qml/org/crt/konsole
%attr(755,root,root) %{_libdir}/qt5/qml/org/crt/konsole/libkdekonsole.so
%{_libdir}/qt5/qml/org/crt/konsole/color-schemes
%{_libdir}/qt5/qml/org/crt/konsole/kb-layouts
%{_libdir}/qt5/qml/org/crt/konsole/plugins.qmltypes
%{_libdir}/qt5/qml/org/crt/konsole/qmldir
%{_desktopdir}/cool-retro-term.desktop

