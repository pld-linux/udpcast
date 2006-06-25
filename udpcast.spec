Summary:	UDPcast is a multicast file transfer tool
Summary(pl):	UDPcast - przesy³anie plików przez multicast
Name:		udpcast
Version:	20060619
Release:	1
License:	GPL v2 for main code, BSD-like for fec.c
Group:		Networking
Source0:	http://udpcast.linux.lu/download/%{name}-%{version}.tar.gz
# Source0-md5:	d75202195307aa7e550a381b90541835
Patch0:		%{name}-Makefile.patch
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
UDPcast jest narzêdziem do przesy³ania danych jednocze¶nie do wielu
lokalizacji w sieci LAN, przyk³adowo do instalacji oprogramowania
w ca³ej pracowni komputerowej za jednym razem. Przewag± UDPcast
w porównaniu do innych sposobów (NFS, FTP czy te¿ innych) jest to,
i¿ wykorzystuje mo¿liwo¶æ transmisji multicast - instalacja 15
stacji roboczych nie powinna zaj±æ wiêcej ni¿ 2.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

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
%doc Changelog.txt
