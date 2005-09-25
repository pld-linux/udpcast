Summary:	UDPcast is a file transfer tool
Name:		udpcast
Version:	20050226
Release:	0.1
License:	GPL v2 for main code, BSD-like for fec.c
Group:		Networking
# only working, recent url that i've found ;)
Source0:	http://gentoo.nedlinux.nl/distfiles/%{name}-%{version}.tar.gz
# Source0-md5:	8165440ba93e2b0ec8150926c3787dd1
URL:		http://udpcast.linux.lu/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
UDPcast is a file transfer tool that can send data simultaneously to
many destinations on a LAN. This can for instance be used to install
entire classrooms of PC's at once. The advantage of UDPcast over using
other methods (nfs, ftp, whatever) is that UDPcast uses Ethernet's
multicast abilities: it won't take longer to install 15 machines than
it would to install just 2.

%prep
%setup -q -n %{name}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man1/*
