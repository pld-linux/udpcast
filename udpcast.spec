Summary:	UDPcast is a multicast file transfer tool
Summary(pl.UTF-8):	UDPcast - przesyłanie plików przez multicast
Name:		udpcast
Version:	20081213
Release:	2
License:	GPL v2 for main code, BSD-like for fec.c
Group:		Networking
Source0:	http://udpcast.linux.lu/download/%{name}-%{version}.tar.gz
# Source0-md5:	23f3371cb60a1f66f6be12fa98d4d5ca
Patch0:		%{name}-Makefile.patch
URL:		http://udpcast.linux.lu/
BuildRequires:	autoconf >= 2.58
BuildRequires:	perl-tools-pod
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
UDPcast is a file transfer tool that can send data simultaneously to
many destinations on a LAN. This can for instance be used to install
entire classrooms of PC's at once. The advantage of UDPcast over using
other methods (NFS, FTP, whatever) is that UDPcast uses Ethernet's
multicast abilities: it won't take longer to install 15 machines than
it would to install just 2.

%description -l pl.UTF-8
UDPcast jest narzędziem do przesyłania danych jednocześnie do wielu
lokalizacji w sieci LAN, przykładowo do instalacji oprogramowania w
całej pracowni komputerowej za jednym razem. Przewagą UDPcast w
porównaniu do innych sposobów (NFS, FTP czy też innych) jest to, iż
wykorzystuje możliwość transmisji multicast - instalacja piętnastu
stacji roboczych nie powinna zająć więcej niż instalacja dwóch.

%package devel
Summary:	Header file for rateGovernor plugins
Summary(pl.UTF-8):	Plik nagłówkowy do tworzenia wtyczek rateGovernora
Group:		Development/Libraries
# doesn't require base

%description devel
Header file for rateGovernor plugins.

%description devel -l pl.UTF-8
Plik nagłówkowy do tworzenia wtyczek rateGovernora.

%prep
%setup -q
%patch0 -p1

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changelog.txt
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/udpcast
