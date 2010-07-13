%define upstream_name    Parse-RecDescent-FAQ
%define upstream_version 7.3

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Parse::RecDescent::FAQ - the official, authorized FAQ for Parse::RecDescent
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Parse/%{upstream_name}-%{upstream_version}.tar.gz

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Parse::RecDescent::FAQ - the official, authorized FAQ for
Parse::RecDescent.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog
%{perl_vendorlib}/Parse/RecDescent/*
%{_mandir}/*/*
