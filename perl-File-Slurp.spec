#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	File
%define		pnam	Slurp
Summary:	File::Slurp - efficient reading/writing of complete files
Summary(pl):	File::Slurp - wydajny odczyt/zapis ca³ych plików
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

%description -l pl
Ten modu³ dostarcza funkcje pozwalaj±ce na odczyt lub zapis ca³ych
plików pojedynczym wywo³aniem. Zosta³y zaprojektowane tak, aby by³y
proste w u¿yciu, umo¿liwia³y przekazywanie lub pobieranie zawarto¶ci
plików w elastyczny sposób oraz by³y bardzo wydajne. Jest tak¿e
funkcja do odczytu wszystkich plików w katalogu innym ni¿ . i .. .

Nale¿y zauwa¿yæ, ¿e te funkcje dzia³aj± tylko dla plików, a nie
potoków czy standardowego wej¶cia/wyj¶cia. Dla tych urz±dzeñ pozostaj±
standardowe techniki, takie jak ustawianie $/ na undef, czytanie <> w
kontek¶cie listy lub pisanie wszystkiego co chcemy na STDOUT.

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
