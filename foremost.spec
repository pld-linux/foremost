Summary:	Recover files by "carving" them from a raw disk
Summary(pl):	Odzyskiwanie plik�w poprzez "wykrawanie" ich z dysku
Name:		foremost
Version:	1.3
Release:	1
License:	Public Domain
Group:		Applications/System
Source0:	http://foremost.sourceforge.net/pkg/%{name}-%{version}.tar.gz
# Source0-md5:	73222e54aa0e0e878f58e91cb98f8fbf
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

%description -l pl
Foremost odzyskuje pliki bazuj�c na ich nag��wkach, stopkach, oraz
wewn�trznych strukturach danych. Ten proces jest zwany jako
"wykrawanie" danych. Foremost mo�e pracowa� na "surowym" dost�pie do
dysku lub obrazach utworzonych przez dd. Nag��wki i stopki mog� by�
umieszczone w pliku konfiguracyjnym lub mo�na u�y� linii polece� do
wykorzystania wbudowanych typ�w. Wbudowane typy wskazuj� na struktury
danych podanych format�w plik�w dla pewniejszego i szybszego
odzyskiwania danych.

%prep
%setup -q
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
%doc README CHANGES
%verify(not md5 mtime size) %config(noreplace) %{_sysconfdir}/%{name}.conf
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
