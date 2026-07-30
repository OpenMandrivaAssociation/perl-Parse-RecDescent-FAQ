%define upstream_name    Parse-RecDescent-FAQ
%define upstream_version 7.5
Name:		perl-%{upstream_name}
Version:	7.5
Release:	1

Summary:	Parse::RecDescent::FAQ - the official, authorized FAQ for Parse::RecDescent
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Parse-RecDescent-FAQ
Source0:	https://cpan.metacpan.org/authors/id/T/TB/TBONE/Parse-RecDescent-FAQ-7.5.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

%description
Parse::RecDescent::FAQ - the official, authorized FAQ for
Parse::RecDescent.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc ChangeLog
%{perl_vendorlib}/Parse/RecDescent/*
%{_mandir}/*/*

