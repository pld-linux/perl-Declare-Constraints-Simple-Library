#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Declare
%define	pnam	Constraints-Simple
Summary:	Declare::Constraints::Simple - Declarative Validation of Data Structures
Summary(pl.UTF-8):	Declare::Constraints::Simple - deklaratywna walidacja struktur danych
Name:		perl-Declare-Constraints-Simple
Version:	0.03
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Declare/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	abcd5e9f2dd034deed975601b38d684e
URL:		http://search.cpan.org/dist/Declare-Constraints-Simple/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-aliased
BuildRequires:	perl-Carp-Clan
BuildRequires:	perl-Class-Inspector
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The main purpose of this module is to provide an easy way to build a
profile to validate a data structure. It does this by giving you a set of
declarative keywords in the importing namespace.

%description -l pl.UTF-8
Głównym celem tego modułu jest dostarczenie prostego sposobu budowania
profili służących do walidacji sktryktur danych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Declare/Constraints/*.pm
%{perl_vendorlib}/Declare/Constraints/Simple
%{_mandir}/man3/*
