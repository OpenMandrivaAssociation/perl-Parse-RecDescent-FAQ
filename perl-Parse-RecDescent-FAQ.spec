%define upstream_name    Parse-RecDescent-FAQ
%define upstream_version 7.5

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Parse::RecDescent::FAQ - the official, authorized FAQ for Parse::RecDescent
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Parse/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Parse::RecDescent::FAQ - the official, authorized FAQ for
Parse::RecDescent.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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

%changelog
* Sat Aug 28 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 7.500.0-1mdv2011.0
+ Revision: 573800
- update to 7.5

* Tue Aug 24 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 7.400.0-1mdv2011.0
+ Revision: 572746
- update to 7.4

* Tue Jul 13 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 7.300.0-1mdv2011.0
+ Revision: 552529
- update to 7.3

* Thu Aug 06 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 6.0.0-1mdv2010.0
+ Revision: 410638
- update to 6.0.f

* Wed Oct 01 2008 Oden Eriksson <oeriksson@mandriva.com> 5.04-4mdv2009.0
+ Revision: 290434
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - update to new version 5.08

* Wed Aug 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 5.04-1mdv2008.0
+ Revision: 69245
- update to new version 5.04

* Sun Jul 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 5.02-1mdv2008.0
+ Revision: 46658
- update to new version 5.02

* Tue May 08 2007 Olivier Thauvin <nanardon@mandriva.org> 5.00-2mdv2008.0
+ Revision: 25190
- rebuild


* Wed Apr 05 2006 Nicolas Lécureuil <neoclust@mandriva.org> 5.00-1mdk
- New release 5.00
- use mkrel

* Thu Aug 18 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 3.94-1mdk
- 3.94

* Wed Jul 13 2005 Oden Eriksson <oeriksson@mandriva.com> 3.91-1mdk
- initial Mandriva package

