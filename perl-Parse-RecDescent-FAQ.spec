%define real_name Parse-RecDescent-FAQ

Summary:	Parse::RecDescent::FAQ - the official, authorized FAQ for Parse::RecDescent
Name:		perl-%{real_name}
Version:	5.00
Release: %mkrel 2
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Parse::RecDescent::FAQ - the official, authorized FAQ for
Parse::RecDescent.

%prep
%setup -q -n %{real_name}-%{version} 

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
