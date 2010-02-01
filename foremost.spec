Summary:	Recover files by "carving" them from a raw disk
Summary(pl.UTF-8):	Odzyskiwanie plików poprzez "wykrawanie" ich z dysku
Name:		foremost
Version:	1.5.6
Release:	1
License:	Public Domain
Group:		Applications/System
Source0:	http://foremost.sourceforge.net/pkg/%{name}-%{version}.tar.gz
# Source0-md5:	1ac068f5681bbee679f99d2f9fa7f39f
Patch0:		%{name}-sysconfdir.patch
URL:		http://foremost.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Foremost recovers files files based on their headers, footers, and
internal data structures. This process is commonly referred to as data
carving. Foremost can work on a raw disk drive or image file generated
by dd. The headers and footers can be specified by a configuration
file or you can use command line switches to specify built-in file
types. These built-in types look at the data structures of a given
file format allowing for a more reliable and faster recovery.

%description -l pl.UTF-8
Foremost odzyskuje pliki bazując na ich nagłówkach, stopkach, oraz
wewnętrznych strukturach danych. Ten proces jest zwany jako
"wykrawanie" danych. Foremost może pracować na "surowym" dostępie do
dysku lub obrazach utworzonych przez dd. Nagłówki i stopki mogą być
umieszczone w pliku konfiguracyjnym lub można użyć linii poleceń do
wykorzystania wbudowanych typów. Wbudowane typy wskazują na struktury
danych podanych formatów plików dla pewniejszego i szybszego
odzyskiwania danych.

%prep
%setup -q
sed -i -e 's,\r$,,' main.h
%patch0 -p1

%build
%{__make} \
	RAW_CC="%{__cc}" \
	RAW_FLAGS="%{rpmcflags} -DVERSION=\\\"%{version}\\\"" \
	BIN=%{_bindir} \
	MAN=%{_mandir}/man1 \
	CONF=%{_sysconfdir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_sysconfdir}}

%{__make} install \
	BIN=$RPM_BUILD_ROOT%{_bindir} \
	MAN=$RPM_BUILD_ROOT%{_mandir}/man1 \
	CONF=$RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%verify(not md5 mtime size) %config(noreplace) %{_sysconfdir}/%{name}.conf
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
