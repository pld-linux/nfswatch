Summary:	An NFS traffic monitoring tool
Summary(pl.UTF-8):	Narzędzie do monitorowania ruchu NFS
Name:		nfswatch
Version:	4.99.9
Release:	0.1
License:	BSD
Group:		Networking
Source0:	http://dl.sourceforge.net/nfswatch/%{name}-%{version}.tar.gz
# Source0-md5:	0e0735115b99ebe150789c93746f0772
URL:		http://nfswatch.sourceforge.net/
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nfswatch is a command-line tool for monitoring NFS traffic. Nfswatch
can capture and analyze the NFS packets on a particular network
interface or on all interfaces.

%description -l pl.UTF-8
nfswatch to działające z linii poleceń narzędzie do monitorowania
ruchu NFS. nfswatch potrafi wyłapywać i analizować pakiety NFS na
konkretnym interfejsie sieciowym lub wszystkich interfejsach.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	LINUXCFLAGS="%{rpmcflags} -DLINUX -I/usr/include/ncurses"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}/man8,%{_sbindir}}

install nfslogsum nfswatch $RPM_BUILD_ROOT%{_sbindir}
install *.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*
