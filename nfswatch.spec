Summary:	An NFS traffic monitoring tool
Name:		nfswatch
Version:	4.99.5
Release:	0.1
License:	BSD
Group:		Networking
Source0:	http://dl.sourceforge.net/nfswatch/%{name}-%{version}.tar.gz
# Source0-md5:	15c178ade0532a935f0522a9d108b975
URL:		http://nfswatch.sourceforge.net
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nfswatch is a command-line tool for monitoring NFS traffic. Nfswatch
can capture and analyze the NFS packets on a particular network
interface or on all interfaces.

Install nfswatch if you need a program to monitor NFS traffic.

%prep
%setup -q

%build
%{__make} \
	LINUXCFLAGS="-DLINUX -I/usr/include/ncurses"

%install
rm -rf $RPM_BUILD_ROOT
install -d ${RPM_BUILD_ROOT}%{_mandir}/man8
install -d ${RPM_BUILD_ROOT}%{_sbindir}

install nfslogsum nfswatch ${RPM_BUILD_ROOT}%{_sbindir}
install *.8 ${RPM_BUILD_ROOT}%{_mandir}/man8

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*
