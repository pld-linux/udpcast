Summary:	UDPcast is a multicast file transfer tool
Summary(pl):	UDPcast - przesy�anie plik�w przez multicast
Name:		udpcast
Version:	20070205
Release:	1
License:	GPL v2 for main code, BSD-like for fec.c
Group:		Networking
Source0:	http://udpcast.linux.lu/download/%{name}-%{version}.tar.gz
# Source0-md5:	6a4d6d973bdf4dca28975aa447180dbf
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-Makefile.patch
URL:		http://udpcast.linux.lu/
BuildRequires:	perl-tools-pod
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
UDPcast is a file transfer tool that can send data simultaneously to
many destinations on a LAN. This can for instance be used to install
entire classrooms of PC's at once. The advantage of UDPcast over using
other methods (NFS, FTP, whatever) is that UDPcast uses Ethernet's
multicast abilities: it won't take longer to install 15 machines than
it would to install just 2.

%description -l pl
UDPcast jest narz�dziem do przesy�ania danych jednocze�nie do wielu
lokalizacji w sieci LAN, przyk�adowo do instalacji oprogramowania w
ca�ej pracowni komputerowej za jednym razem. Przewag� UDPcast w
por�wnaniu do innych sposob�w (NFS, FTP czy te� innych) jest to, i�
wykorzystuje mo�liwo�� transmisji multicast - instalacja pi�tnastu
stacji roboczych nie powinna zaj�� wi�cej ni� instalacja dw�ch.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
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
