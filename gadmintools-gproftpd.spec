# TODO:
# - please do a general checkup of this program
# - please note the patch and check it
# - ensure that everything actually works and is installed
#   as the install scripts are horrible in this package
# - lookup for other BR-s
%define		realname	gproftpd
Summary:	A GTK+ administation tool for the ProFTPD server
Summary(pl.UTF_8):	Narzędzie GTK+ do administracji serwerem ProFTPD
Name:		gadmintools-%{realname}
Version:	8.3.2
Release:	0.1
License:	GPL v2
Group:		Applications/System
Source0:	http://mange.dynalias.org/linux/gproftpd/%{realname}-%{version}.tar.gz
# Source0-md5:	0b8a06c4972a00b912b0afa3ae6ec539
Patch0:		%{name}-install.patch
URL:		http://mange.dynalias.org/linux.html
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	pkgconfig
Requires:	proftpd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GProFTPD is a fast and easy to use GTK+ administration tool for the
proftpd standalone server.

%description -l pl.UTF-8
GProFTPD jest szybkim i łatwym w użyciu narzędziem administracyjnym
dla serwera ProFTPD napisanym w GTK+.

%prep
%setup -q -n %{realname}-%{version}
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{realname}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add %{name}
%service %{name} restart

%preun
if [ "$1" = "0" ]; then
	%service -q %{name} stop
	/sbin/chkconfig --del %{name}
fi

%files -f %{realname}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_sbindir}/%{realname}
%attr(755,root,root) %{_sbindir}/gprostats
%dir %{_sysconfdir}/%{realname}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{realname}/gproftpd.pem
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{realname}/gprotls.conf
%config(noreplace) %verify(not md5 mtime size) /etc/pam.d/%{realname}
%config(noreplace) %verify(not md5 mtime size) /etc/security/console.apps/%{realname}
%{_desktopdir}/%{realname}.desktop
%{_pixmapsdir}/*.png
%dir %{_pixmapsdir}/%{realname}
%{_pixmapsdir}/%{realname}/*.png
%{_pixmapsdir}/%{realname}/%{realname}36.xpm
