# $Id: e-smith-ingo.spec,v 1.8 2010/11/08 04:09:45 mrjhb3 Exp $

Summary: e-smith specific INGO configuration and templates.
%define name e-smith-ingo
Name: %{name}
%define version 2.2.0
%define release 5
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
Patch1: e-smith-ingo_ingo-1.2.2.patch
Patch2: e-smith-ingo-1.2.3.patch
Patch3: e-smith-ingo-1.2.4.patch
Patch4: e-smith-ingo-1.2.5.patch
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildArchitectures: noarch
Requires: imp-h3 >= 4.2
Requires: ingo-h3 >= 1.2
Requires: e-smith-base >= 4.15.1
Requires: e-smith-apache >= 1.1.0-18
Requires: e-smith-lib >= 1.15.1-16
Requires: php
BuildRequires: e-smith-devtools >= 1.13.1-03
AutoReqProv: no
Obsoletes: smeserver-ingo-menuarray

%changelog 
* Sun Nov 07 2010 John H. Bennett III <bennettj@johnbennettservices.com> 2.2.0-5
- Update e-smith-ingo templates to reflect changes in Ingo 1.2.5 [SME: 6352]

* Mon May 10 2010 John H. Bennett III <bennettj@johnbennettservices.com> 2.2.0-4
- Update e-smith-ingo templates to reflect changes in Ingo 1.2.4 [SME: 5940]

* Sat Feb 13 2010 John H. Bennett III <bennettj@johnbennettservices.com> 2.2.0-3
- Update e-smith-ingo templates to reflect changes in Ingo 1.2.3 [SME: 5777]

* Tue Oct 13 2009 John H. Bennett III <bennettj@johnbennettservices.com> 2.2.0-2
- Update e-smith-ingo templates to reflect changes in Ingo 1.2.2 [SME: 5511]

* Tue Oct 7 2008 Shad L. Lords <slords@mail.com> 2.2.0-1.sme
- Roll new stream to separate sme7/sme8 trees [SME: 4633]

* Tue Sep 16 2008 John H. Bennett III <bennettj@johnbennettservices.com> 1.2-2    
- Update to e-smith-ingo templates to reflect changes in Ingo 1.2.1 [SME: 4568]

* Wed Jun 18 2008 John H. Bennett III <bennettj@johnbennettservices.com> 1.2-1    
- Initial production build

* Sat May 24 2008 John H. Bennett III <bennettj@johnbennettservices.com> 1.2-02
- Updated to include changes in Ingo 1.2 RC3
- Re-rolled tarball

* Thu Apr 10 2008 John H. Bennett III <bennettj@johnbennettservices.com> 1.2-01
- Initial build
- Jump in package name to reflect new version of ingo

%description
This package adds necessary templates and configuration items
so that INGO will work properly on SME Server	

%prep
%setup

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
 
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT > %{name}-%{version}-filelist
echo "%doc COPYING"          >> %{name}-%{version}-filelist

%clean 
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
