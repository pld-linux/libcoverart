Summary:	CoverArtArchive client library
Summary(pl.UTF-8):	Biblioteka kliencka CoverArtArchive
Name:		libcoverart
Version:	1.0.0
Release:	1
License:	LGPL v2
Group:		Libraries
#Source0Download: https://github.com/metabrainz/libcoverart/releases/
Source0:	https://github.com/metabrainz/libcoverart/releases/download/release-%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	856d83a4e57a2325c168eb979b9c00d8
URL:		https://musicbrainz.org/doc/libcoverart
BuildRequires:	cmake >= 2.6
BuildRequires:	jansson-devel
BuildRequires:	libstdc++-devel
BuildRequires:	neon-devel >= 0.25
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Cover Art Archive Library (libcoverart), is a development library
geared towards developers who wish to add Cover Art capabilities to
their applications. The library supports Linux and Mac OS X. The data
is mostly gathered from the Cover Art Archive.

%description -l pl.UTF-8
Biblioteka Covert Art Archive (libcoverart) to biblioteka dla
programistów chcących dodać obsługę okładek do aplikacji. Biblioteka
działa na systemach Linux oraz Mac OS X. Dane są pobierane w
większości z Covert Art Archive.

%package devel
Summary:	Header files for coverart library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki coverart
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	jansson-devel
Requires:	libstdc++-devel
Requires:	neon-devel >= 0.25

%description devel
Header files for coverart library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki coverart.

%prep
%setup -q

%build
%cmake .
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NEWS.txt README.md
%attr(755,root,root) %{_libdir}/libcoverart.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcoverart.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcoverart.so
%{_includedir}/coverart
%{_pkgconfigdir}/libcoverart.pc
