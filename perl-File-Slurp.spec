%include	/usr/lib/rpm/macros.perl
%define	pdir	File
%define	pnam	Slurp
Summary:	File::Slurp -- single call read & write file routines; read directories
Name:		perl-File-Slurp
Version:	2002.0305
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
These are quickie routines that are meant to save a couple of lines of
code over and over again.  They do not do anything fancy.

read_file() does what you would expect.  If you are using its output in
array context, then it returns an array of lines.  If you are calling
it from scalar context, then returns the entire file in a single string.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_sitelib}/File/Slurp.pm
%{_mandir}/man3/*
