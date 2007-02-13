#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	File
%define		pnam	Slurp
Summary:	File::Slurp - efficient reading/writing of complete files
Summary(pl.UTF-8):	File::Slurp - wydajny odczyt/zapis całych plików
Name:		perl-File-Slurp
Version:	9999.09
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b2bd4e917b6fafe03145f3977ba8bd7a
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides subs that allow you to read or write entire files
with one simple call. They are designed to be simple to use, have
flexible ways to pass in or get the file contents and to be very
efficient. There is also a sub to read in all the files in a directory
other than . and .. .

Note that these slurp/spew subs work only for files and not for pipes
or stdio. If you want to slurp the latter, use the standard techniques
such as setting $/ to undef, reading <> in a list context, or printing
all you want to STDOUT.

%description -l pl.UTF-8
Ten moduł dostarcza funkcje pozwalające na odczyt lub zapis całych
plików pojedynczym wywołaniem. Zostały zaprojektowane tak, aby były
proste w użyciu, umożliwiały przekazywanie lub pobieranie zawartości
plików w elastyczny sposób oraz były bardzo wydajne. Jest także
funkcja do odczytu wszystkich plików w katalogu innym niż . i .. .

Należy zauważyć, że te funkcje działają tylko dla plików, a nie
potoków czy standardowego wejścia/wyjścia. Dla tych urządzeń pozostają
standardowe techniki, takie jak ustawianie $/ na undef, czytanie <> w
kontekście listy lub pisanie wszystkiego co chcemy na STDOUT.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/%{pdir}/%{pnam}.pm
%{_mandir}/man3/*
